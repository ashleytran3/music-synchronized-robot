import json
import robosuite as suite


def make_env():
    with open("baxter_joint_pos.json") as f:
        controller_config = json.load(f)

    env = suite.make(
        env_name="Lift",
        robots="Baxter",
        gripper_types="Robotiq85Gripper",
        has_renderer=True,
        has_offscreen_renderer=False,
        use_camera_obs=False,
        control_freq=20,
        ignore_done=True,
        controller_configs=controller_config,
    )
    return env