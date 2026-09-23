from dataclasses import dataclass


@dataclass
class RobotConfig:
    robot_name: str
    user_name: str
    user_gender: str
    identity: str