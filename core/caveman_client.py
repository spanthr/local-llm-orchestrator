"""Caveman token compression client"""

import re
from typing import Tuple


class CavemanFormatter:
    """Compress responses to reduce token usage"""

    def __init__(self, level: str = "full"):
        self.level = level  # lite, full, ultra, wenyan
        self.levels = {
            "lite": 0.3,      # 30% compression
            "full": 0.65,     # 65% compression
            "ultra": 0.8,     # 80% compression
            "wenyan": 0.65    # 65% (classical Chinese style)
        }

    def compress(self, text: str, level: str = None) -> str:
        """Compress text to reduce tokens"""
        level = level or self.level

        if level == "lite":
            return self._compress_lite(text)
        elif level == "full":
            return self._compress_full(text)
        elif level == "ultra":
            return self._compress_ultra(text)
        elif level == "wenyan":
            return self._compress_wenyan(text)
        else:
            return text

    def _compress_lite(self, text: str) -> str:
        """Light compression (~30%)"""
        lines = text.split("\n")
        compressed = []

        for line in lines:
            line = line.strip()
            if not line:
                continue

            # Remove redundant words
            line = re.sub(r"\b(very|really|actually|basically|essentially)\b", "", line, flags=re.I)
            line = re.sub(r"\s+", " ", line).strip()

            if line:
                compressed.append(line)

        return "\n".join(compressed)

    def _compress_full(self, text: str) -> str:
        """Full compression (~65%)"""
        text = self._compress_lite(text)

        # Remove explanations
        lines = text.split("\n")
        result = []

        for line in lines:
            # Keep lines that are useful
            if any(x in line.lower() for x in [":", "→", "-", "•", "✓"]):
                result.append(line)
            elif len(line) < 100:
                result.append(line)

        return "\n".join(result)

    def _compress_ultra(self, text: str) -> str:
        """Ultra compression (~80%)"""
        text = self._compress_full(text)

        # Keep only critical info
        lines = [l for l in text.split("\n") if l.strip()]

        # Remove more than 2 consecutive lines
        result = []
        empty_count = 0
        for line in lines:
            if not line.strip():
                empty_count += 1
                if empty_count <= 1:
                    result.append(line)
            else:
                empty_count = 0
                result.append(line)

        return "\n".join(result[:len(result) // 2])  # Keep only first half

    def _compress_wenyan(self, text: str) -> str:
        """Classical Chinese style compression"""
        # Simplified classical Chinese tone (mostly removes grammar)
        text = text.replace("You should", "宜")
        text = text.replace("If you want", "若欲")
        text = text.replace("The way to", "其法")
        text = text.replace("must", "必")
        text = text.replace("can", "可")

        return self._compress_full(text)

    def get_token_savings(self, original: str, compressed: str) -> Tuple[int, float]:
        """Calculate token savings"""
        original_tokens = len(original) // 4
        compressed_tokens = len(compressed) // 4
        saved = original_tokens - compressed_tokens
        percentage = (saved / original_tokens * 100) if original_tokens > 0 else 0

        return saved, percentage

    def estimate_cost_reduction(
        self,
        tokens: int,
        model: str = "claude-sonnet-4-6",
        level: str = None
    ) -> float:
        """Estimate cost reduction"""
        level = level or self.level
        compression_rate = self.levels.get(level, 0.65)

        # Pricing (output tokens)
        pricing = {
            "claude-opus-4-8": 0.045,
            "claude-sonnet-4-6": 0.015,
            "claude-haiku-4-5": 0.0004,
        }

        price_per_token = pricing.get(model, 0.015) / 1_000_000
        original_cost = tokens * price_per_token
        compressed_tokens = tokens * (1 - compression_rate)
        compressed_cost = compressed_tokens * price_per_token

        return round(original_cost - compressed_cost, 4)
