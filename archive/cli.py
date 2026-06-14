#!/usr/bin/env python3
"""Ollama Local LLM CLI - Holiday Planner, ROS2/CARLA, Media Editing"""

import subprocess
import sys
import os
from pathlib import Path

WORKSPACE = Path("E:\\llm_workspace")
MODELS_DIR = WORKSPACE / "ollama_models"
TASKS = {
    "task1": {"name": "Holiday Planner", "model": "mistral"},
    "task2": {"name": "CARLA Autonomous Driving", "model": "mistral"},
    "task3": {"name": "Media Editing", "model": "neural-chat"}
}

def verify_setup():
    """Verify installation and privacy settings"""
    checks = {
        "Ollama installed": subprocess.run(["ollama", "--version"], capture_output=True).returncode == 0,
        "Workspace exists": WORKSPACE.exists(),
        "Models directory": MODELS_DIR.exists(),
        "OLLAMA_TELEMETRY": os.getenv("OLLAMA_TELEMETRY") == "false",
    }

    print("\n" + "="*50)
    print("PRIVACY & SETUP VERIFICATION")
    print("="*50)
    for check, passed in checks.items():
        status = "✓" if passed else "✗"
        print(f"{status} {check}")
    print("="*50)
    return all(checks.values())

def list_models():
    """List installed models"""
    result = subprocess.run(["ollama", "list"], capture_output=True, text=True)
    print(result.stdout)

def run_task(task_id, prompt):
    """Run a task with given prompt"""
    if task_id not in TASKS:
        print(f"Unknown task: {task_id}")
        return

    task = TASKS[task_id]
    model = task["model"]
    name = task["name"]

    print(f"\n{'='*50}")
    print(f"Task: {name}")
    print(f"Model: {model}")
    print(f"{'='*50}\n")

    try:
        result = subprocess.run(
            ["ollama", "run", model, prompt],
            capture_output=True,
            text=True
        )
        print(result.stdout)
        if result.stderr:
            print(f"Note: {result.stderr}", file=sys.stderr)
    except Exception as e:
        print(f"Error: {e}")

def main():
    args = sys.argv[1:]

    if not args or args[0] == "--verify":
        verify_setup()
    elif args[0] == "--list-models":
        list_models()
    elif args[0] == "--task" and len(args) >= 3:
        task_id = args[1]
        prompt = " ".join(args[3:]) if args[2] == "--prompt" else " ".join(args[2:])
        run_task(task_id, prompt)
    else:
        print("""
Ollama Local LLM CLI
Usage:
  python cli.py --verify              (Check setup & privacy)
  python cli.py --list-models         (Show installed models)
  python cli.py --task <id> --prompt "<prompt>"

Tasks:
  task1: Holiday Planner
  task2: ROS2/CARLA Development
  task3: Media Editing
        """)

if __name__ == "__main__":
    main()
