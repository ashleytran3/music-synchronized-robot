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
    # Arms crossed
    "neutral": np.array([
        0, 0,  0.0,  0.0,  0.0,  0.0,  0.0,             # right arm
        0, 0,  0.0,  0.0,  0.0,  0.0,  0.0,             # left arm
        -1.0, -1.0                                      # grippers open
    ]),

    # Arms bent out to sides (T-pose)
    "arms_wide": np.array([
        -0.52, 0.0,  0.0,  0.0,  0.0,  0.0,  0.0,             # right arm
         0.52, 0.0,  0.0,  0.0,  0.0,  0.0,  0.0,             # left arm
         -1.0, -1.0                                           #grippers open
    ]),

    "tut1": np.array([
        -0.52, 0.0,  0.0,  1.57,  0.0,  1.57,  0.0,             # right arm
         0.52, 0.0,  0.0,  1.57,  0.0,  1.57,  0.0,             # left arm
         -1.0, -1.0                                             #grippers 
    ]),

    "wrists_bent1": np.array([
        -0.52, 0.0,  0.0,  0.0,  0.0,  1.57,  0.0,            
        0.52, 0.0,  0.0,  0.0,  0.0,  -1.57,  0.0,             
        -1.0, -1.0                           
    ]),

    "wrists_bent2": np.array([
        -0.52, 0.0,  0.0,  0.0,  0.0,  -1.57,  0.0,            
        0.52, 0.0,  0.0,  0.0,  0.0,  1.57,  0.0,             
        -1.0, -1.0                           
    ]),

    "wrists_bent_up": np.array([
        -0.52, 0.0,  0.0,  0.0,  0.0,  -1.57,  0.0,            
        0.52, 0.0,  0.0,  0.0,  0.0,  -1.57,  0.0,             
        -1.0, -1.0  
    ]),

    "wrists_bent_down": np.array([
        -0.52, 0.0,  0.0,  0.0,  0.0,  -1.57,  0.0,            
        0.52, 0.0,  0.0,  0.0,  0.0,  -1.57,  0.0,             
        -1.0, -1.0  
    ]),
    
    "shrug": np.array([
        -0.52, 0.52,  0.0,  0.78,  0.0,  -1.4,  0.0,            
        0.52, 0.52,  0.0,  0.78,  0.0,  -1.4,  0.0,             
        0.0, 0.0 
    ]),
}

# 10 beats covering the first 5 seconds
SEQUENCE = [
    "tut1",         # beat 1
    "shrug",    # beat 2
    "wrists_bent1",         # beat 3
    "arms_wide",    
    "tut1",         # beat 2
    "wrists_bent_up",
    "neutral",         # beat 2
    "wrists_bent2",
    "wrists_bent1",         # beat 2
    "arms_wide",
]


def get_pose(name):
    if name not in POSES:
        raise ValueError(f"Unknown pose '{name}'. Available: {list(POSES.keys())}")
    return POSES[name].copy()