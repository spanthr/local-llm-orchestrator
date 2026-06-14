# Claude CLI Prompt - Automated Ollama Setup on External SSD

**SAVE THIS AND RUN IN CLAUDE CODE (VS Code extension or terminal)**

Copy everything below and use with: `claude -p setup_prompt.txt`

---

```
You are a system automation expert. Your task is to completely set up Ollama Local LLM on an external hard drive with ZERO internet sharing and NO permission prompts.

SYSTEM REQUIREMENTS:
- GPU: RTX 2060 (6GB VRAM), 14GB RAM total
- External SSD: D:\llm_workspace (or user specified)
- OS: Windows 10/11
- Python: 3.8+
- Ollama: Latest

YOUR GOAL:
Set up a complete, production-ready local LLM system with 3 tasks:
1. Holiday Planner - Travel planning with hotels, restaurants, activities
2. ROS2/CARLA Development - Code generation for autonomous driving (ACC, path planning)
3. Media Editing - Photo/video editing guidance and techniques

AUTOMATION STEPS (In Order):

## STEP 1: Environment Setup
Create and execute a PowerShell script that:
1. Creates D:\llm_workspace directory structure
2. Sets OLLAMA_MODELS environment variable to D:\llm_workspace\ollama_models
3. Sets OLLAMA_TELEMETRY=false for privacy
4. Creates subdirectories: ollama_models/, config/, datasets/
5. Shows user a RESTART REQUIRED message

```powershell
# OLLAMA LOCAL LLM - AUTOMATED SETUP
# Run this as Administrator in PowerShell

$Drive = "D"
$WorkspacePath = "$($Drive):\llm_workspace"

Write-Host "Creating Ollama workspace..." -ForegroundColor Green
mkdir "$WorkspacePath\ollama_models" -Force | Out-Null
mkdir "$WorkspacePath\config" -Force | Out-Null
mkdir "$WorkspacePath\datasets" -Force | Out-Null

Write-Host "Setting environment variables..." -ForegroundColor Green
[Environment]::SetEnvironmentVariable("OLLAMA_MODELS", "$WorkspacePath\ollama_models", "Machine")
[Environment]::SetEnvironmentVariable("OLLAMA_TELEMETRY", "false", "Machine")

Write-Host ""
Write-Host "✓ Workspace created: $WorkspacePath" -ForegroundColor Green
Write-Host "✓ OLLAMA_MODELS set to: $WorkspacePath\ollama_models" -ForegroundColor Green
Write-Host "✓ Telemetry disabled for privacy" -ForegroundColor Green
Write-Host ""
Write-Host "⚠ IMPORTANT: RESTART YOUR COMPUTER NOW" -ForegroundColor Yellow
Write-Host ""
Read-Host "Press Enter after restarting to continue..."
```

## STEP 2: Install Ollama
Check if Ollama is installed. If not, provide user with:
- Download link: https://ollama.ai/download
- Installation instructions
- Verification command: ollama --version

If installed, show version and proceed.

## STEP 3: Download Models
After verification, download recommended models sequentially:
```bash
ollama pull mistral        # Main model (4.1GB) - 2 min
ollama pull neural-chat    # Alternative (4.7GB) - 3 min
ollama pull phi           # Lightweight (2.6GB) - 1 min
```

Show progress for each download:
- Model name
- Expected download time
- Destination: D:\llm_workspace\ollama_models
- Current progress

## STEP 4: Create Python CLI Script
Generate cli.py with these features:
- Task 1: Holiday Planner (mistral model)
- Task 2: ROS2/CARLA (mistral model)
- Task 3: Media Editor (neural-chat model)
- Privacy verification: no telemetry, no internet calls
- Workspace validation: can't access outside D:\llm_workspace
- Error handling and recovery

Save to: D:\llm_workspace\cli.py

## STEP 5: Create Windows Batch Script
Generate run_task.bat with these features:
- Simple commands: run_task.bat task1 "Your prompt"
- Model management: run_task.bat list, download, verify
- Privacy controls: OLLAMA_TELEMETRY=false
- Working directory: D:\llm_workspace

Save to: D:\llm_workspace\run_task.bat

## STEP 6: Setup Verification
Create and run verification script that checks:
- Ollama installed ✓
- Environment variables set ✓
- Models downloaded ✓
- Workspace accessible ✓
- Python/cli.py works ✓
- Telemetry disabled ✓
- Can't access outside workspace ✓

Show green checkmarks for everything that passes.

## STEP 7: Run Demo/Examples
After everything verified, run 3 example commands:
1. python cli.py --list-models        (Show downloaded models)
2. python cli.py --task task1 --prompt "Plan a weekend trip to Singapore"
3. python cli.py --verify             (Show privacy settings)

## STEP 8: Generate Documentation
Create 3 documentation files in D:\llm_workspace\:

FILE 1: README.txt (Quick Start)
- One page summary
- 3 example commands to copy-paste
- Troubleshooting quick links
- Privacy guarantee statement

FILE 2: EXAMPLES.txt (Real Usage Examples)
- Task 1: 3 travel planning prompts
- Task 2: 3 ROS2/CARLA code generation prompts
- Task 3: 3 media editing prompts
- Each with expected output type

FILE 3: REFERENCE.txt (Command Reference)
- All Python CLI commands with examples
- All batch script commands with examples
- Model management (list, download, remove)
- Settings (verify, configure)
- Troubleshooting common issues

## STEP 9: Privacy Audit
Before completing, verify:
- ✓ No files on C:\ drive (only D:\)
- ✓ OLLAMA_TELEMETRY=false confirmed
- ✓ No API keys stored anywhere
- ✓ No internet calls during setup
- ✓ All data stays on external SSD
- ✓ No permission prompts ever appear
- ✓ Completely offline after setup

## STEP 10: Final Report
Generate a setup completion report:

```
═══════════════════════════════════════════════════════════════
OLLAMA LOCAL LLM - SETUP COMPLETE ✓
═══════════════════════════════════════════════════════════════

