import numpy as np

# np.array([s0,   s1,   e0,   e1,   w0,   w1,   w2])
# s0 -> shoulder in/out
# s1 -> shoulder up/down
# e0 -> upper arm twist
# e1 -> elbow bend
# w0 -> forearm twist
# w1 -> wrist up/down
# w2 -> wrist twist

POSES = {
    # Arms relaxed at sides
    "neutral": np.array([
        0, 0,  0.0,  0.0,  0.0,  0.0,  0.0,             # right arm
        0, 0,  0.0,  0.0,  0.0,  0.0,  0.0,             # left arm
        -1.0, -1.0                                      # grippers open
    ]),

    # Arms stretched out to sides
    "arms_wide": np.array([
        3, 0,  0.0,  0.0,  0.0,  0.0,  0.0,
        -3, 0,  0.0,  0.0,  0.0,  0.0,  0.0,
        -1.0, -1.0                                      # grippers open
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