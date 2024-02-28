# Read the number of test cases
num_cases = int(input().strip())

# Process each test case
for _ in range(num_cases):
    h, a = map(int, input().strip().split())
    assignments = list(map(int, input().strip().split()))
    
    # Sort assignments in ascending order of time taken
    assignments.sort()

    # Initialize count and total time
    count = 0
    total_time = 0

    # Go through each assignment
    for time in assignments:
        if total_time + time <= h:
            total_time += time
            count += 1
        else:
            break

    # Print the maximum number of assignments that can be completed
    print(count)
