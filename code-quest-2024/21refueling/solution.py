# Note: Incomplete solution – Attempted to solve as first problem but it was much more complex than I first thought
import math

num_cases = int(input())

for _ in range(num_cases):
    sirus = input().split()
    speed = float(sirus.pop(0))
    sirus_x = float(sirus.pop(0))
    sirus_y = float(sirus.pop(0))
    num_ships = int(sirus.pop(0))

    ships = []
    for _ in range(num_ships):
        s = input().split()
        name = s.pop(0)
        dis = s.pop(0)
        x = int(s.pop(0))
        y = int(s.pop(0))
        
        liters = float(s.pop(0))
        lph = float(s.pop(0))

        dist = math.sqrt(math.pow(sirus_x - x, 2) + math.pow(sirus_y - y, 2))
        print(dist)
        time = liters / lph - (speed * (dist))

        ship = (name, x, y, time)
        if dis == "Allied":
            ships.append(ship)

    ships = sorted(ships, key=lambda x: x[3])
    # for s in ships:
    #     print(s[0])
    print(ships)

