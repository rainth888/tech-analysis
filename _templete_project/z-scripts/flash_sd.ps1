# flash_sd.ps1
param(
    [string]$ImagePath = "E:\BaiduNetdiskDownload\rk3576-sd-buildroot-6.1-arm64-20260413.img",
    [int]$DiskNumber = 2
)

$ErrorActionPreference = "Stop"

# Check Administrator privilege
$principal = [Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()
if (-not $principal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Write-Error "Please run this script as Administrator!"
    exit 1
}

$Disk = Get-Disk -Number $DiskNumber -ErrorAction SilentlyContinue
if (-not $Disk) {
    Write-Error "Disk $DiskNumber not found!"
    exit 1
}

Write-Host "=========================================="
Write-Host "Target Disk Details:"
Write-Host "Number:            $($Disk.Number)"
Write-Host "Friendly Name:     $($Disk.FriendlyName)"
Write-Host "Size:              $([Math]::Round($Disk.Size / 1GB, 2)) GB"
Write-Host "OperationalStatus: $($Disk.OperationalStatus)"
Write-Host "=========================================="

# Confirm the image file exists
if (-not (Test-Path $ImagePath)) {
    Write-Error "Image file $ImagePath not found!"
    exit 1
}

$ImageSize = (Get-Item $ImagePath).Length
Write-Host "Image File: $ImagePath ($([Math]::Round($ImageSize / 1GB, 2)) GB)"
Write-Host "=========================================="

# Offline the disk to unlock all partitions
Write-Host "Setting disk $DiskNumber to Offline to unlock all volumes..."
Set-Disk -Number $DiskNumber -IsOffline $true

$inStream = $null
$outStream = $null

try {
    $diskPath = "\\.\PhysicalDrive$DiskNumber"
    Write-Host "Opening streams..."
    
    $inStream = [System.IO.File]::OpenRead($ImagePath)
    $outStream = New-Object System.IO.FileStream($diskPath, [System.IO.FileMode]::Open, [System.IO.FileAccess]::Write, [System.IO.FileShare]::ReadWrite)

    $buffer = New-Object byte[] (1024 * 1024) # 1MB buffer
    $totalWritten = 0
    $lastReport = 0

    Write-Host "Flashing starting..."
    $sw = [System.Diagnostics.Stopwatch]::StartNew()

    while (($bytesRead = $inStream.Read($buffer, 0, $buffer.Length)) -gt 0) {
        $outStream.Write($buffer, 0, $bytesRead)
        $totalWritten += $bytesRead
        
        # Progress report every 50MB
        if ($totalWritten - $lastReport -ge (50 * 1024 * 1024)) {
            $lastReport = $totalWritten
            $elapsed = $sw.Elapsed.TotalSeconds
            $speed = if ($elapsed -gt 0) { ($totalWritten / 1MB) / $elapsed } else { 0 }
            Write-Host ("Flashed: {0:N2} MB / {1:N2} MB ({2:P0}) - Speed: {3:N2} MB/s" -f ($totalWritten / 1MB), ($ImageSize / 1MB), ($totalWritten / $ImageSize), $speed)
        }
    }

    $sw.Stop()
    $elapsedTotal = $sw.Elapsed.TotalSeconds
    $avgSpeed = if ($elapsedTotal -gt 0) { ($totalWritten / 1MB) / $elapsedTotal } else { 0 }
    Write-Host "=========================================="
    Write-Host ("Flashing completed! Time elapsed: {0:N2} seconds. Average Speed: {1:N2} MB/s" -f $elapsedTotal, $avgSpeed)
    Write-Host "Flushing disk cache..."
    $outStream.Flush()
}
catch {
    Write-Error "Error during flashing: $_"
}
finally {
    if ($inStream) { $inStream.Close(); Write-Host "Input stream closed." }
    if ($outStream) { $outStream.Close(); Write-Host "Output stream closed." }

    Write-Host "Setting disk $DiskNumber to Online..."
    Set-Disk -Number $DiskNumber -IsOffline $false
    Write-Host "Disk $DiskNumber is now online."
}
