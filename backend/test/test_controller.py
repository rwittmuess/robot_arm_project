import numpy as np
from app.controller import interpolate_angles, interpolate_frames

def test_interpolation_endpoints():
    current = [0, 0, 0, 0, 0, 0]
    target  = [20, 20, 20, 20, 20, 20]
    frames  = interpolate_angles(current, target, steps=42)
    
    frames = np.array(frames).T  

    assert np.all(np.isclose(frames[0], [0, 0, 0, 0, 0, 0]))
    assert np.all(np.isclose(frames[-1], [20, 20, 20, 20, 20, 20]))


