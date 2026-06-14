@echo off
REM Ollama Installation Wrapper
REM This runs the PowerShell installation script with Administrator privileges

setlocal enabledelayedexpansion

echo.
echo ╔════════════════════════════════════════╗
echo ║  OLLAMA INSTALLER                       ║
echo ╚════════════════════════════════════════╝
echo.

REM Check if running as Administrator
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo ⚠ This script requires Administrator privileges
    echo.
    echo How to fix:
    echo   1. Right-click Command Prompt
    echo   2. Select "Run as Administrator"
    echo   3. Run: E:\llm_workspace\install_ollama.bat
    echo.
    pause
    exit /b 1
)

REM Run PowerShell script
echo Starting Ollama installation...
echo.

powershell -NoProfile -ExecutionPolicy Bypass -File "E:\llm_workspace\install_ollama.ps1"

if %errorLevel% equ 0 (
    echo.
    echo ✓ Installation complete!
    echo.
    echo Next: Run setup_env.bat and restart your computer
) else (
    echo.
    echo ✗ Installation failed
    echo Try manual download: https://ollama.ai/download
)

pause
