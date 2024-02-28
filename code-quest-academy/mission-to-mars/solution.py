# Wrong answer (not sure why)
num_cases = int(input())

def convert_seconds(total_seconds):
    SECONDS_PER_MINUTE = 60
    MINUTES_PER_HOUR = 60
    HOURS_PER_DAY = 24

    minutes, seconds = divmod(total_seconds, SECONDS_PER_MINUTE)
    hours, minutes = divmod(minutes, MINUTES_PER_HOUR)
    days, hours = divmod(hours, HOURS_PER_DAY)

    return (days, hours, minutes, seconds)

for _ in range(num_cases):
    # Distance in millions of miles
    # Speed in miles per hour
    distance, speed = map(float, input().split())

    # Now distance is in seconds
    distance = distance * 1e6

    # hours (so we multiply by 60 for minutes and 60 for seconds)
    time = (distance / speed) * 60 * 60

    # time in seconds so use convert seconds
    days, hours, minutes, seconds = map(round, convert_seconds(time))
    print(f"Time to Mars: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")
