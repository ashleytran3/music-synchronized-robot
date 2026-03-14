import numpy as np
from robosuite.environments.manipulation.manipulation_env import ManipulationEnv
from robosuite.models.arenas import EmptyArena
from robosuite.models.tasks import ManipulationTask


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
        mujoco_arena.set_origin([1, 0, -0.8])

        self.model = ManipulationTask(
            mujoco_arena=mujoco_arena,
            mujoco_robots=[robot.robot_model for robot in self.robots],
        )

    def _setup_references(self):
        super()._setup_references()

    def _setup_observables(self):
        observables = super()._setup_observables()
        return observables

    def _reset_internal(self):
        super()._reset_internal()

    def reward(self, action=None):
        return 0.0

    def _check_success(self):
        return False