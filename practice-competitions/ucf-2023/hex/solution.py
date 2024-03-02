n, s = map(int, input().split())

hexes = []

for _ in range(n):
    hexes.append(input())

looking_for = input()

found = False
for h in hexes:
    for h_2 in hexes:
        if looking_for in h + h_2:
            found = True
            break
    if found:
        break

print("Helga is loveable" if found else "Toil and Trouble")