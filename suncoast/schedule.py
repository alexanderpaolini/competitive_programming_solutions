# Read the number of test cases
num_cases = int(input().strip())

# Process each test case
for _ in range(num_cases):
    info = input().strip().split(" ")
    rooms_per_minute = int(info.pop())
    total_time = 0

    floor1, room1 = map(int, info[0].split('-'))
    floor2, room2 = map(int, info[1].split('-'))

    # Time to reach the floor from the previous floor
    time_to_floor = abs(floor2 - floor1)

    # Determine the nearest stairwell for the current room
    nearest_stairwell1 = min(room1, 100 - room1)
    nearest_stairwell2 = min(room2, 100 - room2)

    # Time to walk from the previous room to the current room
    hallway_distance = abs(
        room2 - room1) if floor1 == floor2 else nearest_stairwell1 + nearest_stairwell2
    time_to_room = hallway_distance / rooms_per_minute

    # Check if it's possible to visit both rooms within 7 minutes
    if total_time <= 7:
        print("Not even close!")
    else:
        print("Better late than never...")
