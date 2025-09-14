"""Image and overlay operations used by UI components."""
from __future__ import annotations
from typing import Tuple
import numpy as np


def resize_nearest(data: np.ndarray, target_shape: Tuple[int, int]) -> np.ndarray:
    """Nearest-neighbor resize for 2D or HxWxC arrays."""
    height, width = target_shape
    if data.ndim == 2:
        out = np.zeros((height, width), dtype=data.dtype)
        for i in range(height):
            for j in range(width):
                si = int(i * data.shape[0] / height)
                sj = int(j * data.shape[1] / width)
                out[i, j] = data[si, sj]
        return out
    else:
        channels = data.shape[2]
        out = np.zeros((height, width, channels), dtype=data.dtype)
        for i in range(height):
            for j in range(width):
                si = int(i * data.shape[0] / height)
                sj = int(j * data.shape[1] / width)
                out[i, j] = data[si, sj]
        return out


def apply_color_mapping(data: np.ndarray, color_map: str) -> np.ndarray:
    """Very simple color mapping for demo frames (returns HxWx3)."""
    data = data.astype(np.float32)
    dmin, dmax = float(data.min()), float(data.max())
    norm = (data - dmin) / (dmax - dmin + 1e-8)

    if color_map == "hot":
        r = np.clip(norm * 3, 0, 1)
        g = np.clip((norm - 0.33) * 3, 0, 1)
        b = np.clip((norm - 0.67) * 3, 0, 1)
    elif color_map == "plasma":
        r = np.clip(norm * 2, 0, 1)
        g = np.clip((norm - 0.5) * 2, 0, 1)
        b = np.clip(1 - norm * 2, 0, 1)
    elif color_map == "viridis":
        r = np.clip(norm * 2, 0, 1)
        g = np.clip(norm, 0, 1)
        b = np.clip(1 - norm, 0, 1)
    else:
        r = g = b = norm

    return np.stack([r, g, b], axis=2)

