# AGENTS.md

## Command Execution

### SafeToAutoRun = true (no confirm needed)
- Read-only: ls, dir, cat, type, head, tail, grep, find, tree, wc, stat, file, echo, df, du
- System info: hostname, whoami, uname, ifconfig, ip, netstat, ping, ps, free, uptime, dmesg, date, env
- Git read: git status, git log, git diff, git branch, git show, git remote
- Build/run: make, gcc, g++, cmake, npm, node, python, cargo, go, gradle, javac, ./build.sh, ./configure
- Package query: pip list, npm list, dpkg -l, apt list, rpm -qa
- File create/copy only: mkdir, cp, copy, scp, tar, chmod, chown, ln -s
- Remote read via plink/ssh: any read-only command above

### BLOCKED (must confirm)
rm, del, Remove-Item,
mv, move, ren, Rename-Item,
format, fdisk, dd, mkfs,
DROP DATABASE, DROP TABLE, truncate,
iptables -F, shutdown, reboot, poweroff,
kill -9, systemctl stop,
git push --force, git reset --hard,
any production data mutation

### File Safety
Before delete/rename/move: backup → `filename.bak.YYYYMMDDhhmmss`, show plan, wait for confirm.

## Formatting
All markdown tables must have aligned columns.
