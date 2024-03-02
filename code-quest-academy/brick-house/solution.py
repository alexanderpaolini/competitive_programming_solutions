# Submitted
num_cases = int(input())

for _ in range(num_cases):
    small, large, total = map(int, input().split())

    num_large_bricks = total // 5
    total = total - 5 * min(num_large_bricks, large)

    if small >= total:
        print("true")
    else:
        print("false")























