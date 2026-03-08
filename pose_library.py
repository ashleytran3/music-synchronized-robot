import numpy as np

# np.array([s0,   s1,   e0,   e1,   w0,   w1,   w2])
# s0 -> shoulder in/out
# s1 -> shoulder up/down

POSES = {
    # Arms relaxed at sides
    "neutral": np.array([
         0.0, -0.55,  0.0,  0.5,  0.0,  0.0,  0.0,   # left arm
         0.0, -0.55,  0.0,  0.5,  0.0,  0.0,  0.0,   # right arm
    ]),

    # Arms stretched out to sides
    "arms_wide": np.array([
        -1.2, -0.1,  0.0,  0.5,  0.0,  0.0,  0.0,   # left arm
         1.2, -0.1,  0.0,  0.5,  0.0,  0.0,  0.0,   # right arm
    ]),
}

# 10 beats covering the first 5 seconds
SEQUENCE = [
    "neutral",      # beat 1
    "arms_wide",    # beat 2
    "neutral",      # beat 3
    "arms_wide",    # beat 4
    "neutral",      # beat 5
    "arms_wide",    # beat 6
    "neutral",      # beat 7
    "arms_wide",    # beat 8
    "neutral",      # beat 9
    "arms_wide",    # beat 10
]


def get_pose(name):
    if name not in POSES:
        raise ValueError(f"Unknown pose '{name}'. Available: {list(POSES.keys())}")
    return POSES[name].copy()