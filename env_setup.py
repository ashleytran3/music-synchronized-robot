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

    return env


if __name__ == "__main__":
    env = make_env()
    # obs = env.reset()
    # print("Action dim:", env.action_dim)
    # print("Observation keys:", list(obs.keys()))
    # env.close()

    env.reset()
    print("Action dim:", env.action_dim)
    print("Low: ", env.action_spec[0])
    print("High:", env.action_spec[1])

    robot = env.robots[0]
    print("\nRobot type:", type(robot))
    print("Robot arms:", robot.arms)
    print("Robot gripper:", robot.gripper)
    print("Gripper type:", type(robot.gripper))
    print("Gripper dir:", [x for x in dir(robot.gripper) if not x.startswith("_")])
    env.close()