from dataclasses import dataclass
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError


@dataclass
class UserConfig:
    name: str
    gender: str
    timezone: str = "UTC"

    def __post_init__(self):
        try:
            ZoneInfo(self.timezone)
        except ZoneInfoNotFoundError:
            raise ValueError(
                f"Invalid timezone: {self.timezone}"
            )


@dataclass
class RobotConfig:
    name: str
    identity: str
    user: UserConfig