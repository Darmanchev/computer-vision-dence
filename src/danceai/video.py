import math
from collections.abc import Iterator
from pathlib import Path

import cv2
import numpy as np

def read_frames(video_path: str | Path) -> Iterator[tuple[int, np.ndarray]]:
    """Yield (timestamp_ms, BGR frame) for constant-frame-rate video.
    """