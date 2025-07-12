import numpy as np

def interpolate_angles(current, target, steps=10):
    return [list(np.linspace(c, t, steps)) for c, t in zip(current, target)]

def interpolate_frames(current, target, speed_deg_s=30.0, step_time=0.05):
    """Return a list of full‑pose frames so the move runs at `speed_deg_s`."""
    max_delta = max(abs(t - c) for c, t in zip(current, target))
    duration = max_delta / speed_deg_s            # seconds
    steps = max(2, int(duration / step_time))     # at least 2 frames
    frames = []
    for s in range(steps):
        alpha = s / (steps - 1)
        frame = [c + (t - c) * alpha for c, t in zip(current, target)]
        frames.append(frame)
    return frames, step_time
