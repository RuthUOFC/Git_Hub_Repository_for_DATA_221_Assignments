def convert_total_time(Total_seconds):
    if Total_seconds < 0 or Total_seconds >= 86400:
        return "INVALID INPUT: seconds can only be between 0 and 86399."
    hours_24 = Total_seconds//3600
    minutes = (Total_seconds % 3600) // 60
    seconds = Total_seconds % 60

    Time_period = "AM" if hours_24 < 12 else "PM"
    # convert 24 hour format to 12 hour format
    hours_12 = hours_24 % 12
    if hours_12 == 0:
        hours_12 == 12

    return f"{hours_12} {minutes} {seconds} {Time_period}"


print(convert_total_time(9999))