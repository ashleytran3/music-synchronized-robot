import numpy as np

class PID:
    def __init__(self, kp, ki, kd, target):
        # Initialize gains and setpoint
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.target = target
        self.curr_pos = None
        self.last_err = np.zeros_like(target)
        self.acc_err = np.zeros_like(target)
        
    def reset(self, target=None):
        # Reset internal error history
        self.target = target
        self.last_err = np.zeros_like(target)
        self.acc_err = np.zeros_like(target)
        
    def get_error(self):
        # Return magnitude of last error
        return self.target - self.curr_pos

    def update(self, current_pos, dt):
        # Compute and return control signal
        self.curr_pos = current_pos
        curr_err = self.get_error()
        self.acc_err += curr_err * dt
        control = (self.kp * curr_err) + (self.ki * self.acc_err) + (self.kd * (curr_err - self.last_err) / dt)
        self.last_err = curr_err
        return control