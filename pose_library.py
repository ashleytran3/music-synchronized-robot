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

    "front_box_1": np.array([
        1.57, -0.5,  1.8,  1,  -1.5,  2.094,  0.0,             # right arm
        -1.702, 1.047,  -1.8,  0.0,  -1,    1.57,  0.0,             # left arm  
        -1.0, -1.0       
    ]),

    "front_box_2": np.array([
        1.702,  1.047,  1.8,  0.0,   0.0,  1.57,  0.0,   # right arm
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

    "point_left": np.array([
        -0.52, 0.0,  0.0,  0.0,  0.0,  0.0,  0.0,            
        -0.52, 0.0,  -1.57,  1.83,  0.0,  0.0,  0,             
        0.0, 0.0
    ]),

    "point_right": np.array([
        0.52, 0.0,  1.57,  1.83,  0.0,  0.0,  0.0,            
        0.52, 0.0,  0.0, 0.0,  0.0,  0.0,  0,             
        0.0, 0.0  
    ]),

    "point_right_wrists_down": np.array([
        0.52, 0.0,  1.57,  1.83,  1.57,  -1.57,  0.0,            
        0.52, 0.0,  0.0, 0.0,  0.0,  1.57,  0.0,             
        0.0, 0.0  
    ]),

    "point_left_wrists_down": np.array([
        -0.52, 0.0,  0.0,  0.0,  0.0,  1.57,  0.0,            
        -0.52, 0.0,  -1.57, 1.83,  1.57,  1.57,  0.0,             
        0.0, 0.0   
    ]),

    "shoulder_triangles": np.array([
        #s0,    s1,   e0,   e1,   w0,   w1,  w2
        -0.52, 0.0,  -3.14,  2.04,  0.0,  2.04,  1.57,            
         0.52, 0.0,  3.14, 2.04,  0.0,  2.04,  1.57,             
        0.0, 0.0   
    ]),

    "shoulder_triangle_left": np.array([
        -0.52, 0.0,  -3.14,  2.04,  0.0,  2.04,  1.57,            
         0.52, 0.0,  0.0, 0.0,  0.0,  1.57,  0.0,             
        0.0, 0.0  
    ]),

    "shoulder_triangle_right": np.array([
        -0.52, 0.0,  0.0,  0.0,  0.0,  1.57,  0.0,             
        -0.52, 0.0,  -3.14,  2.04,  0.0,  2.04,  1.57,             
        0.0, 0.0  
    ]),

    "diagonal": np.array([
         0.52, 0.0,  1.83,  1.83,  1.57,  1.57,  0.0,       
        -0.52, 0.0,  -1.31, 1.83,  1.83,  1.57,  0.0,             
        0.0, 0.0  
    ]),

    "diagonal_untangle_1": np.array([
        0.52, 0.0,  1.83,  1.83,  1.57,  0.05,  0.0,       
        -0.52, 0.0,  -1.31, 1.83,  1.83,  0.05,  0.0,             
        0.0, 0.0   
    ]),

    "diagonal_untangle_2": np.array([
        0.52, 0.0,  3.054,  1.83,  1.57,  0.05,  0.0,      
        -0.52, 0.0,  0, 1.83,  1.83,  0.05,  0.0,             
        0.0, 0.0  
    ]),

    "diagonal_untangle_3": np.array([
        0.52, 0.0,  0,  1.6,  1.57,  0.05,  0.0,      
        -0.52, 0.0,  3.054, 1.83,  1.83,  0.05,  0.0,             
        0.0, 0.0   
    ]),

    "straight": np.array([
        0.8, 0.0,  0.0,  0,  1,  0.0,  0.0,             # right arm
        -0.8, 0.0,  0.0,  0,  -1,  0.0,  0.0,             # left arm
         -1.0, -1.0 
    ]),

}

# 10 beats covering the first 5 seconds
SEQUENCE = [
    "tut1",                     # beat 1
    "shrug",                    # beat 2
    "wrists_bent1",             # beat 3
    "arms_wide",                # beat 4
    "tut1",                     # beat 5
    "wrists_bent_up",           # beat 6
    "neutral",                  # beat 7
    "wrists_bent2",             # beat 8
    "wrists_bent1",             # beat 9
    "arms_wide",                # beat 10
    "shrug",                    # beat 11
    "arms_wide",                # beat 12
    "tut1",                     # beat 13
    "wrists_bent1",             # beat 14
    "wrists_bent2",             # beat 15
    "arms_wide",                # beat 16
    "line_1",                   # beat 17
    "spider_1",                 # beat 18
    "line_2",                   # beat 19
    "spider_2",                 # beat 20
    "line_1",                   # beat 21
    "spider_1",                 # beat 22
    "line_2",                   # beat 23
    "spider_2",                 # beat 24
    "arms_wide",                # beat 25
    "clap",                     # beat 26
    "arms_wide",                # beat 27
    "clap",                     # beat 28
    "arms_wide",                # beat 29
    "clap",                     # beat 30
    "point_left",               # beat 31
    "point_right",              # beat 32
    "front_box_1",              # beat 33
    "arms_wide",                # beat 34
    "front_box_2",              # beat 35
    "arms_wide",                # beat 36
    "clap",                     # beat 37
    "point_left_wrists_down",   # beat 38
    "point_right_wrists_down",  # beat 39
    "neutral",                  # beat 40
    "shoulder_triangles",       # beat 41
    "shoulder_triangle_left",   # beat 42
    "shoulder_triangle_right",  # beat 43
    "arms_wide",                # beat 44
    "diagonal",                 # beat 45
    "diagonal_untangle_1",      # beat 46
    "diagonal_untangle_2",      # beat 47
    "arms_wide",                # beat 48
]


def get_pose(name):
    if name not in POSES:
        raise ValueError(f"Unknown pose '{name}'. Available: {list(POSES.keys())}")
    return POSES[name].copy()