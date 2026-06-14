@echo off
REM Local LLM System - Windows Batch Interface
REM Usage: run_task.bat task1 "Your prompt" local
REM Usage: run_task.bat task2 "Your prompt" claude
REM Usage: run_task.bat task3 "Your prompt" hybrid

setlocal enabledelayedexpansion

if "%1"=="" (
    echo.
    echo Local LLM System - Three-mode AI orchestration
    echo.
    echo Usage:
    echo   run_task.bat TASK "PROMPT" MODE
    echo.
    echo Tasks:
    echo   task1  - Holiday Planner
    echo   task2  - CARLA Autonomous Driving
    echo   task3  - Media Editing
    echo.
    echo Modes:
    echo   local   - Free, private, offline (uses Ollama)
    echo   claude  - Best quality (uses Claude API, costs $)
    echo   hybrid  - Smart routing (recommended, saves 40% cost)
    echo.
    echo Examples:
    echo   run_task.bat task1 "Plan a trip to Tokyo" local
    echo   run_task.bat task2 "Generate ACC code" claude
    echo   run_task.bat task3 "Color grading guide" hybrid
    echo.
    pause
    exit /b 1
)

if "%2"=="" (
    echo Error: Prompt required
    echo Usage: run_task.bat TASK "PROMPT" MODE
    pause
    exit /b 1
)

set TASK=%1
set PROMPT=%2
set MODE=%3

if "%MODE%"=="" (
    REM Default to hybrid if not specified
    set MODE=hybrid
)

REM Run Python main.py
python main.py %TASK% "%PROMPT%" %MODE% --show-tokens

pause
