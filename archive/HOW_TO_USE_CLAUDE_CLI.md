# How to Use Claude CLI for Complete Automated Setup

## QUICKEST METHOD (Recommended)

### Step 1: Download Claude Code

```
VS Code → Extensions → Search "Claude Code" → Install
or
Download from: https://www.anthropic.com/claude-code
```

### Step 2: Copy the Setup Prompt

The complete setup prompt is in: `CLAUDE_CLI_SETUP_PROMPT.md`

Copy everything between the triple backticks starting with "You are a system automation expert..." and ending with "START NOW - Execute all steps..."

### Step 3: Open Claude Code Chat

In VS Code with Claude Code extension:
1. Open the Command Palette (Ctrl+Shift+P)
2. Type "Claude: New Chat"
3. Click to create new chat

### Step 4: Paste and Run

Paste the setup prompt directly into Claude Code chat.

Claude will:
- ✅ Create directories
- ✅ Set environment variables
- ✅ Download models
- ✅ Generate scripts
- ✅ Verify setup
- ✅ Run examples
- ✅ Create documentation

**Total time: 20-30 minutes**

---

## ALTERNATIVE METHOD (Claude CLI Terminal)

### Step 1: Install Claude CLI

```bash
# Windows PowerShell (as Administrator)
pip install anthropic-cli

# Or download: https://github.com/anthropics/anthropic-sdk-python
```

### Step 2: Set API Key

```bash
# Windows PowerShell
$env:ANTHROPIC_API_KEY="your-api-key-here"

# Or set permanently:
[Environment]::SetEnvironmentVariable("ANTHROPIC_API_KEY", "your-api-key", "Machine")
```

### Step 3: Save Prompt to File

Create `setup_prompt.txt` with the complete prompt from `CLAUDE_CLI_SETUP_PROMPT.md`

```bash
# Windows Command Prompt
cd D:\llm_workspace
notepad setup_prompt.txt
# Paste the prompt, save and exit
```

### Step 4: Run Claude CLI Setup

```bash
# Windows Command Prompt
cd D:\llm_workspace
claude -p setup_prompt.txt

# Claude will execute the entire setup
```

---

## STEP-BY-STEP WALKTHROUGH

### What Claude Will Do (In Order)

**PHASE 1: Environment Setup (2 minutes)**
```
1. Create D:\llm_workspace directory
2. Create subdirectories (ollama_models, config, datasets)
3. Set OLLAMA_MODELS environment variable
4. Set OLLAMA_TELEMETRY=false
5. Display: "RESTART YOUR COMPUTER"
6. Wait for user to restart and continue
```

**PHASE 2: Verify Installation (1 minute)**
```
1. Check if Ollama is installed
2. If not: Show download link (https://ollama.ai/download)
3. If yes: Show version number
4. Proceed to next phase
```

**PHASE 3: Download Models (15 minutes)**
```
1. Download mistral (4.1 GB) - ~2 minutes
   D:\llm_workspace\ollama_models\mistral
   
2. Download neural-chat (4.7 GB) - ~3 minutes
   D:\llm_workspace\ollama_models\neural-chat
   
3. Download phi (2.6 GB) - ~1 minute
   D:\llm_workspace\ollama_models\phi

Claude shows:
- [████████████  ] 45% mistral...
- Model name, size, destination
- Estimated time remaining
```

**PHASE 4: Generate Python CLI (2 minutes)**
```
1. Create cli.py with:
   - Task 1: Holiday Planner
   - Task 2: ROS2/CARLA
   - Task 3: Media Editing
   - Privacy controls
   - Error handling
   
2. Save to: D:\llm_workspace\cli.py
3. Verify file created successfully
```

**PHASE 5: Generate Batch Script (1 minute)**
```
1. Create run_task.bat with:
   - Simple command interface
   - Task management
   - Privacy settings
   
2. Save to: D:\llm_workspace\run_task.bat
3. Verify file created successfully
```

