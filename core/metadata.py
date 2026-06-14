"""Metadata tracking for task execution"""

import json
import os
from datetime import datetime
from typing import Dict, Any
from pathlib import Path


class MetadataTracker:
    """Track and save execution metadata"""

    def __init__(self, logs_dir: str = "logs"):
        self.logs_dir = Path(logs_dir)
        self.logs_dir.mkdir(exist_ok=True)

    def create_record(
        self,
        task_id: str,
        prompt: str,
        mode: str,
        result: Dict[str, Any],
        timeout: int = 180,
        caveman_level: str = None
    ) -> Dict[str, Any]:
        """Create execution metadata record"""

        timestamp = datetime.now()

        record = {
            "timestamp": timestamp.isoformat(),
            "task": {
                "id": task_id,
                "prompt": prompt,
                "prompt_length": len(prompt),
                "prompt_words": len(prompt.split())
            },
            "execution": {
                "mode": mode,
                "timeout": timeout,
                "caveman_enabled": caveman_level is not None,
                "caveman_level": caveman_level
            },
            "ai_usage": {
                "model": result.get("model"),
                "hybrid_complexity": result.get("hybrid_complexity"),
                "hybrid_routing": result.get("hybrid_routing"),
                "tokens_used": result.get("tokens", 0),
                "time_seconds": result.get("time", 0),
                "cost_usd": result.get("cost", 0)
            },
            "status": "success" if not result.get("error") else "error",
            "error": result.get("error")
        }

        return record

    def save_record(self, record: Dict[str, Any]) -> str:
        """Save record to file and return path"""

        timestamp = datetime.fromisoformat(record["timestamp"])
        filename = f"{timestamp.strftime('%Y%m%d_%H%M%S')}__{record['task']['id']}.json"
        filepath = self.logs_dir / filename

        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(record, f, indent=2, ensure_ascii=False)

        return str(filepath)

    def print_summary(self, record: Dict[str, Any]) -> None:
        """Print metadata summary"""

        print("\n" + "=" * 70)
        print("EXECUTION METADATA")
        print("=" * 70)

        # Task info
        print("\nTask:")
        print(f"  ID: {record['task']['id']}")
        print(f"  Prompt: {record['task']['prompt'][:60]}...")
        print(f"  Length: {record['task']['prompt_length']} chars, {record['task']['prompt_words']} words")

        # Execution info
        print("\nExecution:")
        print(f"  Mode: {record['execution']['mode'].upper()}")
        print(f"  Timeout: {record['execution']['timeout']}s")
        if record['execution']['caveman_enabled']:
            print(f"  Caveman: {record['execution']['caveman_level']}")

        # AI Usage
        print("\nAI Usage:")
        print(f"  Model: {record['ai_usage']['model']}")
        if record['ai_usage']['hybrid_complexity']:
            print(f"  Complexity: {record['ai_usage']['hybrid_complexity']}")
            print(f"  Routed to: {record['ai_usage']['hybrid_routing']}")
        print(f"  Tokens: {record['ai_usage']['tokens_used']}")
        print(f"  Time: {record['ai_usage']['time_seconds']}s")
        if record['ai_usage']['cost_usd'] > 0:
            print(f"  Cost: ${record['ai_usage']['cost_usd']:.6f}")
        else:
            print(f"  Cost: FREE (local)")

        # Status
        status_symbol = "✓" if record['status'] == "success" else "✗"
        print(f"\nStatus: {status_symbol} {record['status'].upper()}")
        if record['error']:
            print(f"Error: {record['error']}")

        print("=" * 70)

    def get_usage_stats(self) -> Dict[str, Any]:
        """Get aggregated usage statistics"""

        if not self.logs_dir.exists():
            return {}

        records = []
        for filepath in self.logs_dir.glob("*.json"):
            try:
                with open(filepath, "r") as f:
                    records.append(json.load(f))
            except:
                pass

        if not records:
            return {"error": "No execution history"}

        total_cost = sum(r["ai_usage"]["cost_usd"] for r in records)
        total_tokens = sum(r["ai_usage"]["tokens_used"] for r in records)
        total_time = sum(r["ai_usage"]["time_seconds"] for r in records)
        local_count = sum(1 for r in records if r["ai_usage"]["hybrid_routing"] == "local")
        claude_count = sum(1 for r in records if r["ai_usage"]["hybrid_routing"] == "claude")

        return {
            "total_runs": len(records),
            "total_cost": round(total_cost, 4),
            "total_tokens": total_tokens,
            "total_time": round(total_time, 2),
            "local_runs": local_count,
            "claude_runs": claude_count,
            "avg_cost_per_run": round(total_cost / len(records), 6) if records else 0
        }
