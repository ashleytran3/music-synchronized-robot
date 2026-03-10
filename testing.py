from pid import PID
from env_setup import make_env
import numpy as np

def run():
    env = make_env()
    obs = env.reset()

    
    current_action = np.array([
        #s0,    s1,   e0,   e1,   w0,   w1,  w2
        -0.52, 0.52,  0.0,  0.78,  0.0,  -1.4,  0.0,            
        0.52, 0.52,  0.0,  0.78,  0.0,  -1.4,  0.0,             
        0.0, 0.0                           
    ])

    for _ in range(800):
        obs, _, _, _ = env.step(current_action)
        env.render()
    env.close()

if __name__ == "__main__":
    run()