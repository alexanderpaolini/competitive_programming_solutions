# Unsolved
import math

num_cases = int(input())

for _ in range(num_cases):
    a, b, l = map(int, input().split())
    counter = 0

    for k in range(1, l + 1):
        for x in range(0, int(math.log(l, a)) + 2):
            if k * (a ** x) > l:
                break
            for y in range(0, int(math.log(l, b)) + 2):
                if k * (a ** x) * (b ** y) == l:
                    counter += 1
                elif k * (a ** x) * (b ** y) > l:
                    break 

    print(counter)