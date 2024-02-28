# Submitted
num_cases = int(input())

for _ in range(num_cases):
    speed, birthday = input().split()
    speed = int(speed)
    birthday = birthday == 'true'

    speeds = [60, 80]

    if birthday:
        speeds = list(map(lambda x: x + 5, speeds))
    
    if speed <= speeds[0]:
        print("no ticket")
    elif speed <= speeds[1]:
        print("small ticket")
    else:
        print("big ticket")