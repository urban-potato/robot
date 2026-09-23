from .config import RobotConfig


ROBOT_CONFIG = RobotConfig(
    robot_name="Your Robot Name",
    user_name="Your Name",
    user_gender="female/male",
    identity="""
Describe the robot's personality and character using {ROBOT_NAME} and {USER_NAME}.
""",
)