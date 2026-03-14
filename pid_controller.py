import numpy as np
from pid import PID

MAX_DELTA = 0.05


class DancePIDController:
    def __init__(self, kp=0.6, ki=0.0, kd=0.05):
        """
        Args:
            kp: Proportional gain
            ki: Integral gain
            kd: Derivative gain
        """
        neutral = np.zeros(7)
        self.pid_right = PID(kp=kp, ki=ki, kd=kd, target=neutral)
        self.pid_left  = PID(kp=kp, ki=ki, kd=kd, target=neutral)
        self.last_time = None

    def set_target(self, pose_16):
        self.pid_right.reset(target=pose_16[:7])
        self.pid_left.reset(target=pose_16[7:14])

    def update(self, obs, dt):
        current_joints = obs["robot0_joint_pos"]

        delta_right = self.pid_right.update(current_joints[:7],  dt=dt)
        delta_left  = self.pid_left.update(current_joints[7:14], dt=dt)

        delta_right = np.clip(delta_right, -MAX_DELTA, MAX_DELTA)
        delta_left  = np.clip(delta_left,  -MAX_DELTA, MAX_DELTA)

        action = np.concatenate([
            delta_right,
            delta_left,
            [-1.0, -1.0]   # grippers open
        ])

        return action