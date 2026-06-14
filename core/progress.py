"""Real-time progress and AI usage display"""

import sys
import time
from typing import Optional


class ProgressTracker:
    """Display real-time AI usage while task runs"""

    def __init__(self):
        self.start_time = time.time()

    def show_execution_start(
        self,
        task_id: str,
        mode: str,
        prompt: str,
        timeout: int
    ) -> None:
        """Show execution start info"""
        print("\n" + "=" * 70)
        print("EXECUTING TASK")
        print("=" * 70)
        print(f"\nTask: {task_id.upper()}")
        print(f"Prompt: {prompt[:70]}{'...' if len(prompt) > 70 else ''}")
        print(f"Mode: {mode.upper()}")
        print(f"Timeout: {timeout}s")
        print("\n" + "-" * 70)

    def show_hybrid_analysis(
        self,
        complexity: str,
        routing: str,
        model: str
    ) -> None:
        """Show hybrid mode complexity analysis"""
        print(f"\n[HYBRID MODE]")
        print(f"  Complexity detected: {complexity.upper()}")
        print(f"  Routing to: {routing.upper()} ({model})")

        if routing == "local":
            print(f"  AI: Local Ollama (FREE)")
        else:
            print(f"  AI: Claude API (PAID)")

        print(f"\n[RUNNING...]")

    def show_local_execution(self, model: str) -> None:
        """Show local model execution"""
        print(f"\n[LOCAL MODE]")
        print(f"  Model: {model.upper()}")
        print(f"  AI: Local Ollama (FREE)")
        print(f"  Processing on your GPU...")
        print(f"\n[RUNNING...]")

    def show_claude_execution(self, model: str) -> None:
        """Show Claude API execution"""
        print(f"\n[CLAUDE MODE]")
        print(f"  Model: {model.upper()}")
        print(f"  AI: Anthropic Claude API (PAID)")
        print(f"  Sending to cloud...")
        print(f"\n[RUNNING...]")

    def show_semi_hybrid_execution(self) -> None:
        """Show semi-hybrid execution (Claude optimizes, Local executes)"""
        print(f"\n[SEMI-HYBRID MODE - 80% COST SAVINGS]")
        print(f"  Step 1: Claude analyzes your prompt (CHEAP)")
        print(f"  Step 2: Claude optimizes into detailed instructions")
        print(f"  Step 3: Local Ollama executes optimized prompt (FREE)")
        print(f"  AI: Claude API (optimization only) + Local Ollama (execution)")
        print(f"\n[RUNNING...]")

    def show_completion(
        self,
        time_taken: float,
        tokens: int,
        cost: float,
        ai_type: str
    ) -> None:
        """Show task completion summary"""
        print(f"\n" + "-" * 70)
        print(f"[COMPLETE]")
        print(f"  Time: {time_taken:.2f}s")
        print(f"  Tokens: {tokens}")
        if cost > 0:
            print(f"  Cost: ${cost:.6f} ({ai_type})")
        else:
            print(f"  Cost: FREE ({ai_type})")
        print("-" * 70)

    def show_ai_breakdown(
        self,
        mode: str,
        hybrid_routing: Optional[str] = None,
        cost: float = 0,
        tokens: int = 0
    ) -> None:
        """Show AI usage breakdown"""
        print("\n" + "=" * 70)
        print("AI USAGE BREAKDOWN")
        print("=" * 70)

        if mode == "local":
            print("\n[Local Ollama]")
            print(f"  Status: USED")
            print(f"  Tokens: {tokens}")
            print(f"  Cost: FREE")
            print(f"\n[Claude API]")
            print(f"  Status: NOT USED")

        elif mode == "claude":
            print("\n[Local Ollama]")
            print(f"  Status: NOT USED")
            print(f"\n[Claude API]")
            print(f"  Status: USED")
            print(f"  Tokens: {tokens}")
            if cost > 0:
                print(f"  Cost: ${cost:.6f}")

        elif mode == "hybrid":
            if hybrid_routing == "local":
                print("\n[Local Ollama]")
                print(f"  Status: USED (simple task)")
                print(f"  Tokens: {tokens}")
                print(f"  Cost: FREE")
                print(f"\n[Claude API]")
                print(f"  Status: SKIPPED (not needed)")
            else:
                print("\n[Local Ollama]")
                print(f"  Status: SKIPPED (not needed)")
                print(f"\n[Claude API]")
                print(f"  Status: USED (complex task)")
                print(f"  Tokens: {tokens}")
                if cost > 0:
                    print(f"  Cost: ${cost:.6f}")

        print("=" * 70)
