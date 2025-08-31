__all__ = ("seconds_to_str",)


def seconds_to_str(seconds: int) -> str:
    """Реализует текстовое представление времени.

    Example:
        >> seconds_to_str(20)
        20s
        >> seconds_to_str(60)
        01m00s
        >> seconds_to_str(65)
        01m05s
        >> seconds_to_str(3700)
        01h01m40s
        >> seconds_to_str(93600)
        01d02h00m00s
    """
    result = ''
    time_seconds = seconds % 60
    time_minutes = seconds // 60 % 60
    time_hours = seconds // 3600 % 24
    time_days = seconds // (3600 * 24)
    if time_days:
        result += f'{time_days:02d}d{time_hours:02d}h{time_minutes:02d}m'
    elif time_hours:
        result += f'{time_hours:02d}h{time_minutes:02d}m'
    elif time_minutes:
        result += f'{time_minutes:02d}m'
    result += f'{time_seconds:02d}s'
    return result