**PHASE 6: Run Verification (2 minutes)**
```
1. Check Ollama installed ✓
2. Check environment variables ✓
3. Check models downloaded ✓
4. Check workspace accessible ✓
5. Check Python CLI works ✓
6. Check telemetry disabled ✓
7. Check workspace isolation ✓

Claude shows green checkmarks for each
```

**PHASE 7: Demo Run (3 minutes)**
```
1. python cli.py --list-models
   Shows all 3 models installed
   
2. python cli.py --task task1 --prompt "Plan a trip to Singapore"
   Shows example output
   
3. python cli.py --verify
   Shows privacy settings
```

**PHASE 8: Generate Documentation (1 minute)**
```
1. Create README.txt
   - Quick start guide
   - Example commands
   - Troubleshooting
   
2. Create EXAMPLES.txt
   - Task 1: 3 travel planning examples
   - Task 2: 3 ROS2/CARLA examples
   - Task 3: 3 media editing examples
   
3. Create REFERENCE.txt
   - All commands with examples
   - Model management
   - Settings
   - Troubleshooting
```

**PHASE 9: Privacy Audit (1 minute)**
```
1. Verify no files on C:\ drive
2. Verify OLLAMA_TELEMETRY=false
3. Verify no API keys stored
4. Verify no internet calls
5. Verify all data on external SSD
6. Verify no permission prompts
7. Verify offline capability

All checks pass: ✓
```

**PHASE 10: Completion Report (1 minute)**
```
Claude generates final report:
- Setup complete summary
- All models installed
- All tasks available
- Quick start commands
- Privacy verification
- Next steps
```

---

## WHAT YOU SEE IN CLAUDE CODE

### Before Setup
```
You: [Paste setup prompt]
```

### During Setup
Claude shows live progress:
```
Creating workspace at D:\llm_workspace...
✓ Created ollama_models directory
✓ Created config directory
✓ Created datasets directory
✓ Set OLLAMA_MODELS environment variable
✓ Disabled telemetry

Setting environment variables...
⚠ Computer restart required for changes to take effect

Downloading models...
[████████████░░░░░░░░░░░░░░░░░░░░░░] 30% mistral (1.2 GB / 4.1 GB)

Running verification...
✓ Ollama installed (version 0.x.x)
✓ Environment variables set
✓ Models downloaded (3/3)
✓ Workspace accessible
✓ Python CLI works
✓ Telemetry disabled
✓ Workspace isolation verified

Demo run - Task 1:
Request: "Plan a weekend trip to Singapore"
Response: [Generated travel plan...]

Setup Complete!
```

### After Setup
```
═══════════════════════════════════════════════════════════════
OLLAMA LOCAL LLM - SETUP COMPLETE ✓
═══════════════════════════════════════════════════════════════

All 3 tasks ready to use:
✓ Task 1: Holiday Planner
✓ Task 2: ROS2/CARLA Development  
✓ Task 3: Media Editing

Quick start:
  run_task.bat task1 "Plan a trip to Paris"
  run_task.bat task2 "Generate ACC code"
  run_task.bat task3 "Color grading tips"

Privacy verified: ✓
```

---

## IMMEDIATE NEXT STEPS (After Claude Setup Finishes)

### 1. Try Your First Command (Right Now!)

```bash
cd D:\llm_workspace
run_task.bat task1 "Plan a 3-day trip to Bangkok with 2000 SGD budget"
```

You'll get a travel itinerary in seconds!

### 2. Try All Three Tasks

```bash
# Holiday Planner
run_task.bat task1 "Find luxury hotels in Singapore near Marina Bay"

# ROS2/CARLA
run_task.bat task2 "Generate ROS2 code for Adaptive Cruise Control"

# Media Editing
run_task.bat task3 "How to color grade sunset photos in Lightroom"
```

### 3. Verify Everything

```bash
# Show all installed models
python cli.py --list-models

# Show all tasks
python cli.py --list-tasks

# Verify privacy settings
python cli.py --verify
```

### 4. Customize (Optional)

Edit `D:\llm_workspace\cli.py` to:
- Change system prompts
- Add more tasks
- Adjust model selection
- Modify temperature/creativity settings

