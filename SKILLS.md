# Claude Code Skills - Available Commands

How to use Claude Code skills with your local LLM system.

---

## Quick Reference

```bash
# Basic commands
/code-review              # Review code changes
/simplify                 # Simplify and optimize code
/caveman                  # Compress output (65% fewer tokens)
/verify                   # Test changes in browser
/loop                     # Run command on interval
/schedule                 # Schedule cloud agents
```

---

## Skill: `/code-review`

**What:** Review code for bugs, security, quality

**Usage:**
```bash
/code-review              # Review current branch changes
/code-review high         # Deep review (slower, thorough)
/code-review --fix        # Apply fixes automatically
/code-review --comment    # Post comments on PR
```

**Examples:**

```bash
# Review CARLA code
cd E:\llm_workspace
# Make changes to tasks/task2.py
/code-review

# Output:
# ✓ No security issues
# ✓ Performance: Good
# - Consider: Use class methods instead of functions
# - Fix: Remove unused imports
```

**With Local LLM:**
```bash
# In settings.json, set review_mode: "local"
/code-review              # Uses local Ollama for review
```

**With Claude:**
```bash
# In settings.json, set review_mode: "claude"
/code-review              # Uses Claude for deep review
```

---

## Skill: `/simplify`

**What:** Simplify code, remove duplication, improve efficiency

**Usage:**
```bash
/simplify                 # Simplify current code
/simplify --dry-run       # Show changes without applying
```

**Example - CARLA Code:**

```python
# Before
def get_vehicle_speed():
    client = carla.Client('localhost', 2000)
    world = client.get_world()
    actor = world.get_actors()[0]
    velocity = actor.get_velocity()
    speed = (velocity.x**2 + velocity.y**2)**0.5
    return speed

def get_vehicle_location():
    client = carla.Client('localhost', 2000)
    world = client.get_world()
    actor = world.get_actors()[0]
    location = actor.get_location()
    return location

# After /simplify
class VehicleMonitor:
    def __init__(self):
        self.client = carla.Client('localhost', 2000)
        self.world = self.client.get_world()
        self.vehicle = self.world.get_actors()[0]
    
    def get_speed(self):
        v = self.vehicle.get_velocity()
        return (v.x**2 + v.y**2)**0.5
    
    def get_location(self):
        return self.vehicle.get_location()
```

**Result:**
- Removed 50% duplication
- Added class-based design
- Easier to extend

---

## Skill: `/caveman`

**What:** Compress responses (65% fewer tokens = 65% cheaper)

**Usage:**
```bash
/caveman                  # Use default compression
/caveman lite             # Light compression (30%)
/caveman full             # Full compression (65%)
/caveman ultra            # Maximum compression (80%)
```

**Example:**

```bash
# Original response (1000 tokens, $0.05 cost)
"To plan a trip to Paris, you should consider several factors 
including your budget, the time of year, and your interests. 
Paris is a wonderful destination with many attractions..."

# After /caveman full (350 tokens, $0.02 cost)
"Planning Paris trip? Budget, season, interests matter most.
Top attractions: Eiffel Tower, Louvre, Notre-Dame, Champs-Élysées.
Budget: $50-200/day depending on accommodation. Best time: May-Sept."

# Savings: 650 tokens, $0.03
```

**Enable by default (settings.json):**
```json
{
  "enable_caveman": true,
  "caveman_level": "full"
}
```

---

## Skill: `/verify`

**What:** Test code changes in real browser/app

**Usage:**
```bash
/verify                   # Run app and verify changes
/verify --screenshot      # Take screenshots
/verify --record-video    # Record test run
```

**Example - Testing Holiday Planner:**

```bash
# Make changes to tasks/task1.py
# Add new feature: budget calculator

/verify

# Claude Code:
# 1. Launches local LLM system
# 2. Runs: python main.py task1 "test prompt" local
# 3. Captures output
# 4. Verifies: No errors, budget calculated correctly
# 5. Reports: ✓ Feature working
```

---

## Skill: `/loop`

**What:** Run command on repeating interval

**Usage:**
```bash
/loop 30s python main.py task1 "prompt" hybrid
/loop 5m python main.py --stats
/loop 1h python train.py --check-progress
```

**Example - Monitor Token Usage:**

```bash
/loop 1m python main.py --show-tokens

# Every 1 minute, shows:
# Tokens used this session: 5,234
# Cost: $0.26
# Local (free): 3,000 tokens
# Claude (paid): 2,234 tokens × $0.00003 = $0.07
```

**Example - Train Model Background:**

```bash
/loop 30s python train.py --monitor

# Monitors training:
# Epoch 1/3: Loss 0.45 (50% complete)
# Estimated time: 90 minutes
# GPU: 92% utilized
```

---

## Skill: `/schedule`

**What:** Schedule cloud agents to run at specific times

**Usage:**
```bash
/schedule --cron "0 2 * * *" python main.py task1 "prompt" hybrid
/schedule --time "15:30" python train.py --full
/schedule list                  # List scheduled jobs
/schedule delete job-id         # Remove scheduled job
```

**Example - Nightly Training:**

```bash
/schedule --cron "0 2 * * *" python train.py \
  --data training_data.jsonl \
  --epochs 3 \
  --output model-v2

# Runs at 2 AM every day
# Trains new model overnight
# Results ready in morning
```

---

## Skill: `/update-config`

**What:** Configure settings and permissions

