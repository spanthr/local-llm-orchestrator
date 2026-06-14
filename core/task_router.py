"""Task router - routes tasks to local Ollama"""

from typing import Literal, Dict, Any
import json


class TaskRouter:
    """Route tasks to local Ollama execution"""

    def __init__(self, default_mode: str = "local"):
        self.default_mode = default_mode
        self.valid_modes = ["local"]

    def route(
        self,
        task_id: str,
        prompt: str,
        mode: str = None,
        **kwargs
    ) -> Dict[str, Any]:
        """Route task to local Ollama"""
        mode = mode or self.default_mode

        if mode not in self.valid_modes:
            return {
                "error": f"Invalid mode: {mode}. Valid: {self.valid_modes}",
                "result": None
            }

        from modes.local_mode import LocalMode

        if mode == "local":
            executor = LocalMode()
            return executor.execute(task_id, prompt, **kwargs)

    def analyze_complexity(self, prompt: str) -> Literal["simple", "medium", "complex"]:
        """Analyze prompt complexity"""
        word_count = len(prompt.split())
        special_chars = len([c for c in prompt if c in "{}[]()"])

        if word_count < 10 and special_chars == 0:
            return "simple"
        elif word_count < 50 or special_chars < 3:
            return "medium"
        else:
            return "complex"

    def get_best_model(
        self,
        complexity: Literal["simple", "medium", "complex"],
        available_models: list = None
    ) -> str:
        """Get best model for complexity level"""
        if complexity == "simple":
            return "phi"  # Fastest, lightweight
        elif complexity == "medium":
            return "mistral"  # Balanced
        else:
            return "mistral"  # Best quality

    def validate_mode(self, mode: str) -> bool:
        """Validate mode is supported"""
        return mode in self.valid_modes
