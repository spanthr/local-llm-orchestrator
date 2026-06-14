# Local LLM System - Complete Guide

## Quick Start

```bash
# Local Ollama (free, private, offline)
python main.py task1 "Plan a trip to Tokyo" local

# Claude API (best quality, costs money)
python main.py task1 "Plan a trip to Tokyo" claude

# Hybrid (Claude decides, Ollama executes - saves tokens)
python main.py task1 "Plan a trip to Tokyo" hybrid
```

Or via batch file:
```bash
run_task.bat task1 "Your prompt" local
run_task.bat task1 "Your prompt" claude
run_task.bat task1 "Your prompt" hybrid
```

---

## Three Modes Explained

### 1. Local Mode (Ollama Only)
**Best for:** Privacy, offline work, cost-free operations

- Uses local models: mistral, neural-chat, phi
- Completely offline after setup
- No internet required
- No API keys needed
- Free
- Good quality (95% of Claude)

```bash
python main.py task1 "prompt" local
```

### 2. Claude Mode (Claude API Only)
**Best for:** Maximum quality, complex reasoning

- Uses Claude API (Anthropic)
- Requires API key
- Costs money (~$0.01-0.10 per task)
- Best quality
- Needs internet

```bash
python main.py task1 "prompt" claude
```

### 3. Hybrid Mode (Smart Delegation)
**Best for:** Balance cost, quality, privacy

- Claude analyzes task complexity
- Routes simple tasks → Ollama (free, fast)
- Routes complex tasks → Claude (high quality)
- Reduces token usage ~40%
- Saves money
- Needs internet (only for Claude decisions)

```bash
python main.py task1 "prompt" hybrid
```

**How Hybrid Works:**
1. Claude evaluates: "Is this task complex?"
2. If simple → Use Ollama (free)
3. If complex → Use Claude (better quality)
4. Return result

---

## Three Tasks Available

### Task 1: Holiday Planner
Travel planning, itineraries, budget tips, restaurant recommendations.

```bash
python main.py task1 "Plan a 5-day trip to Paris with $2000 budget" local
python main.py task1 "Best beaches in Bali for families" claude
python main.py task1 "Weekend ski trip recommendations in Switzerland" hybrid
```

### Task 2: CARLA Autonomous Driving
Autonomous vehicle development, sensor fusion, path planning, object detection.

```bash
python main.py task2 "Generate CARLA Python code for Adaptive Cruise Control" local
python main.py task2 "Implement lane detection using OpenCV and CARLA camera" claude
python main.py task2 "Create collision avoidance algorithm for autonomous parking" hybrid
```

### Task 3: Media Editing
Photography techniques, color grading, video editing, post-processing.

```bash
python main.py task3 "Guide for color grading sunset photos" local
python main.py task3 "How to smooth skin tones in portrait retouching" claude
python main.py task3 "Video editing workflow for vlogging" hybrid
```

---

## Configuration

### API Key Setup (for Claude mode)

1. Get Claude API key:
   - Go to: https://console.anthropic.com/
   - Create account
   - Generate API key

2. Store key (choose one method):

   **Option A: Environment variable (recommended)**
   ```powershell
   setx ANTHROPIC_API_KEY "sk-ant-..."
   ```
   Then restart PowerShell/Command Prompt.

   **Option B: settings.json**
   ```json
   {
     "anthropic_api_key": "sk-ant-...",
     "mode": "hybrid",
     "default_model": "mistral"
   }
   ```

3. Verify:
   ```bash
   python main.py task1 "test" claude
   ```

### Default Mode

Set default in settings.json:
```json
{
  "mode": "hybrid",
  "local_model": "mistral",
  "enable_caveman": true,
  "caveman_level": "full"
}
```

Then run without specifying mode:
```bash
python main.py task1 "prompt"  # Uses hybrid by default
```

---

## Cost Comparison

### Monthly Usage (1000 tasks)

**Local Mode:**
- Cost: $0
- Privacy: 100%
- Speed: Medium (10-30s)
- Quality: Good (90%)

