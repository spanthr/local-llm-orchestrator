# Claude Code Integration - Use Claude to Orchestrate Local Ollama

Use Claude Code (in VS Code) to make decisions and automatically invoke local Ollama models.

---

## How It Works

```
Claude Code (in VS Code)
    ↓
You ask Claude a question
    ↓
Claude decides: "This needs code generation"
    ↓
Claude invokes local Ollama (via MCP)
    ↓
Local Ollama executes (FREE)
    ↓
Result back to Claude Code
```

**No API costs!** Claude Code → Local Ollama

---

## Setup (5 minutes)

### 1. Install Claude Code Extension

- Open VS Code
- Extensions → Search "Claude"
- Install "Claude" by Anthropic

### 2. Configure MCP Server

**File: `.claude/settings.json`** (already created)

The MCP server is already configured to call local Ollama.

### 3. Test the Connection

In VS Code Claude Code chat, run:

```
/invoke-local task1 "Plan a trip to Tokyo"
```

Or create a simple Python script that Claude Code can execute:

```python
python claude_code_integration.py task1 "Plan a trip to Tokyo"
```

---

## Usage in Claude Code

### Method 1: Direct Terminal Command

In VS Code terminal:

```bash
python claude_code_integration.py task2 "Generate CARLA ACC code"
```

Claude Code will:
1. Show decision (which model to use)
2. Invoke local Ollama
3. Execute locally (FREE)
4. Show result

### Method 2: Claude Code Chat Integration

In Claude Code chat:

```
You: "Generate CARLA code that launches automatically and runs ACC"
Claude: [Analyzes the request]
Claude: "I'll generate this using local Ollama..."
Claude: [Invokes local Ollama]
Local Ollama: [Executes the generation]
Claude: [Shows result]
```

---

## How Claude Decides

Claude Code:
1. Reads your prompt
2. Decides: What model is needed?
3. Calls appropriate executor:
   - **Simple tasks** → Local Ollama (fast, free)
   - **Complex code** → Local Ollama (still free)
   - **Everything** → Your local GPU

---

## Example Workflows

### Workflow 1: Generate Code

```
You (in Claude Code): "Generate CARLA adaptive cruise control code"
↓
Claude (decides): "This is code generation, use local Ollama"
↓
Claude invokes: python claude_code_integration.py task2 "..."
↓
Local Ollama: Generates the code (FREE)
↓
Result appears in Claude Code
```

### Workflow 2: Explain & Generate

```
You: "Explain how ACC works and give me code"
↓
Claude: "Here's the explanation [typed by Claude]
         Now let me generate the code locally..."
↓
Claude invokes: python claude_code_integration.py task2 "..."
↓
Local Ollama: Generates code (FREE)
↓
Both explanation + code in Claude Code
```

### Workflow 3: Iterate

```
You: "That code needs to handle edge cases"
↓
Claude: "Let me improve it with local Ollama..."
↓
Local Ollama: Generates improved version (FREE)
↓
Back and forth - no API costs!
```

---

## Cost Breakdown

| What | Cost | Where |
|------|------|-------|
| Claude thinking | FREE | Claude Code (you use it anyway) |
| Decision making | FREE | Claude Code |
| Task execution | FREE | Local Ollama on your GPU |
| Total | **$0.00** | ✓ |

---

## Commands You Can Use

```bash
# From Claude Code terminal or any terminal:

# Task 1: Holiday Planner
python claude_code_integration.py task1 "Plan a trip to Tokyo"

# Task 2: CARLA Code
python claude_code_integration.py task2 "Generate ACC code"

# Task 3: Media Editing
python claude_code_integration.py task3 "Color grading guide"

# Custom prompt
python claude_code_integration.py task2 "Your custom prompt here"

# Specify model
python claude_code_integration.py task2 "prompt" phi
```

---

## The Perfect Workflow

1. **Open VS Code** with Claude Code extension
2. **Start Claude Code chat** (Ctrl+Shift+I or Cmd+Shift+I)
3. **Ask Claude** your question
4. **Claude analyzes** and decides what to do
5. **Claude invokes** local Ollama when needed
6. **You get result** instantly (no API costs!)

---

## Why This is Better

| vs Pure Claude API | vs Pure Local |
|---|---|
| ✓ Free (no API) | ✓ Claude's intelligence |
| ✓ Claude's thinking | ✓ Fast (local execution) |
| ✓ Local execution | ✓ No network delays |
| ✓ No internet delays | ✓ Orchestration included |
| ✓ Smart routing | ✓ Decision making |

---

## Already Configured

Everything is set up! Just use it:

```
In VS Code:
  - Claude Code is running
  - Local Ollama is ready
  - MCP server is configured
  - Integration script exists
  
Ready to go! 🚀
```

---

## Troubleshooting

**Q: "Command not found"**
```bash
# Make sure you're in the project directory
cd E:\repos_external\LLM_Training
python claude_code_integration.py task1 "test"
```

**Q: "Ollama not running"**
```bash
# Start Ollama server
ollama serve
# In new terminal, run your command
```

**Q: "Connection refused"**
```bash
# Check Ollama is listening on localhost:2000
ollama list
```

---

## Next Steps

1. Open VS Code with Claude Code
2. Start a chat: Ctrl+Shift+I
3. Ask Claude something: "Generate CARLA code"
4. Claude will invoke local Ollama automatically
5. Get result instantly, no costs!

**That's it! You're using Claude + Local Ollama for free.** 🎉
