import datetime

def calculate_shift_duration(start, end):
    # Split the start time into hour, minute, and AM/PM parts
    start_parts = start.split(":")
    if len(start_parts) != 3:
        print("Invalid start time format")
        exit()
    else:
        start_hour, start_minute, start_ampm = start_parts
    
    # Split the end time into hour, minute, and AM/PM parts
    end_parts = end.split(":")
    if len(end_parts) != 3:
        print("Invalid end time format")
        exit()
    else:
        end_hour, end_minute, end_ampm = end_parts

    # Convert the hour and minute parts to integers
    start_hour = int(start_hour)
    start_minute = int(start_minute)
    end_hour = int(end_hour)
    end_minute = int(end_minute)
    
    # Convert the 12-hour time to 24-hour time
    if start_ampm == "PM" and start_hour != 12:
        start_hour += 12
    if start_ampm == "AM" and start_hour == 12:
        start_hour = 0
    if end_ampm == "PM" and end_hour != 12:
        end_hour += 12
    if end_ampm == "AM" and end_hour == 12:
        end_hour = 0

    # Create datetime objects for the start and end times
    start_time = datetime.datetime(1900, 1, 1, start_hour, start_minute)
    end_time = datetime.datetime(1900, 1, 1, end_hour, end_minute)

    # Calculate the duration of the shift
    duration = end_time - start_time

    # Extract the number of hours and minutes from the duration
    hours, remainder = divmod(int(duration.total_seconds() / 60), 60)
    minutes = remainder

    # Return the duration of the shift in hours and minutes
    return f"{hours} hours and {minutes} minutes"

start = input("Enter the start time of the shift (HH:MM:AM/PM): ")
end = input("Enter the end time of the shift (HH:MM:AM/PM): ")

print(start.split(":"))
print(end.split(":"))

result = calculate_shift_duration(start, end)

print(result)