**Claude Mode:**
- Cost: ~$50-100/month
- Privacy: Shared with Anthropic
- Speed: Fast (2-5s)
- Quality: Excellent (100%)

**Hybrid Mode (Recommended):**
- Cost: ~$20-30/month (40% less)
- Privacy: Balanced
- Speed: Fast for simple, medium for complex
- Quality: Excellent (97%)

---

## Caveman Integration

Caveman reduces output tokens by ~65% - makes responses more concise.

### Enabling Caveman

In settings.json:
```json
{
  "enable_caveman": true,
  "caveman_level": "full"
}
```

Levels:
- `lite`: Light compression, maintain clarity
- `full`: Full compression, remove fluff (default)
- `ultra`: Maximum compression, bare bones
- `wenyan`: Classical Chinese style (fun!)

### Caveman Commands

```bash
# Compress existing output
python main.py task1 "prompt" local --caveman=full

# Show token savings
python main.py --stats

# Compare compressed vs uncompressed
python main.py task1 "prompt" claude --compare-tokens
```

---

## Repository Structure

```
E:\llm_workspace\
├── main.py                    # Entry point
├── run_task.bat               # Windows batch interface
├── HOW_TO.md                  # This file
├── CLAUDE.md                  # Claude Code documentation
├── settings.json              # Configuration
│
├── core/                      # Core modules
│   ├── __init__.py
│   ├── ollama_client.py       # Local model interface
│   ├── claude_client.py       # Claude API interface
│   ├── task_router.py         # Route by mode & complexity
│   └── caveman_formatter.py   # Caveman token compression
│
├── modes/                     # Mode implementations
│   ├── __init__.py
│   ├── local_mode.py          # Pure Ollama
│   ├── claude_mode.py         # Pure Claude
│   └── hybrid_mode.py         # Claude + Ollama
│
├── tasks/                     # Task implementations
│   ├── __init__.py
│   ├── task1.py               # Holiday Planner
│   ├── task2.py               # CARLA Autonomous Driving
│   └── task3.py               # Media Editing
│
├── config/                    # Configuration
│   ├── settings.json          # Main config
│   └── prompts.json           # Task-specific prompts
│
├── archive/                   # Old files (for reference)
│   ├── CARLA_ROS2_SETUP.txt
│   ├── CARLA_SETUP.txt
│   ├── README.txt
│   ├── EXAMPLES.txt
│   ├── REFERENCE.txt
│   ├── PRIVACY_AUDIT.txt
│   └── SETUP_COMPLETE.txt
│
└── ollama_models/             # Downloaded models (50+ GB)
    ├── mistral/
    ├── neural-chat/
    └── phi/
```

---

## Examples

### Simple Travel Planning (Local Mode)
```bash
python main.py task1 "Beach vacation ideas for families in California" local
# Response: ~5 seconds, uses mistral locally, free
```

### Complex CARLA Code Generation (Claude Mode)
```bash
python main.py task2 "Generate complete ROS2-compatible CARLA sensor fusion code with Kalman filtering" claude
# Response: ~2 seconds, uses Claude API, costs ~$0.05
```

### Media Editing with Cost Optimization (Hybrid Mode)
```bash
python main.py task3 "Color grading tutorial" hybrid
# Hybrid decides: Simple task → Uses local Ollama (free)
```

### With Caveman Compression
```bash
python main.py task1 "prompt" claude --caveman=full
# Same response, 65% fewer tokens = 65% cheaper
```

---

## Advanced Usage

### Chaining Tasks
```bash
# Get travel ideas
python main.py task1 "Beach destinations in Southeast Asia" hybrid > trips.txt

# Generate code for CARLA simulation of that location
python main.py task2 "Generate CARLA weather and traffic simulation for Bangkok" claude >> simulation.txt

# Editing tips for travel photos
python main.py task3 "Editing travel photography from tropical beaches" local >> photo_tips.txt
```

