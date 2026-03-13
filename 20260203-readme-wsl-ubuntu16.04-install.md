# WSL Ubuntu 16.04 Configuration Log (2026-02-03)

This document records the steps taken to install and configure a WSL Ubuntu 16.04 instance (`ubuntu-16.04`), set up network access via the Windows host proxy, and integrate it into Windows Terminal.

## 0. Installation
**Goal**: Import the Ubuntu 16.04 rootfs into WSL.

### Steps Performed:
1.  **Prepare Directory**:
    Ensured `e:\wsl\ubuntu-16.04` exists for the installation.

2.  **Import Distro**:
    Used the `wsl --import` command to install the distribution from the tarball.
    *   **Distro Name**: `ubuntu-16.04`
    *   **Install Location**: `e:\wsl\ubuntu-16.04`
    *   **Source File**: `e:\wsl\ubuntu16.04.tar`

    ```powershell
    wsl --import ubuntu-16.04 e:\wsl\ubuntu-16.04 e:\wsl\ubuntu16.04.tar
    ```

## 1. User Configuration
**Goal**: Set up a default user `bill` with sudo privileges (password: `qwe123!@#`).

### Steps Performed:
1.  **Create User**:
    ```bash
    wsl -d ubuntu-16.04 useradd -m -s /bin/bash bill
    wsl -d ubuntu-16.04 passwd bill  # Set to qwe123!@#
    ```
2.  **Grant Sudo Access**:
    ```bash
    wsl -d ubuntu-16.04 usermod -aG sudo bill
    ```
3.  **Set as Default User**:
    Created/Updated `/etc/wsl.conf`:
    ```ini
    [user]
    default=bill
    ```
    *Note: Required a WSL restart (`wsl -t ubuntu-16.04`) to take effect.*

## 2. Network Configuration
**Goal**: Allow Ubuntu 16.04 to access the internet via the Windows host proxy (port 7890).

### Method: Host IP Extraction
Since WSL2 has a different IP than the host, we dynamically grab the host's IP from the default route.

### Configurations Applied:
1.  **Shell Proxy (`~/.bashrc`)**:
    Added the following script to auto-configure proxy on login:
    ```bash
    # auto-proxy via Windows gateway for WSL2
    GW=$(ip route | awk '/default/ {print $3; exit}')
    export http_proxy="http://$GW:7890"
    export https_proxy="http://$GW:7890"
    export ALL_PROXY="http://$GW:7890"
    export no_proxy="localhost,127.0.0.1,::1,.local,10.0.0.0/8,172.16.0.0/12,192.168.0.0/16"
    ```

2.  **APT Proxy (`/etc/apt/apt.conf.d/80proxy`)**:
    Created this file to allow `sudo apt update` to work (note: hardcoded IP was used initially during setup, but dynamic is preferred if using `apt-proxy-detect` scripts, simplified here to point to host):
    ```
    Acquire::http::Proxy "http://172.19.128.1:7890/";
    Acquire::https::Proxy "http://172.19.128.1:7890/";
    ```
    *(Note: Users may need to update this IP if the WSL network changes significantly, or use the shell variable method for apt if configured).*
    
    *Correction during setup*: Initially tried `sudo echo` which failed due to permissions; resolved by writing as root directly.

## 3. Windows Terminal Integration
**Goal**: Add "Ubuntu 16.04" to the Windows Terminal dropdown menu with a custom icon.

### Steps Performed:
1.  **Download Icon**:
    Downloaded Ubuntu icon to local path to avoid dependency on internet for icon loading.
    *   Source: `https://assets.ubuntu.com/v1/49a1a858-favicon-32x32.png`
    *   Destination: `e:\wsl\ubuntu1604.png`

2.  **Profile Configuration (`settings.json`)**:
    Added the following JSON object to the `profiles.list` array in Windows Terminal settings.
    
    **Important Fix**: initially included `"source": "Microsoft.WSL"`, which caused a "Profile not detected" error because this instance wasn't auto-discovered. Removing that line converted it to a standard custom profile.

    **Final Config**:
    ```json
    {
        "guid": "{c72d8e40-128c-4a11-80e6-9993309a6016}",
        "hidden": false,
        "name": "Ubuntu-16.04",
        "commandline": "wsl.exe -d ubuntu-16.04",
        "icon": "e:\\wsl\\ubuntu1604.png"
    }
    ```

## Summary
The instance is now fully operational:
*   Launched via `wsl -d ubuntu-16.04` or Windows Terminal.
*   Logs in as `bill` automatically.
*   Has internet access for both shell commands (`curl`) and system updates (`apt`).
