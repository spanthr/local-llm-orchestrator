"""MCP Server for Local Ollama - Claude Code Integration"""

import json
import sys
from core.ollama_client import LocalOllamaClient


class OllamaMCPServer:
    """MCP server allowing Claude Code to invoke local Ollama"""

    def __init__(self):
        self.client = LocalOllamaClient(model="mistral")
        self.models = ["mistral", "neural-chat", "phi"]

    def run_task(self, task_id: str, prompt: str, model: str = "mistral") -> dict:
        """Run task on local Ollama - called by Claude Code"""

        print(f"\n[MCP] Claude Code → Local Ollama")
        print(f"  Task: {task_id}")
        print(f"  Model: {model}")
        print(f"  Running locally...")

        self.client.model = model
        result = self.client.run(prompt)

        return {
            "status": "success" if not result.get("error") else "error",
            "task_id": task_id,
            "model": model,
            "result": result.get("result"),
            "tokens": result.get("tokens", 0),
            "time": result.get("time", 0),
            "error": result.get("error")
        }

    def list_models(self) -> dict:
        """List available local models"""
        return {
            "models": self.models,
            "default": "mistral"
        }

    def handle_request(self, request_data: str) -> str:
        """Handle MCP request from Claude Code"""
        try:
            request = json.loads(request_data)
            method = request.get("method")
            params = request.get("params", {})

            if method == "run_task":
                result = self.run_task(**params)
            elif method == "list_models":
                result = self.list_models()
            else:
                result = {"error": f"Unknown method: {method}"}

            return json.dumps({"result": result})
        except Exception as e:
            return json.dumps({"error": str(e)})


if __name__ == "__main__":
    server = OllamaMCPServer()

    # Read from stdin, process, write to stdout
    for line in sys.stdin:
        line = line.strip()
        if line:
            response = server.handle_request(line)
            print(response)
            sys.stdout.flush()