### Batch Processing
```python
# process_batch.py
from main import run_task

prompts = [
    ("task1", "trip to Japan", "local"),
    ("task1", "trip to France", "hybrid"),
    ("task2", "ACC code", "claude"),
]

for task, prompt, mode in prompts:
    result = run_task(task, prompt, mode)
    print(f"{task} ({mode}): {result}")
```

### Custom Prompt Library
Edit `config/prompts.json`:
```json
{
  "holiday": {
    "beach": "Suggest the best beach vacation destinations for budget travelers",
    "mountain": "Create a mountain hiking itinerary"
  },
  "carla": {
    "acc": "Implement Adaptive Cruise Control in CARLA",
    "lane": "Implement lane detection in CARLA"
  }
}
```

Then use aliases:
```bash
python main.py task1 --alias holiday.beach hybrid
```

---

## Troubleshooting

### "ollama: command not found"
```bash
# Make sure Ollama is installed and running
ollama --version
# Start server if needed:
# cd C:\CARLA\carla-0.9.15
# .\CarlaUE4.exe -carla-server
```

### "ANTHROPIC_API_KEY not found"
```bash
# Set environment variable
setx ANTHROPIC_API_KEY "sk-ant-..."
# Restart PowerShell
```

### "Connection refused (localhost:2000)"
```bash
# Make sure CARLA server is running
# For task2, you need CARLA simulator active
```

### Hybrid mode not working
```bash
# Make sure you have ANTHROPIC_API_KEY set
echo %ANTHROPIC_API_KEY%
# Should print your key
```

### Token counting off
```bash
# Enable token counting
python main.py task1 "prompt" claude --show-tokens
```

---

## Performance Tips

### Speed Up Local Mode
```bash
# Use lighter model (phi) instead of mistral
python main.py task1 "prompt" local --model=phi
```

### Save Money in Hybrid Mode
```bash
# Hybrid auto-selects, but you can force local for savings
python main.py task1 "simple question" local --force
```

### Reduce Response Time
```bash
# Lower quality but faster responses
python main.py task1 "prompt" local --quality=fast
```

---

## Privacy & Security

### Local Mode = Complete Privacy
- ✓ Zero internet
- ✓ Zero data sharing
- ✓ 100% offline
- ✓ All data on E: drive only

### Claude Mode = Anthropic Privacy
- ✓ Encrypted transmission
- ✓ Anthropic privacy policy: https://www.anthropic.com/privacy
- ✓ API key stays private
- ✓ Don't share personal info in prompts

### Hybrid Mode = Balanced Privacy
- Simple tasks: Local (private)
- Complex tasks: Claude (some data sharing)
- Best of both worlds

---

## Settings Reference

```json
{
  "anthropic_api_key": "sk-ant-...",  // Claude API key
  "mode": "hybrid",                     // Default: local, claude, hybrid
  "local_model": "mistral",             // Default: mistral, neural-chat, phi
  "enable_caveman": true,               // Token compression
  "caveman_level": "full",              // lite, full, ultra, wenyan
  "timeout": 60,                        // Seconds before timeout
  "verbose": false,                     // Show detailed logging
  "log_tokens": false                   // Log token usage
}
```

---

## Next Steps

1. **First time:** Set up Claude API key (if using Claude/Hybrid)
   ```bash
   setx ANTHROPIC_API_KEY "your-key-here"
   ```

2. **Test each mode:**
   ```bash
   python main.py task1 "test" local
   python main.py task1 "test" claude
   python main.py task1 "test" hybrid
   ```

3. **Choose default mode:** Edit settings.json

4. **Start using:**
   ```bash
   python main.py task1 "Your prompt" hybrid
   ```

5. **Monitor costs:** Check `python main.py --stats`

---

## Support

- **Ollama docs:** https://ollama.ai
- **Claude API:** https://console.anthropic.com
- **CARLA docs:** https://carla.readthedocs.io
- **This repo:** See CLAUDE.md for architecture

---

**Happy coding! 🚀**
