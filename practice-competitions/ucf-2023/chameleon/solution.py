n = int(input())
a = input().split()

count = 1
prev = a[0]
for i in range(1, n):
    if a[i] != prev:
        count += 1
        prev = a[i]

print(count)