from __future__ import annotations
import numpy as np

def mean_shift(ref: list[float], cur: list[float], threshold: float = 0.5) -> dict:
    delta = abs(float(np.mean(ref)) - float(np.mean(cur)))
    return {"drift": delta > threshold, "mean_shift": delta}
