"""Utility functions shared across modules."""
from __future__ import annotations
import math
from typing import Dict


def cosine_similarity(a: Dict[str, float], b: Dict[str, float]) -> float:
    """Cosine similarity between two feature dicts (0..1)."""
    if not a or not b:
        return 0.0
    keys = set(a) & set(b)
    if not keys:
        return 0.0
    num = sum(a[k] * b[k] for k in keys)
    a_norm = math.sqrt(sum(a[k] ** 2 for k in keys))
    b_norm = math.sqrt(sum(b[k] ** 2 for k in keys))
    if a_norm == 0 or b_norm == 0:
        return 0.0
    return max(0.0, min(1.0, num / (a_norm * b_norm)))


def euclidean_similarity(a: Dict[str, float], b: Dict[str, float]) -> float:
    """Convert Euclidean distance into similarity (0..1)."""
    if not a or not b:
        return 0.0
    keys = set(a) & set(b)
    if not keys:
        return 0.0
    dist = math.sqrt(sum((a[k] - b[k]) ** 2 for k in keys))
    max_dist = math.sqrt(len(keys))
    sim = 1.0 - (dist / max_dist)
    return max(0.0, min(1.0, sim))

