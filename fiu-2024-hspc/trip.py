a = int(input())
buildings = []
for i in range(a):
    buildings.append(int(input()))
thing = max(buildings)
print(buildings.index(thing) + 1)
