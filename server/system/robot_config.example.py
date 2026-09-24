from .config import RobotConfig, UserConfig


ROBOT_CONFIG = RobotConfig(
    name="Your Robot Name",
    identity="""
Describe the robot's personality and character using {ROBOT_NAME} and {USER_NAME}.
""",
    user=UserConfig(
        name="Your name",
        gender="female or male",
        timezone="Your/Timezone",
    ),
)