**Usage:**
```bash
/update-config             # Interactive setup
/update-config --permission "allow npm"
/update-config --set "mode=hybrid"
```

**Examples:**

```bash
# Set default mode to hybrid
/update-config --set "mode=hybrid"

# Allow specific commands
/update-config --permission "allow ollama"

# Enable caveman compression
/update-config --set "enable_caveman=true"
```

---

## Combined Skill Examples

### Example 1: Complete Code Review + Fix + Simplify

```bash
# Step 1: Deep code review
/code-review high

# Step 2: Apply fixes
/code-review --fix

# Step 3: Simplify code
/simplify

# Step 4: Compress response
/caveman ultra

# Result: Clean, simple, optimized code
```

### Example 2: Generate → Test → Monitor

```bash
# Step 1: Generate CARLA code
python main.py task2 "Generate ACC code" claude

# Step 2: Test changes
/verify

# Step 3: Monitor performance
/loop 10s python evaluate_carla_code.py

# Step 4: Compress output
/caveman full
```

### Example 3: Train Model with Background Monitoring

```bash
# Step 1: Start training in background
/schedule --cron "0 2 * * *" python train.py --full

# Step 2: Monitor progress
/loop 5m python train.py --check-progress

# Step 3: Get notifications
# (Claude will notify when training completes)
```

---

## Skill Settings (in .claude/settings.json)

```json
{
  "skills": {
    "code_review": {
      "mode": "hybrid",           // local, claude, hybrid
      "effort": "high",            // low, medium, high
      "timeout": 120
    },
    "simplify": {
      "mode": "local",            // Simplify is simple task
      "target_reduction": "30%"   // Reduce lines by 30%
    },
    "caveman": {
      "enabled": true,
      "default_level": "full"     // lite, full, ultra, wenyan
    },
    "verify": {
      "screenshot": true,
      "record_video": false,
      "timeout": 60
    },
    "loop": {
      "max_iterations": 100,
      "capture_output": true
    }
  }
}
```

---

## Integration with Modes

### Local Mode + Skills
```bash
# All code review done locally (free)
/code-review              # Uses Ollama for analysis
/simplify                 # Uses local models
/caveman full             # Compression (works everywhere)
```

**Cost:** Free
**Speed:** Medium
**Quality:** Good (90%)

### Claude Mode + Skills
```bash
# All code review using Claude (best quality)
/code-review high         # Deep Claude analysis
/simplify                 # Claude refactoring
```

**Cost:** $0.05-0.10 per review
**Speed:** Fast
**Quality:** Excellent (100%)

### Hybrid Mode + Skills
```bash
# Smart routing
/code-review              # Analyzes complexity
  → Simple bugs → Ollama (free)
  → Complex refactor → Claude (best)
```

**Cost:** ~$0.02 per review (40% savings)
**Speed:** Fast for simple, medium for complex
**Quality:** Balanced (95%)

---

## Performance Tips

### 1. Use Caveman Always
```bash
/caveman full             # 65% token reduction
# Every skill + caveman = Lower costs
```

### 2. Use Local for Simple Tasks
```bash
/code-review             # For simple code
/simplify                # Code cleanup
# Quick, free, no API cost
```

### 3. Use Claude for Complex
```bash
/code-review high        # Deep architectural review
# Complex analysis needs Claude
```

### 4. Schedule Heavy Work
```bash
/schedule --cron "2 AM" python train.py
# Run expensive tasks at night
```

---

## Troubleshooting Skills

### Skill Not Available
```bash
# Check if installed
/help code-review

# Install/update Claude Code
# VS Code: Extensions → Claude → Update
```

### Too Slow
```bash
# Use local mode instead of Claude
/update-config --set "skill_mode=local"
/code-review              # Now faster, free
```

### Too Expensive
```bash
# Enable caveman everywhere
/update-config --set "enable_caveman=true"

# Use hybrid mode for balance
/update-config --set "mode=hybrid"
```

### Not Working with Local LLM
```bash
# Verify Ollama is running
python core/mcp_ollama_server.py --test

# Check MCP settings
cat .claude/settings.json | grep -A5 "mcp"
```

---

## Keyboard Shortcuts

Add to `~/.claude/keybindings.json`:

```json
{
  "bindings": [
    {
      "key": "ctrl+shift+r",
      "command": "code-review"
    },
    {
      "key": "ctrl+shift+s",
      "command": "simplify"
    },
    {
      "key": "ctrl+shift+c",
      "command": "caveman full"
    },
    {
      "key": "ctrl+shift+v",
      "command": "verify"
    }
  ]
}
```

Then use:
- `Ctrl+Shift+R` → Code review
- `Ctrl+Shift+S` → Simplify
- `Ctrl+Shift+C` → Caveman compress
- `Ctrl+Shift+V` → Verify

---

## Summary Table

| Skill | Cost | Speed | Quality | Use Case |
|-------|------|-------|---------|----------|
| `/code-review local` | Free | 5-10s | Good | Quick feedback |
| `/code-review claude` | $0.05 | 2-5s | Excellent | Deep review |
| `/code-review hybrid` | $0.02 | 3-8s | Balanced | Best value |
| `/simplify` | Free | 5-10s | Good | Code cleanup |
| `/caveman` | Free | 0.5s | Same | 65% cost reduction |
| `/verify` | Free | 30-60s | - | Test changes |
| `/loop` | Variable | - | - | Monitor progress |
| `/schedule` | Variable | - | - | Batch processing |

---

**All skills work with local, Claude, and hybrid modes!**
