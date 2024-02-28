# Submitted
num_cases = int(input())

for _ in range(num_cases):
    l = list(map(int, input().split()))
    maximum = l[0]
    for x in l:
        if x > maximum:
            maximum = x
    print(maximum)