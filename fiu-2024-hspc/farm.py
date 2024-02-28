num_cows = int(input())

x = []
y = []
for _ in range(num_cows):
    nx, ny = map(int, input().split())
    x.append(nx)
    y.append(ny)

# MIN MAX
min_x = min(x)
max_x = max(x)
min_y = min(y)
max_y = max(y)

perim = 2 * (max_x - min_x) + 2 * (max_y - min_y)
print(perim)
