"""Local Ollama client for running models locally"""

import subprocess
import json
import time
from typing import Optional, Dict, Any


class LocalOllamaClient:
    """Interface to local Ollama models"""

    def __init__(self, model: str = "mistral", host: str = "localhost:2000"):
        self.model = model
        self.host = host
        self.timeout = 180  # 3 minutes for complex tasks

    def health_check(self) -> bool:
        """Verify Ollama is running"""
        try:
            result = subprocess.run(
                ["ollama", "list"],
                capture_output=True,
                timeout=5,
                text=True,
                encoding='utf-8',
                errors='replace'
            )
            return result.returncode == 0
        except Exception as e:
            print(f"✗ Ollama health check failed: {e}")
            return False

    def list_models(self) -> list:
        """List available models"""
        try:
            result = subprocess.run(
                ["ollama", "list"],
                capture_output=True,
                timeout=5,
                text=True,
                encoding='utf-8',
                errors='replace'
            )
            if result.returncode == 0:
                lines = result.stdout.split("\n")[1:]  # Skip header
                models = []
                for line in lines:
                    if line.strip():
                        parts = line.split()
                        if parts:
                            models.append(parts[0])
                return models
            return []
        except Exception as e:
            print(f"✗ Failed to list models: {e}")
            return []

    def run(self, prompt: str, timeout: Optional[int] = None) -> Dict[str, Any]:
        """Run prompt on local model"""
        if not self.health_check():
            return {
                "error": "Ollama not running. Start with: ollama serve",
                "result": None,
                "tokens": 0,
                "time": 0
            }

        timeout = timeout or self.timeout
        start_time = time.time()

        try:
            result = subprocess.run(
                ["ollama", "run", self.model, prompt],
                capture_output=True,
                timeout=timeout,
                text=True,
                encoding='utf-8',
                errors='replace'
            )

            elapsed = time.time() - start_time

            if result.returncode == 0:
                return {
                    "result": result.stdout.strip(),
                    "tokens": self._estimate_tokens(result.stdout),
                    "time": round(elapsed, 2),
                    "model": self.model,
                    "error": None
                }
            else:
                return {
                    "error": result.stderr,
                    "result": None,
                    "tokens": 0,
                    "time": round(elapsed, 2)
                }

        except subprocess.TimeoutExpired:
            return {
                "error": f"Timeout after {timeout}s",
                "result": None,
                "tokens": 0,
                "time": timeout
            }
        except Exception as e:
            return {
                "error": str(e),
                "result": None,
                "tokens": 0,
                "time": round(time.time() - start_time, 2)
            }

    @staticmethod
    def _estimate_tokens(text: str) -> int:
        """Rough estimate of tokens (1 token ≈ 4 characters)"""
        return len(text) // 4