---

## TROUBLESHOOTING DURING SETUP

### Issue: "PowerShell requires administrator"

**Solution:** Right-click PowerShell → "Run as Administrator" → Try again

### Issue: "Ollama not found"

**Claude will:** Show download link and pause setup
**You do:** 
1. Download Ollama from https://ollama.ai/download
2. Install and restart
3. Resume the prompt in Claude

### Issue: "Not enough disk space"

**Claude will:** Show required space vs available
**You do:** Free up space on external SSD and retry

### Issue: Model download timeout

**Claude will:** Retry automatically up to 3 times
**You do:** Check internet connection and retry

---

## WHAT MAKES THIS SPECIAL

✅ **Fully Automated** - Claude handles everything, step by step

✅ **Privacy First** - Sets up telemetry disabled, workspace isolated

✅ **Error Handling** - If anything fails, Claude shows exactly what went wrong

✅ **Resumable** - Can restart anytime, won't duplicate work

✅ **Documented** - Creates comprehensive docs automatically

✅ **Verified** - Runs 10 verification checks before completing

✅ **Ready to Use** - Can immediately run all 3 tasks

✅ **No Manual Config** - Claude handles all environment variables

---

## FILE LOCATIONS AFTER SETUP

```
D:\llm_workspace\
├── ollama_models/
│   ├── mistral/           (downloaded by Ollama)
│   ├── neural-chat/       (downloaded by Ollama)
│   └── phi/               (downloaded by Ollama)
├── cli.py                 (generated by Claude)
├── run_task.bat           (generated by Claude)
├── README.txt             (generated by Claude)
├── EXAMPLES.txt           (generated by Claude)
├── REFERENCE.txt          (generated by Claude)
└── config/                (created for future use)
```

---

## EXPECTED TIMELINE

| Phase | Time | What Happens |
|-------|------|--------------|
| Env Setup | 2 min | Directories, variables, restart |
| Verify | 1 min | Check Ollama installed |
| Download Models | 15 min | Download 3 models (7.4 GB total) |
| Generate Scripts | 3 min | Create cli.py and run_task.bat |
| Verify Setup | 2 min | Run all checks |
| Demo Run | 3 min | Show examples working |
| Documentation | 1 min | Create help files |
| Audit | 1 min | Verify privacy |
| Report | 1 min | Final summary |
| **TOTAL** | **~30 min** | Ready to use! |

---

## VERIFICATION CHECKLIST AFTER CLAUDE FINISHES

- [ ] D:\llm_workspace folder exists
- [ ] ollama_models folder has 3 models
- [ ] cli.py file exists and is executable
- [ ] run_task.bat file exists
- [ ] README.txt, EXAMPLES.txt, REFERENCE.txt exist
- [ ] OLLAMA_TELEMETRY=false confirmed
- [ ] Can run: `python cli.py --list-models`
- [ ] Can run: `run_task.bat task1 "test"`
- [ ] Can run: `python cli.py --verify` (all green)
- [ ] No files on C:\ drive (check Windows search)

**All checked?** You're ready to go! 🚀

---

## SUPPORT

**If Claude gets stuck:**

1. **Interrupt:** Press Ctrl+C in terminal
2. **Check:** `python cli.py --verify`
3. **Retry:** Run the prompt again (it's safe)
4. **Manual:** Follow QUICK_START.md manually

**If you need help:**

1. Check: `D:\llm_workspace\REFERENCE.txt`
2. Read: `D:\llm_workspace\EXAMPLES.txt`
3. Verify: `python cli.py --verify`

---

## YOU'RE READY!

**Copy the prompt from `CLAUDE_CLI_SETUP_PROMPT.md` and paste it into Claude Code NOW!**

Claude will handle everything. In 30 minutes, you'll have:
✅ Complete local LLM setup
✅ 3 ready-to-use tasks
✅ All privacy controls enabled
✅ Full documentation
✅ Immediate access to use

**Let Claude Code do the heavy lifting!** 🤖
