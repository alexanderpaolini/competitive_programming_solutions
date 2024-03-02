n, m = map(int, input().split())

data = []

for _ in range(n):
    data.append(input())

ma = 0
mi = 0
for i in range(n):
    l = data[i]
    for j in range(len(l)):
        c = l[j]
        if c == "P":
            count  = 0  
            # Check left
            if j > 0 and l[j-1] == "#":
                count += 1
            # Check right
            if j < len(l) - 1 and l[j+1] == "#":
                count += 1
            # Check top
            if i > 0 and data[i - 1][j] == "#":
                count += 1
            # Check bottom
            if i < len(data) - 1 and data[i + 1][j] == "#":
                count += 1
        
            if count >= 2:
                mi += 1
            if count >= 1:
                ma += 1

print(mi, ma)