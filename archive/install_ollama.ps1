# Ollama Installer - Automated Setup

$ErrorActionPreference = "Stop"

Write-Host "OLLAMA INSTALLATION AND MODEL DOWNLOAD" -ForegroundColor Cyan
Write-Host ""

# Check if running as Admin
$isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
if (-not $isAdmin) {
    Write-Host "This script needs Administrator privileges" -ForegroundColor Yellow
    Write-Host "Relaunch PowerShell as Administrator and try again" -ForegroundColor Yellow
    exit 1
}

# Step 1: Download Ollama Installer
Write-Host "Step 1: Downloading Ollama Installer..." -ForegroundColor Green
$installerPath = "$env:TEMP\OllamaSetup.exe"
$downloadUrl = "https://ollama.ai/download/OllamaSetup.exe"

try {
    Write-Host "  Source: $downloadUrl" -ForegroundColor Gray
    Write-Host "  Destination: $installerPath" -ForegroundColor Gray

    $ProgressPreference = 'SilentlyContinue'
    Invoke-WebRequest -Uri $downloadUrl -OutFile $installerPath -UseBasicParsing

    if (Test-Path $installerPath) {
        $fileSize = (Get-Item $installerPath).Length / 1MB
        Write-Host "  DONE: Downloaded $('{0:F1}' -f $fileSize) MB" -ForegroundColor Green
    } else {
        throw "Download failed"
    }
} catch {
    Write-Host "  FAILED: $_" -ForegroundColor Red
    Write-Host ""
    Write-Host "Manual download:" -ForegroundColor Yellow
    Write-Host "  1. https://ollama.ai/download" -ForegroundColor White
    Write-Host "  2. Download and run OllamaSetup.exe" -ForegroundColor White
    Write-Host "  3. Restart computer" -ForegroundColor White
    exit 1
}

Write-Host ""

# Step 2: Run Installer
Write-Host "Step 2: Running Ollama Installer..." -ForegroundColor Green
try {
    Write-Host "  Starting installation..." -ForegroundColor Gray
    $process = Start-Process -FilePath $installerPath -Wait -PassThru

    if ($process.ExitCode -eq 0) {
        Write-Host "  DONE: Installation successful" -ForegroundColor Green
    } else {
        Write-Host "  NOTE: Exit code $($process.ExitCode)" -ForegroundColor Yellow
        Write-Host "  Continuing..." -ForegroundColor Gray
    }
} catch {
    Write-Host "  FAILED: $_" -ForegroundColor Red
    exit 1
}

Write-Host ""

# Step 3: Verify Installation
Write-Host "Step 3: Verifying Installation..." -ForegroundColor Green
Start-Sleep -Seconds 5

$ollamaCmd = $null
$ollamaLocations = @(
    "C:\Program Files\Ollama\ollama.exe",
    "C:\Program Files (x86)\Ollama\ollama.exe",
    "$env:LOCALAPPDATA\Ollama\ollama.exe"
)

foreach ($location in $ollamaLocations) {
    if (Test-Path $location) {
        $ollamaCmd = $location
        break
    }
}

if ($ollamaCmd) {
    Write-Host "  DONE: Found $ollamaCmd" -ForegroundColor Green
    $version = & $ollamaCmd --version
    Write-Host "  Version: $version" -ForegroundColor Green
} else {
    Write-Host "  FAILED: Ollama not found" -ForegroundColor Red
    Write-Host ""
    Write-Host "  Try:" -ForegroundColor Yellow
    Write-Host "    1. Restart your computer" -ForegroundColor White
    Write-Host "    2. Run this script again" -ForegroundColor White
    exit 1
}

Write-Host ""

# Step 4: Download Models
Write-Host "Step 4: Downloading AI Models..." -ForegroundColor Green
Write-Host ""

$models = @("mistral", "neural-chat", "phi")
$sizes = @("mistral: 4.1 GB", "neural-chat: 4.7 GB", "phi: 2.6 GB")

for ($i = 0; $i -lt $models.Count; $i++) {
    $model = $models[$i]
    $size = $sizes[$i]
    Write-Host "  Downloading $size..." -ForegroundColor Cyan
    try {
        & $ollamaCmd pull $model
        Write-Host "  DONE: $model" -ForegroundColor Green
    } catch {
        Write-Host "  FAILED: $model - $_" -ForegroundColor Red
    }
    Write-Host ""
}

# Step 5: Summary
Write-Host "SETUP COMPLETE" -ForegroundColor Green
Write-Host ""
Write-Host "Next Steps:" -ForegroundColor Yellow
Write-Host "  1. Run: E:\llm_workspace\setup_env.bat" -ForegroundColor White
Write-Host "  2. Restart your computer" -ForegroundColor White
Write-Host "  3. Run: run_task.bat verify" -ForegroundColor White
Write-Host "  4. Try: run_task.bat task1 'Plan a trip'" -ForegroundColor White
Write-Host ""
