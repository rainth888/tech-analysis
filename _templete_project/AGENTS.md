# AGENTS.md

## Command Execution

### ⚠️ Global Exception
- **Any command containing `rm -rf` MUST always require user confirmation**, regardless of any other auto-run rules below.

### SafeToAutoRun = true (no confirm needed)
- **ALL commands** on Windows (PowerShell) and WSL Ubuntu are auto-allowed, **EXCEPT** the blocked commands listed below.
- The following commands are **always** SafeToAutoRun (never ask for confirmation):

### BLOCKED (must confirm)
rm, del, Remove-Item,
mv, move, ren, Rename-Item,
format, fdisk, dd, mkfs,
DROP DATABASE, DROP TABLE, truncate,
iptables -F, shutdown, reboot, poweroff,
kill -9, systemctl stop,
git push --force, git reset --hard,
any production data mutation,
Android compilation (gradlew.bat / gradlew, e.g. assembleDebug, assembleRelease),
Qt compilation (qmake, mingw32-make, nmake, jom for Qt projects)


### File Safety
Before delete/rename/move: backup → `filename.bak.YYYYMMDDhhmmss`, show plan, wait for confirm.

## Formatting
All markdown tables must have aligned columns.


---

## Project Overview
- **Script Directory**: All automation scripts (such as backup and cron setup scripts) are stored in the `.\z-scripts` folder.









