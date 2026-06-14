# MCP Integration for Local LLM Setup

Connect Ollama Local LLM with MCP (Model Context Protocol) servers for enhanced capabilities.

## Overview

This guide shows how to integrate your Ollama setup with MCP servers to:
- Manage models across platforms
- Access external APIs safely within sandboxed environment
- Automate model downloads and updates
- Monitor model performance
- Enable file storage operations
- Connect to external tools while maintaining privacy

---

## Available MCP Integrations

### 1. Model Management MCP

**Purpose:** Manage Ollama models programmatically

**Configuration:**
```json
{
  "mcpServers": {
    "ollama-models": {
      "command": "python",
      "args": ["mcp_ollama_models.py"],
      "env": {
        "OLLAMA_MODELS": "D:\\llm_workspace\\ollama_models",
        "OLLAMA_TELEMETRY": "false"
      }
    }
  }
}
```

**Available Tools:**
```
- list_models()
- download_model(model_id)
- remove_model(model_id)
- get_model_info(model_id)
- run_inference(model_id, prompt)
```

**Example MCP Script:**
```python
# mcp_ollama_models.py
import subprocess
import json
from pathlib import Path
from mcp.server import Server

server = Server("ollama-models")

@server.tool()
def list_models():
    """List all available Ollama models"""
    result = subprocess.run(['ollama', 'list'], 
                          capture_output=True, 
                          text=True)
    return json.loads(result.stdout)

@server.tool()
def download_model(model_id: str):
    """Download a model from Ollama library"""
    result = subprocess.run(['ollama', 'pull', model_id],
                          capture_output=True,
                          text=True)
    return {"success": result.returncode == 0, "model": model_id}

@server.tool()
def run_inference(model_id: str, prompt: str, max_tokens: int = 256):
    """Run inference on a model"""
    cmd = ['ollama', 'run', model_id, prompt]
    result = subprocess.run(cmd,
                          capture_output=True,
                          text=True,
                          timeout=300)
    return {"output": result.stdout, "success": result.returncode == 0}
```

---

### 2. File Storage MCP

**Purpose:** Safely manage files on external SSD

**Configuration:**
```json
{
  "mcpServers": {
    "storage": {
      "command": "python",
      "args": ["mcp_storage.py"],
      "env": {
        "WORKSPACE_ROOT": "D:\\llm_workspace",
        "ALLOWED_PATHS": "D:\\llm_workspace"
      }
    }
  }
}
```

**Available Tools:**
```
- list_files(directory)
- read_file(path)
- write_file(path, content)
- delete_file(path)
- create_directory(path)
```

**Example MCP Script:**
```python
# mcp_storage.py
import os
from pathlib import Path
from mcp.server import Server

WORKSPACE_ROOT = Path(os.getenv("WORKSPACE_ROOT", "D:\\llm_workspace"))

def validate_path(filepath):
    """Security: Ensure path is within workspace"""
    try:
        Path(filepath).resolve().relative_to(WORKSPACE_ROOT.resolve())
        return True
    except ValueError:
        raise PermissionError(f"Access denied: {filepath}")

server = Server("storage")

@server.tool()
def list_files(directory: str = "."):
    """List files in directory (within workspace)"""
    path = WORKSPACE_ROOT / directory
    validate_path(path)
    return [str(f) for f in path.iterdir()]

@server.tool()
def read_file(filepath: str):
    """Read file content"""
    path = WORKSPACE_ROOT / filepath
    validate_path(path)
    with open(path, 'r') as f:
        return f.read()

@server.tool()
def write_file(filepath: str, content: str):
    """Write file content"""
    path = WORKSPACE_ROOT / filepath
    validate_path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w') as f:
        f.write(content)
    return {"success": True, "path": str(path)}

@server.tool()
def delete_file(filepath: str):
    """Delete file"""
    path = WORKSPACE_ROOT / filepath
    validate_path(path)
    path.unlink()
    return {"success": True}

@server.tool()
def create_directory(dirpath: str):
    """Create directory"""
    path = WORKSPACE_ROOT / dirpath
    validate_path(path)
    path.mkdir(parents=True, exist_ok=True)
    return {"success": True, "path": str(path)}
```

---

### 3. Code Execution MCP (Task 2)

**Purpose:** Test ROS2/CARLA code generation safely

**Configuration:**
```json
{
  "mcpServers": {
    "code-executor": {
      "command": "python",
      "args": ["mcp_code_executor.py"],
      "env": {
        "WORKSPACE_ROOT": "D:\\llm_workspace",
        "PYTHON_PATH": "D:\\llm_workspace\\venv\\Scripts\\python.exe"
      }
    }
  }
}
```

