from pid import PID
from env_setup import make_env
import numpy as np

# limits
# s0: -1.702 to  1.702
# s1: -2.147 to  1.047
# e0: -3.054 to  3.054
# e1: -0.050 to  2.618
# w0: -3.059 to  3.059
# w1: -1.571 to  2.094
# w2: -3.059 to  3.059

def run():
    env = make_env()
    obs = env.reset()


    # default arms stretched to side
    # -0.52, 0.0,  0.0,  0.0,  0.0,  0.0,  0.0,             # right arm
    # 0.52, 0.0,  0.0,  0.0,  0.0,  0.0,  0.0,             # left arm
    # -1.0, -1.0   
    
    current_action = np.array([
        #s0,    s1,   e0,   e1,   w0,   w1,  w2
        0.52, 0.0,  1.83,  1.83,  1.57,  0.1,  0.0,       
        -0.52, 0.0,  -1.31, 1.83,  1.83,  0.2,  0.0,             
        0.0, 0.0                       
    ])

    while True:
        obs, _, _, _ = env.step(current_action)
        env.render()
    env.close()

if __name__ == "__main__":
    run()