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
        -0.52, 0.0, -3.14, 2.04,  0.0,  2.04,  1.57,            
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

    "akimbo_1": np.array([
        -0.52, 0.5,  0.0,  2,  0.0,  0.0,  0.0,             # right arm
         0.52, 0.0,  0.0,  0.0,  0.0,  0.0,  0.0,             # left arm
         -1.0, -1.0  
    ]),

    "akimbo_2": np.array([
        -0.52, 0.5,  0.0,  2,  0.0,  0.0,  0.0,             # right arm
         0.52, 0.5,  0.0,  2,  0.0,  0.0,  0.0,             # left arm
         -1.0, -1.0  
    ]),

    "akimbo_3": np.array([
        -0.52, -0.4,  3,  2,  0.0,   -1.571,  0.0,             # right arm
         0.52, 0.5,  0.0,  2,  0.0,  0.0,  0.0,             # left arm
         -1.0, -1.0    
    ]),

    "akimbo_4": np.array([
        -0.52, -0.4,  3,  2,  0.0,   -1.571,  0.0,             # right arm
         0.52, -0.4,  3,  2,  0.0,   -1.571,  0.0,             # left arm
         -1.0, -1.0    
    ]),

     "elbows_left": np.array([
         -0.52, 0.0,  0.0,  1.57,  0.0,  -1.57,  0.0,            
        -0.52, 0.0,  -1.57,  1.83,  1.57,  1.57,  0,             
        0.0, 0.0  
    ]),

    "elbows_right": np.array([
         0.52, 0.0,  1.57,  1.83,  1.57,  -1.57,  0.0,            
        0.52, 0.0,  0.0, 1.57,  0.0,  -1.57,  0,             
        0.0, 0.0
    ]),

    "L1": np.array([
        -0.52, 0.0,  0.0,  0.0,  0.0,  0.0,  0.0,             # right arm
         0.52, -1.57,  0.0,  0.0,  0.0,  0.0,  0.0,             # left arm
         -1.0, -1.0
    ]),

    "L2": np.array([
        -0.52, -1.57,  0.0,  0.0,  0.0,  0.0,  0.0,             # right arm
         0.52, 0.0,  0.0,  0.0,  0.0,  0.0,  0.0,             # left arm
         -1.0, -1.0 
    ]),

    "move_1": np.array([
        -0.52, 0.8,  0.0,  1.57,  0.0,  -1.57,  0.0,   # right arm
        0.52, -0.8, 0.0,  1.57,  0.0,   1.57,  0.0,   # left arm
        -1.0, -1.0
    ]),

    "move_2": np.array([
        -0.52, -0.8,  0.0,  1.57,  0.0,  1.57,  0.0,   # right arm
        0.52,  0.8,  0.0,  1.57,  0.0, -1.57,  0.0,   # left arm
        -1.0, -1.0
    ]),

    "move_3": np.array([
        -0.3, 0.0,  1.57,  2.0,  0.0,  0.0,  0.0,     # right arm
        0.3, 0.0, -1.57,  2.0,  0.0,  0.0,  0.0,     # left arm
        -1.0, -1.0
    ]),

    "move_4": np.array([
        #s0,    s1,   e0,   e1,   w0,   w1,  w2
        -0.3, 0.0,  1.57,  2.0,  0.0,  0.0,  1,      # right arm
        0.3, 0.0, -1.57,  2.0,  0.0,  0.0, 1,      # left arm
        -1.0, -1.0
    ]),

    "move_5": np.array([
        -0.3, 0.0,  1.57,  1.0,  0.0,  0.0,  1,      # right arm
        0.3, 0.0, -1.57,  1.0,  0.0,  0.0, 1,      # left arm
        1.0, 1.0
    ]),

    "move_6": np.array([
        1.5, 0.0,  2,  2.6,  0.0,  0.0,  1,      # right arm
        -1.5, 0.0, -1,  2.6,  0.0,  0.0, 1,      # left arm
        1.0, 1.0
    ]),

    "move_7": np.array([
        -0.52, 0,  2,  2,  0.0,  1.5,  0.0,   # right
        0.52, 0, -2,  2,  0.0,  1.5,  0.0,   # left
        -1.0, -1.0
    ]),

    "move_8": np.array([
        -0.52, 0,  3,  2,  0.0,   1.5,  0.0,             # right arm
        0.52, 0, -3,  2,  0.0,  1.5,  0.0,             # left arm
         -1.0, -1.0  
    ]),

    "move_9": np.array([
        -0.52, 1,  3,  2,  0.0,   1.5,  0.0,             # right arm
        0.52, 0.7,  0.0,  0.0,  0.0,  -1,  0.0,             # left arm
         -1.0, -1.0  
    ]),

    "move_9_out": np.array([
        -0.52, 1,  3,  2,  0.0,   -0.6,  0.0,             # right arm
        0.52, 0.5,  0.0,  0.0,  0.0,  -1,  0.0,             # left arm
         -1.0, -1.0  
    ]),

    "move_10": np.array([
        1, 0.0,  2,  1,  0.0,  -1,  0.0,             # right arm
        -0.4, 0.0,  -1.5,  2,  0.0,  -1,  0.0,             # left arm
        -1.0, -1.0  
    ]),

    "move_11": np.array([
        -0.52, 0.0,  2,  1.6,  0.0,  0.0,  0.0,             # right arm
        0.52, 0.0,  -2,  1.6,  0.0,  0.0,  0.0,             # left arm
        -1.0, -1.0  
    ]),

    # halfbeat pose
    "arms_out_forward": np.array([
        .90, 0.0,  0.0,  -0.52,  -0.1,  0.0,  0.0,             # right arm
        -0.9, 0.0,  0.0, -0.52,  0.1,  0.0,  0.0,             # left arm
         -1.0, -1.0
    ]),

    "wave1": np.array([
        -0.52, 0.0,  0.0,  0.0,  0.0,  0.52,  0.0,             # right arm
         0.52, 0.0,  0.0,  0.0,  0.0,  0.0,  0.0,             # left arm
         -1.0, -1.0 
    ]),

    "wave2": np.array([
         -0.52, -0.2,  0.0,  0.6,  0.0,  -0.52,  0.0,             # right arm
         0.52, 0.0,  0.0,  0.0,  0.0,  0.0,  0.0,             # left arm
         -1.0, -1.0 
    ]),

    "wave3": np.array([
        -0.52, 0.0,  0.0,  0.0,  0.0,  0.0,  0.0,             # right arm
        0.52, -0.2,  0.0,  0.6,  0.0,  -0.52,  0.0,             # left arm
        -1.0, -1.0
    ]),

    "wave4": np.array([
        -0.52, 0.0,  0.0,  0.0,  0.0,  0.0,  0.0,             # right arm
         0.52, 0.0,  0.0,  0.0,  0.0,  0.52,  0.0,             # left arm
         -1.0, -1.0 
    ]),

    "arms_down": np.array([
        -0.52, 1.3,  0.0,  0.0,  0.0,  0.0,  0.0,             # right arm
        0.52, 1.3,  0.0,  0.0,  0.0,  0.0,  0.0,             # left arm
        -1.0, -1.0  
    ]),

    "elbow_push_1": np.array([
         -0.52, 1.3,  0.0,  0.0,  0.0,  0.0,  0.0,   # right
        0.52, 0, -1.5,  2,  0.0,  1.5,  0.0,   # left
        -1.0, -1.0
    ]),

    "elbow_push_2": np.array([
        -0.52, 0,  1.5,  2,  0.0,  1.5,  0.0,   # right
        0.52, 1.3, 0.0,  0.0,  0.0,  0.0,  0.0,   # left
        -1.0, -1.0
    ]),

    "S1": np.array([
         -0.52, 0.0,  3.14,  1.57,  0.0,  0.0,  0.0,             # right arm
        0.52, 0.0,  0.0,  1.57,  0.0,  0.0,  0.0,             # left arm
        -1.0, -1.0  
    ]),

    "S2": np.array([
         -0.52, 0.0,  0.0,  1.57,  0.0,  0.0,  0.0,             # right arm
        0.52, 0.0,  3.14,  1.57,  0.0,  0.0,  0.0,             # left arm
        -1.0, -1.0  
    ]),

    "point": np.array([
         -0.52, 0.5,  0.0,  2,  0.0,  0.0,  0.0,             # right arm
        -0.7, 0.0,  0.0, 0,  0.0,  0.0,  0.0,   
       -1.0, -1.0 
    ]),

    "point_up": np.array([
         -0.52, 0.5,  0.0,  2,  0.0,  0.0,  0.0,             # right arm
        0.52, -0.52,  1.57, 0,  0.0,  0.0,  0.0,   
       -1.0, -1.0 
    ]),

    "point_down": np.array([
         -0.52, 0.5,  0.0,  2,  0.0,  0.0,  0.0,             # right arm
        -0.7, 0.0,  -0.78,  1.57,  0.0,  0.0,  0.0, 
       -1.0, -1.0 
    ])
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
    "arms_wide",                  # beat 40
    "shoulder_triangles",       # beat 41
    "shoulder_triangle_left",   # beat 42
    "shoulder_triangle_right",  # beat 43
    "arms_wide",                # beat 44
    "diagonal",                 # beat 45
    "diagonal_untangle_1",      # beat 46
    "diagonal_untangle_2",      # beat 47
    "arms_wide",                # beat 48
    "akimbo_1",                 # beat 49
    "akimbo_2",                 # beat 50
    "akimbo_3",                 # beat 51
    "akimbo_4",                 # beat 52
    "elbows_left",              # beat 53
    "elbows_right",             # beat 54
    "L1",                       # beat 55
    "L2",                       # beat 56
    "move_1",                   # beat 57
    "move_2",                   # beat 58
    "move_3",                   # beat 59
    "move_4",                   # beat 60
    "move_5",                   # beat 61
    "move_6",                   # beat 62
    "move_7",                   # beat 63
    "move_8",                   # beat 64
    "move_9",                   # beat 65
    "move_9",                   # beat 66
    "move_9_out",               # beat 67
    "move_9",                   # beat 68
    "move_10",                  # beat 69
    "move_11",                  # beat 70
    "arms_wide",                # beat 71
    "move_11",                  # beat 72
    "move_9",                   # beat 73
    "move_9_out",               # beat 74
    "move_9",                   # beat 75
    "point_left_wrists_down",   # beat 76
    "point_right_wrists_down",  # beat 77
    "point_left_wrists_down",   # beat 78
    "point_right_wrists_down",  # beat 79
    "move_9",                   # beat 80
    "move_9",                   # beat 81
    "move_9_out",               # beat 82
    "move_9",                   # beat 83
    "akimbo_1",                 # beat 84
    "akimbo_2",                 # beat 85
    "akimbo_3",                 # beat 86
    "akimbo_4",                 # beat 87
    "move_9",                   # beat 88
    "move_9",                   # beat 89
    "move_9_out",               # beat 90
    "move_9",                   # beat 91
    "L1",                       # beat 92
    "L2",                       # beat 93
    "point_left",               # beat 94
    "point_right",              # beat 95
    "arms_wide",                # beat 96
    "wave1",                    # beat 97
    "wave2",                    # beat 98
    "wave3",                    # beat 99
    "arms_wide",                # beat 100
    "wave1",                    # beat 101
    "wave2",                    # beat 102
    "wave3",                    # beat 103
    "arms_wide",                # beat 104
    "wave1",                    # beat 105
    "wave2",                    # beat 106
    "wave3",                    # beat 107
    "arms_wide",                # beat 108
    "elbow_push_1",             # beat 109
    "elbow_push_2",             # beat 110
    "elbow_push_1",             # beat 111
    "elbow_push_2",             # beat 112
    "elbow_push_1",             # beat 113
    "elbow_push_2",             # beat 114
    "elbow_push_1",             # beat 115
    "elbow_push_2",             # beat 116
    "elbow_push_1",             # beat 117
    "elbow_push_2",             # beat 118
    "elbow_push_1",             # beat 119
    "elbow_push_2",             # beat 120
    "elbow_push_1",             # beat 121
    "elbow_push_2",             # beat 122
    "elbow_push_1",             # beat 123
    "elbow_push_2",             # beat 124
    "arms_wide",                # beat 125
    "point",                    # beat 126
    "point",                    # beat 127
    "point",                    # beat 128  
    "S1",                       # beat 129
    "S2",                       # beat 130
    "S1",                       # beat 131
    "S2",                       # beat 132
    "S1",                       # beat 133
    "S2",                       # beat 134
    "S1",                       # beat 135
    "S2",                       # beat 136
    "clap",                     # beat 137
    "point_left",               # beat 138
    "point_right",              # beat 139
    "point_left",               # beat 140
    "point_right",              # beat 141
    "point_left",               # beat 142
    "point_right",              # beat 143
    "point_left",               # beat 144
    "point_right",              # beat 145
    "point_up", 
    "point_down",
    "point_up",
    "point_down",
    "point_up",
    "point_down",
    "point_up",
    "point_down",
    "arms_wide",
    "clap",
    "arms_wide",
    "move_1",
    "move_2",
    "move_1",
    "move_2",
]

HALFBEAT_SEQUENCE = [
    "arms_out_forward"
]

def get_pose(name):
    if name not in POSES:
        raise ValueError(f"Unknown pose '{name}'. Available: {list(POSES.keys())}")
    return POSES[name].copy()