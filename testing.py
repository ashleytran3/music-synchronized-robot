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

    
    current_action = np.array([
        1.702,  1.047,  0.0,  0.0,   1.0,  1.57,  0.0,   # right arm
        -1.57, -0.5, -1.8,  1.0,   1.5,  2.094, 0.0,   # left arm
        -1.0, -1.0                               #grippers open                     
    ])

    while True:
        obs, _, _, _ = env.step(current_action)
        env.render()
    env.close()

if __name__ == "__main__":
    run()