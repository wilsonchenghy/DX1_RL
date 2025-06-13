import isaaclab.sim as sim_utils
from isaaclab.actuators import ActuatorNetMLPCfg, DCMotorCfg, ImplicitActuatorCfg
from isaaclab.assets.articulation import ArticulationCfg
import os
from math import pi

DX1_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path="/home/hy/Downloads/DX1_RL/ModelAssets4/DX1.usd",
        activate_contact_sensors=True,
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            rigid_body_enabled=True,
            disable_gravity=False,
            retain_accelerations=False,
            linear_damping=0.0,
            angular_damping=0.0,
            max_linear_velocity=1000.0,
            max_angular_velocity=1000.0,
            max_depenetration_velocity=1.0,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=False,
            solver_position_iteration_count=4,
            solver_velocity_iteration_count=0
        ),
    ),
    init_state = ArticulationCfg.InitialStateCfg(
        joint_pos={
            "Revolute_2": 0.0,
            "Revolute_3": 0.0,
            "Revolute_4": 0.0,
            "Revolute_5": 0.0,
            "Revolute_6": 0.0,
            "Revolute_7": 0.0,
            "Revolute_8": 0.0,
            "Revolute_9": 0.0,
            "Revolute_10": 0.0,
            "Revolute_11": 0.0,
            "Revolute_12": 0.0,
            "Revolute_13": 0.0,
        },
    ),
    soft_joint_pos_limit_factor=0.9,
    actuators={
        "base_legs": DCMotorCfg(
            joint_names_expr=[".*"],
            # joint_names_expr=[""],
            effort_limit=45, # 33.5
            saturation_effort=45,  # 33.5
            velocity_limit=21.0,
            stiffness=60, # 25.0
            damping=1.5, # 0.5
            friction=0.0,
        ),
    },
)