**Available Tools:**
```
- execute_python(code, timeout=30)
- execute_bash(command, timeout=30)
- validate_syntax(code, language)
- lint_code(code, language)
```

**Example MCP Script:**
```python
# mcp_code_executor.py
import subprocess
import tempfile
import os
from pathlib import Path
from mcp.server import Server

WORKSPACE_ROOT = Path(os.getenv("WORKSPACE_ROOT", "D:\\llm_workspace"))

server = Server("code-executor")

@server.tool()
def execute_python(code: str, timeout: int = 30):
    """Execute Python code safely"""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
        f.write(code)
        f.flush()
        
        try:
            result = subprocess.run(
                ['python', f.name],
                capture_output=True,
                text=True,
                timeout=timeout,
                cwd=str(WORKSPACE_ROOT)
            )
            return {
                "success": result.returncode == 0,
                "stdout": result.stdout,
                "stderr": result.stderr
            }
        finally:
            os.unlink(f.name)

@server.tool()
def validate_syntax(code: str, language: str = "python"):
    """Validate code syntax"""
    if language == "python":
        try:
            compile(code, '<string>', 'exec')
            return {"valid": True}
        except SyntaxError as e:
            return {"valid": False, "error": str(e)}
    return {"valid": False, "error": f"Unsupported language: {language}"}

@server.tool()
def lint_code(code: str, language: str = "python"):
    """Lint code for quality"""
    if language == "python":
        try:
            import pylint
            # Run pylint on code
            with tempfile.NamedTemporaryFile(mode='w', suffix='.py') as f:
                f.write(code)
                f.flush()
                result = subprocess.run(
                    ['pylint', f.name],
                    capture_output=True,
                    text=True
                )
                return {"output": result.stdout}
        except ImportError:
            return {"warning": "pylint not installed"}
```

---

### 4. Model Performance MCP

**Purpose:** Monitor and log model performance metrics

**Configuration:**
```json
{
  "mcpServers": {
    "performance-monitor": {
      "command": "python",
      "args": ["mcp_performance_monitor.py"],
      "env": {
        "WORKSPACE_ROOT": "D:\\llm_workspace"
      }
    }
  }
}
```

**Available Tools:**
```
- measure_inference_speed(model_id, prompt_length)
- monitor_gpu_usage()
- log_performance(model_id, metrics)
- get_performance_report(model_id)
```

**Example MCP Script:**
```python
# mcp_performance_monitor.py
import time
import json
import subprocess
from pathlib import Path
from datetime import datetime
from mcp.server import Server

WORKSPACE_ROOT = Path("D:\\llm_workspace")

server = Server("performance-monitor")

@server.tool()
def measure_inference_speed(model_id: str, prompt: str):
    """Measure inference speed"""
    start_time = time.time()
    
    result = subprocess.run(
        ['ollama', 'run', model_id, prompt],
        capture_output=True,
        text=True
    )
    
    duration = time.time() - start_time
    token_count = len(result.stdout.split())
    
    return {
        "model": model_id,
        "duration_seconds": duration,
        "tokens_generated": token_count,
        "tokens_per_second": token_count / duration if duration > 0 else 0
    }

@server.tool()
def monitor_gpu_usage():
    """Monitor GPU usage"""
    try:
        result = subprocess.run(
            ['nvidia-smi', '--query-gpu=memory.used,memory.total', 
             '--format=csv,nounits,noheader'],
            capture_output=True,
            text=True
        )
        used, total = result.stdout.strip().split(',')
        return {
            "gpu_memory_used_mb": int(used),
            "gpu_memory_total_mb": int(total),
            "gpu_memory_percent": (int(used) / int(total)) * 100
        }
    except:
        return {"error": "nvidia-smi not available"}

@server.tool()
def log_performance(model_id: str, metrics: dict):
    """Log performance metrics to file"""
    log_file = WORKSPACE_ROOT / "performance_logs.jsonl"
    
    entry = {
        "timestamp": datetime.now().isoformat(),
        "model": model_id,
        **metrics
    }
    
    with open(log_file, 'a') as f:
        f.write(json.dumps(entry) + '\n')
    
    return {"success": True, "logged_to": str(log_file)}

@server.tool()
def get_performance_report(model_id: str = None):
    """Generate performance report"""
    log_file = WORKSPACE_ROOT / "performance_logs.jsonl"
    
    if not log_file.exists():
        return {"error": "No logs available"}
    
    entries = []
    with open(log_file, 'r') as f:
        for line in f:
            entry = json.loads(line)
            if model_id is None or entry.get('model') == model_id:
                entries.append(entry)
    
    if not entries:
        return {"error": f"No logs for model: {model_id}"}
    
    # Calculate statistics
    speeds = [e.get('tokens_per_second', 0) for e in entries]
    return {
        "model": model_id,
        "total_runs": len(entries),
        "avg_speed": sum(speeds) / len(speeds) if speeds else 0,
        "max_speed": max(speeds) if speeds else 0,
        "min_speed": min(speeds) if speeds else 0
    }
```

