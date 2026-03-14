import json
import robosuite as suite
from robosuite.environments.base import register_env
from custom_env import DanceEnv


def make_env():
    with open("baxter_joint_pos.json") as f:
        controller_config = json.load(f)

    # register custom environment
    register_env(DanceEnv)

    env = suite.make(
        env_name="DanceEnv",
        robots="Baxter",
        gripper_types="Robotiq85Gripper",
        has_renderer=True,
        has_offscreen_renderer=False,
        use_camera_obs=False,
        control_freq=50,
        ignore_done=True,
        controller_configs=controller_config,
    )
    return env