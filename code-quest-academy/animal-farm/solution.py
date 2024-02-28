# Submitted
num_cases = int(input())

for _ in range(num_cases):
    t,g,h = map(int, input().split())

    print(t * 2 + g * 4 + h * 4)