"""Local mode - use Ollama only"""

import json
from typing import Dict, Any
from core.ollama_client import LocalOllamaClient


class LocalMode:
    """Execute tasks using local Ollama models"""

    def __init__(self, model: str = "mistral"):
        self.model = model
        self.client = LocalOllamaClient(model)

    def execute(
        self,
        task_id: str,
        prompt: str,
        system_prompt: str = None,
        **kwargs
    ) -> Dict[str, Any]:
        """Execute task using local model"""

        # Load system prompt
        if not system_prompt:
            system_prompt = self._load_system_prompt(task_id)

        # Combine prompts
        full_prompt = f"{system_prompt}\n\nUser: {prompt}"

        # Run on local model
        timeout = kwargs.get("timeout", 180)
        result = self.client.run(full_prompt, timeout=timeout)

        return {
            "mode": "local",
            "task_id": task_id,
            "model": self.model,
            "result": result.get("result"),
            "tokens": result.get("tokens", 0),
            "time": result.get("time", 0),
            "cost": 0,  # Local is free
            "error": result.get("error")
        }

    def _load_system_prompt(self, task_id: str) -> str:
        """Load system prompt for task"""
        try:
            with open(f"prompts/{task_id}_system.txt", "r") as f:
                return f.read().strip()
        except FileNotFoundError:
            return f"You are an expert assistant for {task_id}."
