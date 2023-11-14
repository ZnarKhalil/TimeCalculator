def add_time(start, duration, day=""):
    week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Extract hour, minute, am or pm from start
    start_time, am_or_pm = start.split(" ")
    start_hour, start_minute = map(int, start_time.split(":"))

    # Check duration and get hour and minute
    duration_hour, duration_minute = map(int, duration.split(":"))

    if am_or_pm == "PM":
        start_hour += 12

    total_minutes = start_minute + duration_minute
    total_hours = start_hour + duration_hour + total_minutes // 60

    final_am_or_pm = "AM" if total_hours%24 < 12 else "PM"
    final_hour_time = total_hours % 12 or 12
    final_minute_time = f"{total_minutes % 60:02}"

    number_of_extra_days = total_hours // 24

    if day:
        day = day.capitalize()
        new_index = (week_days.index(day) + number_of_extra_days) % 7
        day = f", {week_days[new_index]}"

    if number_of_extra_days == 1:
        number_of_extra_days = " (next day)"
    elif number_of_extra_days > 1:
        number_of_extra_days = f" ({number_of_extra_days} days later)"
    else:
        number_of_extra_days = ""

    new_time = f"{final_hour_time}:{final_minute_time} {final_am_or_pm}{day}{number_of_extra_days}"
    return new_time