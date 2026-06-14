# Local LLM Workspace

**Claude Code + Local Ollama Integration**

Use Claude Code to orchestrate. Local Ollama executes. Zero API costs, 100% local.

---

## Quick Start

### Option 1: Claude Code (Recommended)

```
1. Open VS Code with Claude Code extension
2. Press Ctrl+Shift+I
3. Ask: "Generate CARLA ACC code"
4. Claude invokes local Ollama automatically
5. Get result instantly (FREE!)
```

### Option 2: Terminal

```bash
# Task 1: Holiday Planner
python claude_code_integration.py task1 "Plan a trip to Tokyo"

# Task 2: CARLA Code
python claude_code_integration.py task2 "Generate ACC code"

# Task 3: Media Editing
python claude_code_integration.py task3 "Color grading tips"
```

---

## Three Tasks

- **Task 1**: Holiday Planner - Travel planning, itineraries
- **Task 2**: CARLA Autonomous Driving - ACC, path planning, sensors
- **Task 3**: Media Editing - Color grading, photography, video

---

## Setup

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Download Ollama
https://ollama.ai/download

# 3. Verify Ollama
ollama list

# 4. Ready!
```

---

## System Requirements

- GPU: RTX 2060+ (6GB+ VRAM)
- RAM: 8GB+
- Storage: 20GB for models
- Python: 3.8+

---

## How It Works

```
Claude Code (Your IDE)
  ↓
You ask Claude
  ↓
Claude thinks & decides
  ↓
Claude invokes Local Ollama (MCP)
  ↓
Local Ollama executes (FREE on your GPU)
  ↓
Result in Claude Code
```

**Cost: $0.00** ✓

---

## Features

✅ Zero API costs
✅ Claude Code integration
✅ Real-time progress display
✅ Execution tracking & metadata
✅ Token compression (Caveman)
✅ 3 ready-to-use tasks
✅ 3 local models available

---

## Files

```
├── main.py                    ← CLI interface
├── claude_code_integration.py ← Claude orchestrator
├── core/                      ← Core modules
├── modes/                     ← Execution modes
├── tasks/                     ← Task definitions (3 tasks)
├── prompts/                   ← System prompts
├── .claude/                   ← Claude Code config
└── requirements.txt
```

---

## Next Steps

1. Open VS Code with Claude Code
2. Press Ctrl+Shift+I to chat with Claude
3. Ask: "Generate CARLA code"
4. Watch Claude invoke local Ollama
5. Get result instantly!

---

**Ready? Open VS Code and start using Claude Code!** 🚀
