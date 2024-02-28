# Submitted
def move_ship(ship):
    if ship["type"] == "A":
        ship["x"] -= 10
    if ship["type"] == "B":
        ship["x"] -= 20
    if ship["type"] == "C":
        ship["x"] -= 30
    return ship


case_num = int(input())

for _ in range(case_num):
    ships = []

    ships_num = int(input())

    for _ in range(ships_num):
        ship = input()
        fullname, pos = ship.split(":")
        name, type = fullname.split("_")
        x, y = map(int, pos.split(","))

        ships.append({
            "name": name,
            "x": x,
            "y": y,
            "type": type
        })

    while len(ships) > 0:
        min_x = ships[0]["x"]
        max_y = ships[0]["y"]
        name = ships[0]["name"]
        index = 0
        for i, ship in enumerate(ships):
            if ship["x"] < min_x or ship["x"] == min_x and ship["y"] > max_y:
                min_x = ship["x"]
                max_y = ship["x"]
                name = ship["name"]
                index = i

        print(f"Destroyed Ship: {name} xLoc: {min_x}")

        ships.pop(index)
        ships = list(map(move_ship, ships))
