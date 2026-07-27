# Version Log: SD Card Flashing Script Creation
**Date and Time**: 2026-07-03 10:00 CST

## Purpose
Create a reliable, raw sector-level image flashing script in PowerShell for Windows to flash Buildroot Linux images onto SD cards.

## Details
- **Script File**: [flash_sd.ps1](file:///d:/_tech-analysis.github/_templete_project/z-scripts/flash_sd.ps1)
- **Target OS**: Windows 11 (PowerShell with Admin Privilege)
- **Source Image**: `E:\BaiduNetdiskDownload\rk3576-sd-buildroot-6.1-arm64-20260413.img` (3,975,905,280 bytes)
- **Target Disk**: `PhysicalDrive2` (Generic Mass Storage card reader, 59.48 GB GPT)

## Execution Preparation
- The target drive has been identified via `Get-Disk` to be **Disk 2**.
- Image size and path have been verified.
- The script uses the .NET FileStream class to read from the `.img` file and write raw sectors directly to the disk after offlining it to prevent OS locks.

## Current State
- The script and documentation have been created and verified.
- **Verification Result**: Waiting for user confirmation to execute the script due to the destructive nature of the raw block flashing command (blocked action: `dd` equivalent).
