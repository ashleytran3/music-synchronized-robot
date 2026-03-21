import xml.etree.ElementTree as ET
import numpy as np
from robosuite.environments.manipulation.manipulation_env import ManipulationEnv
from robosuite.models.arenas import EmptyArena
from robosuite.models.tasks import ManipulationTask


# custom environment without table
class DanceEnv(ManipulationEnv):
    def __init__(self, **kwargs):
        kwargs.pop("table_full_size", None)
        kwargs.pop("table_friction", None)
        kwargs.pop("use_object_obs", None)
        kwargs.pop("reward_scale", None)
        kwargs.pop("reward_shaping", None)
        kwargs.pop("placement_initializer", None)
        super().__init__(**kwargs)

    def _load_model(self):
        super()._load_model()

        mujoco_arena = EmptyArena()
        mujoco_arena.set_origin([1.2, 0, -0.8])

        asset    = mujoco_arena.asset
        worldbody = mujoco_arena.worldbody

        for texture in asset.findall("texture"):
            if texture.get("type") == "skybox":
                texture.set("rgb1", "0.05 0.05 0.1")
                texture.set("rgb2", "0.0 0.0 0.05")

        for material in asset.findall("material"):
            if material.get("name") == "floorplane":
                material.set("rgba", "0.1 0.1 0.1 1")
            if material.get("name") == "walls_mat":
                material.set("rgba", "0.05 0.05 0.05 1")

        for light in worldbody.findall("light"):
            worldbody.remove(light)

        ET.SubElement(worldbody, "light", {
            "pos": "0 0 2.5",
            "dir": "0 0 -1",
            "specular": "0.8 0.2 0.8",
            "diffuse": "0.8 0.2 0.8",
            "directional": "true",
            "castshadow": "false",
        })
        ET.SubElement(worldbody, "light", {
            "pos": "1 1 2.5",
            "dir": "-0.2 -0.2 -1",
            "specular": "0.2 0.8 0.8",
            "diffuse": "0.2 0.8 0.8",
            "directional": "true",
            "castshadow": "false",
        })
        ET.SubElement(worldbody, "light", {
            "pos": "-1 -1 2.5",
            "dir": "0.2 0.2 -1",
            "specular": "0.8 0.8 0.2",
            "diffuse": "0.8 0.8 0.2",
            "directional": "true",
            "castshadow": "false",
        })

        self.model = ManipulationTask(
            mujoco_arena=mujoco_arena,
            mujoco_robots=[robot.robot_model for robot in self.robots],
        )

    def _setup_references(self):
        super()._setup_references()

    def _setup_observables(self):
        return super()._setup_observables()

    def _reset_internal(self):
        super()._reset_internal()

    def reward(self, action=None):
        return 0.0

    def _check_success(self):
        return False