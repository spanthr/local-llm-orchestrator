#!/usr/bin/env python3
"""
Claude Code Integration - Call local Ollama from Claude Code

Usage in Claude Code:
  /invoke local-ollama task2 "your prompt"

Or in terminal:
  python claude_code_integration.py task2 "your prompt"
"""

import sys
import json
from pathlib import Path
from core.mcp_ollama_server import OllamaMCPServer
from core.progress import ProgressTracker
from core.metadata import MetadataTracker


def invoke_local_model(task_id: str, prompt: str, model: str = "mistral") -> dict:
    """Invoke local Ollama model - can be called from Claude Code"""

    server = OllamaMCPServer()

    # Show progress
    progress = ProgressTracker()
    progress.show_execution_start(
        task_id=task_id,
        mode="local",
        prompt=prompt,
        timeout=180
    )
    progress.show_local_execution(model)

    # Execute
    result = server.run_task(task_id, prompt, model)

    # Show completion
    if not result.get("error"):
        progress.show_completion(
            time_taken=result["time"],
            tokens=result["tokens"],
            cost=0,
            ai_type="Local Ollama"
        )

    # Save metadata
    tracker = MetadataTracker()
    metadata = tracker.create_record(
        task_id=task_id,
        prompt=prompt,
        mode="local",
        result=result,
        timeout=180,
        caveman_level=None
    )
    metadata_file = tracker.save_record(metadata)

    # Show result
    print("\n" + "=" * 70)
    print("RESPONSE:")
    print("-" * 70)
    print(result.get("result", "No result"))
    print("\n" + "=" * 70)
    print(f"Metadata saved to: {metadata_file}")

    return result


def main():
    """CLI entry point for Claude Code or terminal"""

    if len(sys.argv) < 3:
        print("Usage: python claude_code_integration.py TASK PROMPT [MODEL]")
        print("\nExample:")
        print('  python claude_code_integration.py task1 "Plan a trip to Tokyo" mistral')
        sys.exit(1)

    task_id = sys.argv[1]
    prompt = sys.argv[2]
    model = sys.argv[3] if len(sys.argv) > 3 else "mistral"

    result = invoke_local_model(task_id, prompt, model)

    # Return result as JSON for Claude Code integration
    return json.dumps(result)


if __name__ == "__main__":
    output = main()
    # Print as JSON for MCP
    if output:
        print("\n[MCP_RESULT]")
        print(output)
