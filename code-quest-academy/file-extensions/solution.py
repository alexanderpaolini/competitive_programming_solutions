# Submitted
num_cases = int(input())

l_ext = []
l_count = []

for _ in range(num_cases):
    file = input().split('.')
    ext = file.pop()

    index = l_ext.index(ext) if ext in l_ext else -1

    if index != -1:
        l_count[index] += 1
    else:
        l_ext.append(ext)
        l_count.append(1)

for i, ext in enumerate(l_ext):
    count = l_count[i]
    print(f"{ext} {count}")