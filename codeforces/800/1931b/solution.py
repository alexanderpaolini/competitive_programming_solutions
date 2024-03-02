# 1931 B - Make Equal - https://codeforces.com/problemset/problem/1931/B
num_cases = int(input())

for _ in range(num_cases):
    _ = int(input())
    d = list(map(int, input().split()))

    avg = sum(d) / len(d)

    can = True
    running_sum = 0
    for i in range(len(d)):
        running_sum += d[i]
        if running_sum < (i + 1) * avg:
            can = False
            break
    
    print("YES" if can else "NO")