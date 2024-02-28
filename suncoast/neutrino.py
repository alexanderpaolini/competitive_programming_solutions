# Read the number of test cases
num_tests = int(input().strip())

# Process each test case
for _ in range(num_tests):
    test_case = input().strip()

    # Find the initial position of 'N'
    n_position = test_case.index('N')

    # Count the number of hashtags on each side of 'N'
    left_count = test_case[:n_position].count('#')
    right_count = test_case[n_position + 1:].count('#')

    # Calculate the number of bounces
    if right_count >= left_count:
        bounces = 2 * left_count
    else:
        bounces = 2 * right_count + 1

    print(bounces)
