import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

def main():
    print("Initializing Browser...")
    # Initialize the driver
    options = webdriver.ChromeOptions()
    # Use a local user data dir to avoid C: drive space issues
    profile_dir = os.path.abspath("chrome_profile")
    options.add_argument(f"user-data-dir={profile_dir}")
    print(f"Using Chrome profile at: {profile_dir}")
    
    # options.add_argument('--headless') # Open visible for manual login
    driver = webdriver.Chrome(options=options)
    
    list_url = "https://www.douban.com/group/people/87654321/publish"
    failed_urls = set()
    
    try:
        # 1. Login Phase
        print(f"Opening {list_url}...")
        driver.get(list_url)
        print("Please login manually in the browser window.")
        
        # Robust Login Check
        while True:
            try:
                # Check for "Login/Register" link which indicates we are NOT logged in
                # Page source contained: <a href="..." class="nav-login" rel="nofollow">登录/注册</a>
                is_guest = False
                try:
                    driver.find_element(By.CLASS_NAME, "nav-login")
                    is_guest = True
                except:
                    pass
                
                # Check for "Page Not Found" (Page title "页面不存在")
                # If page is not found AND matches the target URL, it likely means we need login to see it.
                title = driver.title
                is_404 = "页面不存在" in title
                
                if is_guest or is_404:
                    print(f"Status: Not Logged In (Guest: {is_guest}, 404: {is_404}).")
                    print("Please log in to your Douban account in the opened window.")
                    
                    # If on 404 page, redirect to login page for convenience
                    if is_404 and "accounts/login" not in driver.current_url:
                        print("Redirecting to login page...")
                        driver.get("https://accounts.douban.com/passport/login")
                    
                    time.sleep(5)
                else:
                    # If "Login/Register" not found, check if we are truly logged in by looking for user account element
                    try:
                        driver.find_element(By.CLASS_NAME, "nav-user-account")
                        
                        # Verify user ID
                        target_user_id = list_url.split("people/")[1].split("/")[0]
                        current_user_id = driver.execute_script("return (window._GLOBAL_NAV && window._GLOBAL_NAV.USER_ID) ? window._GLOBAL_NAV.USER_ID : null;")
                        
                        if current_user_id and current_user_id != target_user_id:
                            print(f"Logged in user ({current_user_id}) does not match target user ({target_user_id}).")
                            print("Logging out to allow switch...")
                            driver.delete_all_cookies()
                            driver.refresh()
                            time.sleep(2)
                            continue
                            
                        print("Login detected! Proceeding...")
                        break
                    except:
                        # "nav-user-account" not found yet, maybe loading or really not logged in
                        print("Waiting for login confirmation (nav-user-account)...")
                        time.sleep(2)
            except Exception as e:
                print(f"Error checking login state: {e}")
                time.sleep(2)
        
        # Navigate back to target list after login confirmation
        if driver.current_url != list_url:
             driver.get(list_url)
             
        time.sleep(3) # Wait for list load
        
        while True:
            print(f"Navigating to list page: {list_url}")
            driver.get(list_url)
            time.sleep(3) # Wait for load
            
            # 2. Find first post
            try:
                # Douban group topic list usually has class 'olt'
                # Attempting to find the first link in the table data with class 'title'
                # Selectors might need adjustment based on actual page structure
                posts = driver.find_elements(By.CSS_SELECTOR, "table.olt td.title > a")
                
                if not posts:
                    print("No posts found with 'table.olt td.title > a'. Trying broader selector...")
                    posts = driver.find_elements(By.CSS_SELECTOR, "div.article table tr td a")

                if not posts:
                    print("Task Complete or No Posts Visible.")
                    break
                
                # Filter out "last_deleted_url" to avoid infinite loop on failed delete
                valid_post = None
                for p in posts:
                    if p.get_attribute('href') not in failed_urls:
                        valid_post = p
                        break
                
                if not valid_post:
                    print("All visible posts have been attempted and failed. Stopping.")
                    break

                first_post = valid_post
                post_title = first_post.text
                post_href = first_post.get_attribute('href')
                print(f"Found post: {post_title} ({post_href})")
                
                # Click the first post
                first_post.click()
                
            except Exception as e:
                print(f"Error finding/clicking post: {e}")
                time.sleep(5)
                continue

            # 3. Delete Post
            try:
                print("Waiting for post page to load...")
                time.sleep(2)
                
                # Find '删除' link. 
                delete_links = driver.find_elements(By.PARTIAL_LINK_TEXT, "删除")
                
                target_delete_link = None
                for link in delete_links:
                    href = link.get_attribute("href")
                    # Usually "remove" is in the URL for deleting topics
                    if href and "remove" in href:
                         target_delete_link = link
                         break
                
                if not target_delete_link and delete_links:
                    # Fallback logic: some delete buttons might not be links or standard
                    target_delete_link = delete_links[0]
                
                if target_delete_link:
                    print(f"Clicking Delete button (JS): {target_delete_link.text}")
                    driver.execute_script("arguments[0].click();", target_delete_link)
                    
                    # 4. Handle Popup
                    print("Waiting for confirmation popup...")
                    time.sleep(3) 
                    
                    # Correct selector based on debug dump:
                    # <div class="author-action-menu-item" data-action="remove"> ... <span>删除</span> ... </div>
                    confirm_buttons = driver.find_elements(By.XPATH, "//div[@class='author-action-menu-item' and @data-action='remove'] | //div[contains(@class, 'dui-dialog')]//a[contains(text(), '删除')] | //div[contains(@class, 'dui-dialog')]//input[@value='删除'] | //a[@class='btn-content' and contains(text(), '删除')] | //a[text()='删除'] | //input[@value='删除']")

                    clicked_confirm = False
                    for btn in confirm_buttons:
                        if btn.is_displayed():
                            # Ensure it's not the original delete link
                            if btn == target_delete_link:
                                continue
                            
                            print(f"Clicking Confirmation button: {btn.text if btn.text else 'Unknown'}")
                            try:
                                driver.execute_script("arguments[0].click();", btn)
                                clicked_confirm = True
                                
                                # Check for a second confirmation alert (native)
                                try:
                                    print("Checking for native confirmation alert...")
                                    time.sleep(1)
                                    alert = driver.switch_to.alert
                                    print(f"Accepting final alert: {alert.text}")
                                    alert.accept()
                                except:
                                    print("No final native alert found.")
                                    
                                break
                            except Exception as click_err:
                                print(f"Failed to click confirmation button: {click_err}")
                    
                    
                    if not clicked_confirm:
                        # Try browser alert as backup
                        try:
                            alert = driver.switch_to.alert
                            print(f"Accepting alert: {alert.text}")
                            alert.accept()
                            clicked_confirm = True
                        except:
                            print("No alert found.")

                    if clicked_confirm:
                        print("Deletion confirmed. Waiting for redirect or result...")
                        time.sleep(3)
                        # Assume success if we didn't crash
                    else:
                        print("Could not find confirmation button. Marking this URL as failed.")
                        print("Dumping page source for debugging popup...")
                        with open("debug_popup.html", "w", encoding="utf-8") as f:
                             f.write(driver.page_source)
                        print(f"Saved debug popup source to {os.path.abspath('debug_popup.html')}")
                        
                        failed_urls.add(post_href)
                        
                else:
                    print("Delete link not found on this page. Already deleted or permission issue?")
                    print("Dumping page source for debugging no delete link...")
                    with open("debug_no_delete.html", "w", encoding="utf-8") as f:
                         f.write(driver.page_source)
                    print(f"Saved debug source to {os.path.abspath('debug_no_delete.html')}")
                    
                    failed_urls.add(post_href)
            
            except Exception as e:
                print(f"Error during deletion process: {e}")
                failed_urls.add(post_href)
                pass
                
    except KeyboardInterrupt:
        print("Stopping script...")
    finally:
        print("Closing browser...")
        driver.quit()

if __name__ == "__main__":
    main()
