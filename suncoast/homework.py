# Read the number of test cases
num_cases = int(input().strip())

# Process each test case
for _ in range(num_cases):
    # Read lists a, b, and c, and convert them to sets to remove duplicates
    a = set(map(int, input().strip().split()))
    b = set(map(int, input().strip().split()))
    c = set(map(int, input().strip().split()))

    # Check if any list is empty
    if not a or not b or not c:
        print(0)  # No combinations possible if any list is empty
    else:
        # Calculate the number of unique combinations
        num_combinations = len(a) * len(b) * len(c)
        print(num_combinations)
