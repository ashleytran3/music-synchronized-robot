from pid import PID
from env_setup import make_env
import numpy as np
from pose_library import POSES
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
    
    # down -0.52, 1.3,  0.0,  0.0,  0.0,  0.0,  0.0,             # right arm

    # move_5 for chorus
    current_action = np.array([
         -0.52, 0.5,  0.0,  2,  0.0,  0.0,  0.0,             # right arm
        -0.7, 0.0,  -0.78,  1.57,  0.0,  0.0,  0.0, 
       -1.0, -1.0 
    ])
    print(obs["robot0_joint_pos"].shape)
    while True:
        obs, _, _, _ = env.step(current_action)
        env.render()
    env.close()

if __name__ == "__main__":
    run()