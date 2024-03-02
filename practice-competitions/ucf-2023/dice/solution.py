s, v = map(int, input().split())

for _ in range(v):
    # 3
    # 2
    # 1 + 1 + 1
    # 2 + 1
    # (1/3 + (1/3 * 1/3) + (1/3 * 1/3) + (1/3 * 1/3 * 1/3))
    # 3 first roll 1/3

    # 2 first roll 1/3
    # 1 second roll 1/3

    # 1 first roll 1/3
    # 2 second roll 1/3

    # 1 first roll 1/3
    # 1 second roll 1/3
    # 1 third roll 1/3
    t = int(input())
