from isaaclab.utils import configclass

from DX1_RLPackage.DX1_RLSetup.tasks.velocity.velocity_env_cfg import LocomotionVelocityRoughEnvCfg

from DX1_RLPackage.DX1_RLSetup.modelCfg.DX1 import DX1_CFG


@configclass
class DX1_RoughEnvCfg(LocomotionVelocityRoughEnvCfg):
    def __post_init__(self):
        # post init of parent
        super().__post_init__()

        self.scene.robot = DX1_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot")

        # In here redefine/overwrite some of the parameters set in velocity_env_cfg.py to customise for your robot
        self.scene.height_scanner.prim_path = "{ENV_REGEX_NS}/Robot/base_link"
        self.events.add_base_mass.params["asset_cfg"].body_names = "base_link"
        self.events.base_external_force_torque.params["asset_cfg"].body_names = "base_link"

        self.terminations.base_contact.params["sensor_cfg"].body_names = "base_link"

        # air_time should be for foot end effector, undesired_contact is for everything else
        self.rewards.feet_air_time.params["sensor_cfg"].body_names = ["FL_foot", "FR_foot", "BL_foot", "BR_foot"]
        self.rewards.undesired_contacts.params["sensor_cfg"].body_names = ["fl_2_1", "fr_2_1", "bl_2_1", "br_2_1", "fl_3_2", "fr_3_1", "bl_3_1", "br_3_1", "fl_1_1", "fr_1_1", "bl_1_1", "br_1_1"]
        # self.rewards.undesired_contacts.params["sensor_cfg"].body_names = ["fl_2_1", "fr_2_1", "bl_2_1", "br_2_1"]

        self.events.add_base_mass.params["mass_distribution_params"] = (-0.01, 0.01)


@configclass
class DX1_RoughEnvCfg_PLAY(DX1_RoughEnvCfg):
    def __post_init__(self):
        # post init of parent
        super().__post_init__()

        # make a smaller scene for play
        self.scene.num_envs = 50
        self.scene.env_spacing = 2.5
        # spawn the robot randomly in the grid (instead of their terrain levels)
        self.scene.terrain.max_init_terrain_level = None
        # reduce the number of terrains to save memory
        if self.scene.terrain.terrain_generator is not None:
            self.scene.terrain.terrain_generator.num_rows = 5
            self.scene.terrain.terrain_generator.num_cols = 5
            self.scene.terrain.terrain_generator.curriculum = False

        # disable randomization for play
        self.observations.policy.enable_corruption = False
        # remove random pushing event
        self.events.base_external_force_torque = None
        self.events.push_robot = None