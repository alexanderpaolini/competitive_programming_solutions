# Submitted
import math

num_cases = int(input())

cir = 40075
radius = cir / 2 / math.pi

for _ in range(num_cases):
    new_radius = radius + int(input())
    new_cir = new_radius * 2 * math.pi
    print(round(new_cir * 10) / 10)