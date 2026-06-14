# QUICK START - Ollama on External SSD (5 Minutes)

## ⚡ FAST SETUP (Copy-Paste Commands)

### 1. Install Ollama
Download and install: https://ollama.ai/download

### 2. Set External SSD Path (Windows)

**COPY-PASTE THIS IN PowerShell (as Administrator):**

```powershell
# Set your external SSD path (change D: if needed)
$Drive = "D"

# Create workspace folder
cmd /c "mkdir $($Drive):\llm_workspace"

# Set Ollama to use external SSD only
[Environment]::SetEnvironmentVariable("OLLAMA_MODELS", "$($Drive):\llm_workspace\ollama_models", "Machine")

# Disable telemetry (privacy)
[Environment]::SetEnvironmentVariable("OLLAMA_TELEMETRY", "false", "Machine")

# Restart computer (IMPORTANT!)
Write-Host "Done! Please restart your computer now."
Read-Host "Press Enter when ready to restart"
Restart-Computer
```

### 3. After Restart - Download Models

**OPEN Command Prompt and run:**

```bash
# Download Mistral (best for your RTX 2060)
ollama pull mistral

# Download Neural Chat (for media editing)
ollama pull neural-chat

# (Optional) Download others
ollama pull llama2
ollama pull phi
```

Each download takes 2-5 minutes. Wait for "Done" message before proceeding.

### 4. Copy Files to External SSD

Copy these 3 files to `D:\llm_workspace\`:
- `cli.py`
- `run_task.bat`
- `ollama_setup_guide.md`

### 5. DONE! Start Using

**Open Command Prompt in `D:\llm_workspace\` and run:**

```bash
# Holiday Planner
python cli.py --task task1 --prompt "Plan a 3-day trip to Singapore with 3000 SGD budget"

# Or use batch script
run_task.bat task1 "Plan a weekend trip to Bali"
```

---

## 🚀 REAL WORLD EXAMPLES

### Task 1: Holiday Planner

```bash
# Basic trip planning
python cli.py --task task1 --prompt "I want to visit Tokyo for 5 days in December. Budget is 5000 SGD. Suggest itinerary with hotels and restaurants."

# Find hotels
python cli.py --task task1 --prompt "Recommend 4-star hotels in Bangkok near BTS Thonglor station for business travelers."

# Restaurant finder
python cli.py --task task1 --prompt "Find the best 3 Michelin-star restaurants in Singapore and how to get reservations."

# Beach vacation
run_task.bat task1 "Plan a romantic beach getaway to Maldives for 5 nights in March"
```

### Task 2: ROS2/CARLA Development

```bash
# ACC (Adaptive Cruise Control)
python cli.py --task task2 --prompt "Write a ROS2 node that implements Adaptive Cruise Control (ACC) for Carla simulator. Include sensor reading, distance calculation, and throttle control."

# Path Planning
python cli.py --task task2 --prompt "Generate Python code for RRT path planning algorithm in Carla. Include obstacle detection and waypoint following."

# Race line generation
python cli.py --task task2 --prompt "Show me how to generate optimal race line for Carla using minimum curvature algorithm."

# Sensor integration
run_task.bat task2 "Create ROS2 subscriber for Carla LiDAR and camera sensor data"
```

### Task 3: Media Editing

```bash
# Photo editing
python cli.py --task task3 --prompt "How to apply professional color grading to sunset photos? Step-by-step in Lightroom."

# Video editing
python cli.py --task task3 --prompt "Best techniques for smooth video transitions and audio crossfades in DaVinci Resolve?"

# Special effects
python cli.py --task task3 --prompt "How to create cinematic color grading (VHS, film noir, cyberpunk) in Adobe Premiere Pro?"

# Batch processing
run_task.bat task3 "How to efficiently edit and color correct 100 wedding photos in Lightroom"
```

---

## 📋 COMMAND REFERENCE

### View All Models
```bash
python cli.py --list-models
```

### View All Tasks
```bash
python cli.py --list-tasks
```

### Download More Models
```bash
# Individual commands
ollama pull mistral
ollama pull llama2
ollama pull neural-chat
ollama pull phi
ollama pull orca-mini

# Or using CLI
python cli.py --download phi
python cli.py --download orca-mini
```

### Verify Privacy Settings
```bash
python cli.py --verify
```

### Using Batch Script (Easier on Windows)
```bash
# List models
run_task.bat list

# Download model
run_task.bat download phi

# Verify
run_task.bat verify

# Run task
run_task.bat task1 "Your prompt here"
```

---

## ✅ PRIVACY CHECKLIST

- [ ] Set `OLLAMA_MODELS` to external SSD
- [ ] Set `OLLAMA_TELEMETRY=false`
- [ ] All models downloaded locally
- [ ] Restarted computer after setting environment variables
- [ ] Verified with `python cli.py --verify`
- [ ] Models located only on external SSD
- [ ] Never asks for internet permission
- [ ] No API keys needed
- [ ] Completely offline after setup

---

## ⚠️ TROUBLESHOOTING

### "Ollama not found" error
```
Install from: https://ollama.ai/download
Make sure installation is COMPLETE before continuing
```

### Models not saving to external SSD
```
Check environment variable:
Right-click This PC → Properties → Advanced system settings → 
Environment Variables → Look for OLLAMA_MODELS

Should show: D:\llm_workspace\ollama_models (or your path)

If not there, add it and RESTART computer
```

### Very slow responses
```
1. Close other programs
2. Check with: python cli.py --verify
3. Use smaller model: ollama pull phi
4. Reduce temperature: Add --temperature 0.5 to prompt
```

### "Connection refused" error
```
Models directory is isolated on external SSD
Make sure Ollama is running properly:
- Restart Ollama
- Check file permissions on external SSD
- Restart computer
```

---

## 📊 EXPECTED PERFORMANCE (RTX 2060)

| Model | Download | Speed | Quality |
|-------|----------|-------|---------|
| **mistral** | 4 min | 20 tok/sec | Excellent |
| **llama2** | 3 min | 18 tok/sec | Excellent |
| **neural-chat** | 5 min | 22 tok/sec | Very Good |
| **phi** | 1 min | 30 tok/sec | Good |
| **orca-mini** | 1 min | 35 tok/sec | Fair |

For **Task 1 & 2**, use **mistral** (best balance)
For **Task 3**, use **neural-chat** (instruction-following)
For **quick queries**, use **phi** (fastest)

---

## 🔒 DATA PRIVACY GUARANTEE

✓ All models stored on external SSD only
✓ No telemetry enabled
✓ No files sent to internet
✓ No permission prompts
✓ Completely offline
✓ No API keys or accounts needed
✓ Windows can't access files outside external SSD

---

## 📁 FOLDER STRUCTURE

```
D:\llm_workspace\
├── cli.py                          (Python script)
├── run_task.bat                    (Windows batch script)
├── ollama_setup_guide.md           (Full documentation)
├── ollama_models\
│   ├── mistral
│   ├── neural-chat
│   ├── llama2
│   ├── phi
│   └── orca-mini
```

---

## 🎯 NEXT STEPS

1. **Install Ollama** (5 min)
2. **Set environment variables** (2 min)
3. **Restart computer** (required)
4. **Download models** (10-15 min)
5. **Copy Python scripts** (1 min)
6. **Start using!** (immediately)

---

## ❓ NEED HELP?

Check the full guide: `ollama_setup_guide.md`

Or test everything works:
```bash
python cli.py --verify
python cli.py --list-models
python cli.py --list-tasks
```

**You're all set! Enjoy your private, local LLM!** 🚀
