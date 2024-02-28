num_cases = int(input())

for _ in range(num_cases):
    _ = int(input())

    data = list(map(int, input().split()))

    s = sum(data)
    d_s = s % 3
    if d_s == 0:
        print("0")
    elif d_s == 2:
        print("1")
    else:
        found = False
        for d in data:
            if d % 3 == 1:
                found = True
        print("1" if found else "2")