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
        -0.52, 0.0,  0.0,  0.0,  0.0,  1.57,  0.0,             # left up, right down (wrt to robot)
        0.52, 0.0,  0.0,  0.0,  0.0,  -1.57,  0.0,             
        -1.0, -1.0                           
    ]),

    "wrists_bent2": np.array([
        -0.52, 0.0,  0.0,  0.0,  0.0,  -1.57,  0.0,           # left down, right up (wrt to viewer) 
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

    # table in the way
    "front_box_1": np.array([
        1.57, -0.5,  1.8,  1,  -1.5,  2.094,  0.0,             # right arm
        -1.702, 1.047,  0.0,  0.0,  -1,    1.57,  0.0,             # left arm  
        -1.0, -1.0     
    ]),

    "front_box_2": np.array([
        1.702,  1.047,  0.0,  0.0,   1.0,  1.57,  0.0,   # right arm
        -1.57, -0.5, -1.8,  1.0,   1.5,  2.094, 0.0,   # left arm
        -1.0, -1.0         
    ]),

    "arms_front": np.array([
        0.52, 0.0,  0.0,  0.0,  0.0,  0.0,  0.0,            # right arm
        -0.52, 0.0,  0.0,  0.0,  0.0,  0.0,  0.0,            # left arm  
        -1.0, -1.0     
    ]),

    "clap": np.array([
        1.1, 0.0,  0.0,  0.0,  2.0,  0.8,  0.0,             # right arm
        -1.1, 0.0,  0.0,  0.0,  -2.0,  0.8,  0.0,             # left arm
        1.0, 1.0    
    ]),

    "line_1": np.array([
        0.52, 0.0,  0.0,  0.0,  0.0,  0.0,  0.0,            # right arm
        1.7, 0.0,  0.0,  0.0,  0.0,  0.0,  0.0,            # left arm  
        -1.0, -1.0   
    ]),

    "line_2": np.array([
        -1.7, 0,  0.0,  0.0,  0.0,  0,  0.0,
        -0.52, 0, 0, 0, 0, 0, 0,
        -1.0, -1.0     
    ]),

    "spider_1": np.array([
        0.52, -1.0,  0.0,  2.0,  0.0,  -1.5,  0.0,            # right arm
        1.7, -1.0,  0.0,  2.0,  0.0,  -1.5,  0.0,            # left arm  
        -1.0, -1.0  
    ]),

    "spider_2": np.array([
        -1.7, -1.0,  0.0,  2.0,  0.0,  -1.5,  0.0,            # right arm
        -0.52, -1.0, 0, 2.0, 0, -1.5, 0,
        -1.0, -1.0  
    ]),
}

# 10 beats covering the first 5 seconds
SEQUENCE = [
    "tut1",             # beat 1
    "shrug",            # beat 2
    "wrists_bent1",     # beat 3
    "arms_wide",        # beat 4
    "tut1",             # beat 5
    "wrists_bent_up",   # beat 6
    "neutral",          # beat 7
    "wrists_bent2",     # beat 8
    "wrists_bent1",     # beat 9
    "arms_wide",        # beat 10
    "shrug",            # beat 11
    "arms_wide",        # beat 12
    "tut1",             # beat 13
    "wrists_bent1",     # beat 14
    "wrists_bent2",     # beat 15
    "arms_wide",        # beat 16
    "line_1",           # beat 17
    "spider_1",         # beat 18
    "line_2",           # beat 19
    "spider_2",         # beat 20
    "line_1",           # beat 21
    "spider_1",         # beat 22
    "line_2",           # beat 23
    "spider_2",         # beat 24
    "arms_front",       # beat 25
    "clap",             # beat 26
    "arms_front",       # beat 27
    "clap",             # beat 28
    "arms_front",       # beat 29
    "clap",             # beat 30
    "arms_front",       # beat 31
    "clap",             # beat 32
    "front_box_1",      # beat 33
    "arms_wide",        # beat 34
    "front_box_2",      # beat 35
    "arms_wide",        # beat 36

]


def get_pose(name):
    if name not in POSES:
        raise ValueError(f"Unknown pose '{name}'. Available: {list(POSES.keys())}")
    return POSES[name].copy()