---

## Privacy-First MCP Configuration

### Security Settings

Ensure all MCP servers respect privacy and workspace isolation:

```json
{
  "mcpServers": {
    "default-config": {
      "env": {
        "OLLAMA_TELEMETRY": "false",
        "WORKSPACE_ROOT": "D:\\llm_workspace",
        "ALLOWED_PATHS": "D:\\llm_workspace",
        "NO_INTERNET": "true",
        "NO_API_CALLS": "true"
      },
      "timeout": 300,
      "maxRetries": 3
    }
  }
}
```

### Workspace Validation in MCP

All MCP servers should validate paths:

```python
from pathlib import Path

WORKSPACE_ROOT = Path("D:\\llm_workspace")

def secure_path_access(filepath):
    """Ensure path access is within workspace"""
    try:
        resolved = Path(filepath).resolve()
        workspace = WORKSPACE_ROOT.resolve()
        
        # Check if path is within workspace
        resolved.relative_to(workspace)
        return resolved
    except ValueError:
        raise PermissionError(f"Access denied outside workspace: {filepath}")
```

---

## Integration Examples

### Example 1: Automated Model Management

```python
# Use MCP to automatically download and manage models
async def manage_models():
    async with connect_mcp("ollama-models") as client:
        # List current models
        models = await client.call_tool("list_models")
        
        # Download if missing
        if 'mistral' not in str(models):
            result = await client.call_tool("download_model", 
                                           model_id="mistral")
            print(f"Downloaded: {result}")
```

### Example 2: Safe Code Execution for Task 2

```python
# Test generated ROS2 code safely
async def test_ros2_code(code: str):
    async with connect_mcp("code-executor") as client:
        # Validate syntax first
        valid = await client.call_tool("validate_syntax", 
                                      code=code, 
                                      language="python")
        
        if valid['valid']:
            # Execute safely with timeout
            result = await client.call_tool("execute_python", 
                                           code=code,
                                           timeout=10)
            return result
```

### Example 3: Performance Monitoring

```python
# Monitor model performance over time
async def monitor_performance():
    async with connect_mcp("performance-monitor") as client:
        # Measure speed
        metrics = await client.call_tool("measure_inference_speed",
                                        model_id="mistral",
                                        prompt="Test prompt")
        
        # Log metrics
        await client.call_tool("log_performance",
                             model_id="mistral",
                             metrics=metrics)
        
        # Get report
        report = await client.call_tool("get_performance_report",
                                       model_id="mistral")
        print(f"Average speed: {report['avg_speed']} tok/s")
```

---

## Troubleshooting MCP Integration

### Issue: MCP server connection fails

**Solution:** Verify MCP configuration and environment variables
```bash
# Check MCP logs
echo $env:CLAUDE_MCP_DEBUG  # Windows PowerShell
```

### Issue: Permission denied errors

**Solution:** Ensure paths are within WORKSPACE_ROOT
```python
# All paths must validate
WORKSPACE_ROOT / "valid/path/here"  # ✓ OK
"C:\\external\\path"                 # ✗ Denied
```

### Issue: Model operations hang

**Solution:** Set appropriate timeouts
```json
{
  "timeout": 300,  # 5 minutes for downloads
  "maxRetries": 3
}
```

---

## Next Steps

1. **Enable MCP:** Update Claude or your application configuration
2. **Configure Servers:** Add MCP server configs to your workspace
3. **Test Integration:** Run example MCP commands
4. **Monitor:** Use performance MCP to track usage
5. **Extend:** Create custom MCPs for your workflows

---

## Resources

- [MCP Protocol Documentation](https://modelcontextprotocol.io)
- [Ollama API Reference](https://github.com/jmorganca/ollama/blob/main/docs/api.md)
- [Python MCP SDK](https://pypi.org/project/mcp/)

---

**Last Updated:** 2024  
**Status:** Privacy-first design, fully offline
