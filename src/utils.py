"""Utility helpers for the ML prerequisites and algorithms notebooks.

Author: Tohidul Islam Tareq
"""

import random
import numpy as np


def set_seed(seed: int = 42) -> None:
    """Set random seeds for reproducible examples."""
    random.seed(seed)
    np.random.seed(seed)