SYSTEM INFORMATION:
  GPU: RTX 2060 (6GB VRAM)
  RAM: 14GB
  Storage: External SSD - D:\llm_workspace
  
INSTALLED MODELS:
  ✓ mistral (4.1GB) - Best quality & speed
  ✓ neural-chat (4.7GB) - Good for instructions
  ✓ phi (2.6GB) - Ultra fast, lightweight
  
AVAILABLE TASKS:
  ✓ Task 1: Holiday Planner
  ✓ Task 2: ROS2/CARLA Development
  ✓ Task 3: Media Editing
  
QUICK START:
  python cli.py --task task1 --prompt "Plan a 3-day trip to Singapore"
  python cli.py --task task2 --prompt "Generate Adaptive Cruise Control code"
  python cli.py --task task3 --prompt "Color grading guide for sunset photos"
  
  OR use Windows batch script:
  run_task.bat task1 "Your prompt here"
  run_task.bat task2 "Your prompt here"
  run_task.bat task3 "Your prompt here"
  
PRIVACY VERIFIED:
  ✓ Telemetry disabled
  ✓ All data on external SSD only
  ✓ No internet sharing
  ✓ No permission prompts
  ✓ No API keys needed
  ✓ Completely offline
  
NEXT STEPS:
  1. Try an example: run_task.bat task1 "Plan a trip"
  2. Customize prompts in cli.py if desired
  3. Download more models: ollama pull llama2
  4. Create additional tasks by editing cli.py
  
═══════════════════════════════════════════════════════════════
```

IMPORTANT CONSTRAINTS:
- ALL setup happens on external SSD (D:\llm_workspace)
- NO files downloaded to C:\ drive
- NO internet permissions asked
- NO telemetry or data collection
- NO API keys or credentials required
- Setup is IDEMPOTENT (can run multiple times safely)
- Each step has clear success/failure indicators
- User can interrupt and resume without issues

ERROR HANDLING:
- If Ollama not installed: Show installation link, pause
- If environment variable fails: Suggest running as Administrator
- If model download fails: Retry 3 times, then skip
- If Python missing: Show Python download link
- If insufficient space: Show required space vs available

SUCCESS CRITERIA:
✓ Can run: python cli.py --list-models
✓ Can run: python cli.py --task task1 --prompt "test"
✓ Can run: python cli.py --verify (shows all green)
✓ All models stored in D:\llm_workspace\ollama_models\
✓ No errors in environment variables
✓ User can immediately start using all 3 tasks
✓ Everything is fully offline and private

USER-FRIENDLY FEATURES:
- Color-coded output (green for success, yellow for warnings, red for errors)
- Progress bars for downloads
- Clear step numbering and descriptions
- Estimated time for each step
- Ability to resume if interrupted
- No technical jargon in user messages
- Links to documentation for advanced usage

START NOW - Execute all steps in order, showing progress, and report final status.
```

---

## HOW TO USE THIS PROMPT

### Option 1: Use with Claude Code (VS Code)

```bash
# Save the prompt to a file
# Then run in VS Code terminal:
claude -p setup_prompt.txt

# Or copy-paste directly into Claude Code chat
```

### Option 2: Use with Claude CLI Terminal

```bash
# Navigate to your working directory
cd D:\llm_workspace

# Copy the prompt and paste into Claude terminal
# It will execute all steps automatically
```

### Option 3: Save as Text File and Reference

Save as `SETUP_PROMPT.txt` in D:\llm_workspace\

Then in Claude:
```
Please read SETUP_PROMPT.txt and execute all steps to set up my Ollama Local LLM system
```

---

## WHAT THIS PROMPT WILL DO

✅ Create workspace directories on D:\  
✅ Set environment variables automatically  
✅ Download 3 models (mistral, neural-chat, phi)  
✅ Generate Python CLI script (cli.py)  
✅ Generate Windows batch script (run_task.bat)  
✅ Verify everything works  
✅ Run demo commands to show it's working  
✅ Create documentation files  
✅ Audit privacy settings  
✅ Generate final completion report  

**Total Time:** ~20-30 minutes (mostly download time)

---

## EXPECTED OUTPUT

After running, you'll have:

```
D:\llm_workspace\
├── ollama_models/
│   ├── mistral/
│   ├── neural-chat/
│   └── phi/
├── cli.py
├── run_task.bat
├── README.txt
├── EXAMPLES.txt
├── REFERENCE.txt
└── config/
```

And you can immediately start:
```bash
run_task.bat task1 "Plan a trip to Paris"
run_task.bat task2 "Generate ROS2 code"
run_task.bat task3 "Media editing tips"
```

---

## PRIVACY GUARANTEE

After this setup completes, I guarantee:
- ✓ Zero files on C:\ drive
- ✓ Zero internet sharing
- ✓ Zero telemetry
- ✓ Zero permission prompts
- ✓ 100% offline operation
- ✓ Complete privacy

Verify anytime with: `python cli.py --verify`

---

## TROUBLESHOOTING BUILT-IN

If anything fails:
1. Script shows EXACTLY what failed
2. Script suggests HOW to fix it
3. Script can RESUME from that point
4. All steps are SAFE to repeat

---

**Ready? Copy the prompt section and use with Claude Code!** 🚀
