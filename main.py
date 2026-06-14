#!/usr/bin/env python3
"""Local LLM Workspace - Claude Code + Ollama Integration

This system uses:
- Claude Code (VS Code) for orchestration
- Local Ollama models for execution
- Zero API costs, 100% local
"""

import sys
import json
import argparse
from typing import Optional, Dict, Any
from pathlib import Path

from core.task_router import TaskRouter
from core.caveman_client import CavemanFormatter
from core.metadata import MetadataTracker
from core.progress import ProgressTracker
from tasks import TASK_MAP


def load_settings() -> Dict[str, Any]:
    """Load settings from settings.json"""
    try:
        with open("settings.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            "mode": "hybrid",
            "local_model": "mistral",
            "claude_model": "claude-sonnet-4-6",
            "enable_caveman": False,
            "caveman_level": "full"
        }


def run_task(
    task_id: str,
    prompt: str,
    mode: Optional[str] = None,
    caveman_level: Optional[str] = None,
    show_tokens: bool = False,
    **kwargs
) -> Dict[str, Any]:
    """Run a task with the specified mode"""

    # Validate task
    if task_id not in TASK_MAP:
        return {
            "error": f"Unknown task: {task_id}. Available: {list(TASK_MAP.keys())}",
            "result": None
        }

    # Load settings
    settings = load_settings()
    mode = mode or settings.get("mode", "hybrid")

    # Load system prompt from task
    task_class = TASK_MAP[task_id]
    system_prompt = task_class.get_system_prompt()

    # Route and execute
    router = TaskRouter(default_mode=mode)
    result = router.route(task_id, prompt, mode=mode, system_prompt=system_prompt)

    # Apply Caveman compression if enabled
    if result.get("result") and (caveman_level or settings.get("enable_caveman")):
        level = caveman_level or settings.get("caveman_level", "full")
        caveman = CavemanFormatter(level)
        original_result = result["result"]
        result["result"] = caveman.compress(original_result, level)

        # Show savings
        if show_tokens:
            saved, percentage = caveman.get_token_savings(original_result, result["result"])
            print(f"\n📊 Token Savings (Caveman {level}):")
            print(f"   Original: ~{len(original_result) // 4} tokens")
            print(f"   Compressed: ~{len(result['result']) // 4} tokens")
            print(f"   Saved: {saved} tokens ({percentage:.1f}%)")

    # Show tokens if requested
    if show_tokens and result.get("tokens"):
        print(f"\n📊 Token Usage:")
        print(f"   Tokens: {result['tokens']}")
        if result.get("cost", 0) > 0:
            print(f"   Cost: ${result['cost']:.4f}")

    return result


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="Local LLM System - Use local Ollama, Claude, or hybrid"
    )

    parser.add_argument("task", help="Task ID: task1, task2, task3")
    parser.add_argument("prompt", help="Your prompt/question")
    parser.add_argument(
        "mode",
        nargs="?",
        default=None,
        help="Mode: local, claude, hybrid (default: from settings.json)"
    )
    parser.add_argument(
        "--caveman",
        help="Caveman compression: lite, full, ultra",
        metavar="LEVEL"
    )
    parser.add_argument(
        "--show-tokens",
        action="store_true",
        help="Show token usage"
    )
    parser.add_argument(
        "--model",
        help="Override model (local mode only)"
    )
    parser.add_argument(
        "--stats",
        action="store_true",
        help="Show usage statistics"
    )
    parser.add_argument(
        "--stats-history",
        action="store_true",
        help="Show historical execution stats"
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=180,
        help="Timeout in seconds (default: 180 for complex tasks)"
    )

    args = parser.parse_args()

    # Handle --stats
    if args.stats:
        print("\n[*] Local LLM System Statistics")
        print("=" * 50)
        print("Modes: local (free), claude (paid), hybrid (recommended)")
        print("\nLocal Mode: Free, private, offline")
        print("Claude Mode: $20-100/month, best quality")
        print("Hybrid Mode: $10-30/month, smart routing")
        print("\nFor historical stats: Use --stats-history flag")
        return

    # Handle --stats-history
    if args.stats_history:
        tracker = MetadataTracker()
        stats = tracker.get_usage_stats()

        if "error" in stats:
            print(f"\n{stats['error']}")
            return

        print("\n" + "=" * 70)
        print("EXECUTION HISTORY & USAGE STATISTICS")
        print("=" * 70)
        print(f"\nTotal runs: {stats['total_runs']}")
        print(f"Local runs: {stats['local_runs']} (FREE)")
        print(f"Claude runs: {stats['claude_runs']} (PAID)")
        print(f"\nTotal tokens used: {stats['total_tokens']}")
        print(f"Total time: {stats['total_time']}s")
        print(f"Total cost: ${stats['total_cost']:.4f}")
        print(f"Avg cost per run: ${stats['avg_cost_per_run']:.6f}")
        print("\n" + "=" * 70)
        print("\nLogs stored in: logs/")
        return

    # Show progress start
    progress = ProgressTracker()
    mode = args.mode or "hybrid"

    progress.show_execution_start(
        task_id=args.task,
        mode=mode,
        prompt=args.prompt,
        timeout=args.timeout
    )

    # Show AI routing prediction (for hybrid mode)
    if mode == "hybrid":
        router = TaskRouter()
        complexity = router.analyze_complexity(args.prompt)
        if complexity == "simple":
            progress.show_hybrid_analysis(complexity, "local", "mistral")
        else:
            progress.show_hybrid_analysis(complexity, "claude", "claude-sonnet-4-6")
    elif mode == "local":
        progress.show_local_execution("mistral")
    elif mode == "claude":
        progress.show_claude_execution("claude-sonnet-4-6")
    elif mode == "semi-hybrid":
        progress.show_semi_hybrid_execution()

    # Run task
    result = run_task(
        task_id=args.task,
        prompt=args.prompt,
        mode=mode,
        caveman_level=args.caveman,
        show_tokens=args.show_tokens,
        timeout=args.timeout
    )

    # Create metadata
    tracker = MetadataTracker()
    metadata = tracker.create_record(
        task_id=args.task,
        prompt=args.prompt,
        mode=args.mode or "hybrid",
        result=result,
        timeout=args.timeout,
        caveman_level=args.caveman
    )

    # Save metadata
    metadata_file = tracker.save_record(metadata)

    # Display result
    if result.get("error"):
        print(f"\n❌ Error: {result['error']}")
        print(f"Metadata saved to: {metadata_file}")
        return 1

    # Show completion info
    ai_type = "Claude API" if result.get("cost", 0) > 0 else "Local Ollama"
    progress.show_completion(
        time_taken=result.get("time", 0),
        tokens=result.get("tokens", 0),
        cost=result.get("cost", 0),
        ai_type=ai_type
    )

    # Show AI usage breakdown
    progress.show_ai_breakdown(
        mode=result.get("mode", mode),
        hybrid_routing=result.get("hybrid_routing"),
        cost=result.get("cost", 0),
        tokens=result.get("tokens", 0)
    )

    # Show the actual response
    print(f"\nRESPONSE:")
    print("-" * 70)
    print(f"\n{result.get('result', 'No result')}\n")

    # Show metadata summary
    tracker.print_summary(metadata)
    print(f"\nMetadata saved to: {metadata_file}")

    # Show stats option
    print("\nTo see usage statistics: python main.py --stats-history")


if __name__ == "__main__":
    sys.exit(main() or 0)
