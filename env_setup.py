import robosuite as suite


def make_env():
    env = suite.make(
        env_name="Lift",
        robots="Baxter",
        gripper_types="Robotiq85Gripper",
        has_renderer=True,
        has_offscreen_renderer=False,
        use_camera_obs=False,
        control_freq=20,
        ignore_done=True,
    )

    # Baxter action layout:
    #   [0:7]  = left arm joints  (s0, s1, e0, e1, w0, w1, w2)
    #   [7:14] = right arm joints (s0, s1, e0, e1, w0, w1, w2)
    #   [14]   = left gripper  (-1 = open, +1 = close)
    #   [15]   = right gripper (-1 = open, +1 = close)

    return env


if __name__ == "__main__":
    env = make_env()
    obs = env.reset()
    print("Action dim:", env.action_dim)
    print("Observation keys:", list(obs.keys()))
    env.close()