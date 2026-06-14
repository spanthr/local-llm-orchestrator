================================================================================
OLLAMA LOCAL LLM - QUICK START
================================================================================

SETUP COMPLETE ✓
All data stored locally on E:\llm_workspace
No internet, no telemetry, 100% private

INSTALLED MODELS:
  • mistral (4.1GB) - Best quality & speed
  • neural-chat (4.7GB) - Good for instructions
  • phi (2.6GB) - Ultra fast, lightweight

================================================================================
QUICK START - COPY & PASTE THESE COMMANDS
================================================================================

Task 1: Holiday Planner
  run_task.bat task1 "Plan a 3-day trip to Singapore with budget hotels"
  run_task.bat task1 "Suggest restaurants near Tokyo Disneyland"

Task 2: CARLA Autonomous Driving
  run_task.bat task2 "Generate Adaptive Cruise Control code in Python"
  run_task.bat task2 "Create a path planning algorithm for autonomous parking"

Task 3: Media Editing
  run_task.bat task3 "Guide for color grading sunset photography"
  run_task.bat task3 "How to smooth skin tones in portrait editing"

================================================================================
VERIFY PRIVACY & SETUP
================================================================================
run_task.bat verify

This checks:
  ✓ Ollama installed
  ✓ Workspace on E: drive
  ✓ Telemetry disabled
  ✓ Models downloaded

================================================================================
TROUBLESHOOTING
================================================================================

Q: "ollama: command not found"
A: Download from https://ollama.ai/download and restart

Q: "Python not found"
A: Download from https://www.python.org and add to PATH

Q: Model download slow
A: This is normal - depends on your internet
   You can cancel and retry later with: ollama pull [model-name]

Q: Permission denied on setup_env.bat
A: Run Command Prompt as Administrator, then:
   setup_env.bat

================================================================================
NEXT STEPS
================================================================================
1. Run setup_env.bat to set environment variables
2. Restart your computer
3. Try: run_task.bat task1 "Plan a trip"
4. Check: run_task.bat verify
5. Edit cli.py to add custom prompts

For full documentation: see REFERENCE.txt and EXAMPLES.txt
================================================================================
