num_cases = int(input())

for _ in range(num_cases):
    s = input()

    num_z = 0
    for c in s:
        if c == 'Z' or c == 'z':
            num_z += 1

    if num_z >= 3:
        print("Time to take a nap.")
    else:
        print("Perry saves the day!")