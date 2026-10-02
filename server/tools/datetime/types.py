from typing import TypedDict


class DateTimeResult(TypedDict):
    datetime: str
    date: str
    time: str
    weekday: int
    day: int
    month: int
    year: int
    timezone: str
    utc_offset: str