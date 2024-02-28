# 1900 B - Laura and Operations - https://codeforces.com/problemset/problem/1900/B
num_cases = int(input())

for _ in range(num_cases):
    a, b, c = map(int, input().split())

    print(
        int(max(b, c) >= min(b, c) and (max(b, c) - min(b, c)) % 2 == 0),
        int(max(a, c) >= min(a, c) and (max(a, c) - min(a, c)) % 2 == 0),
        int(max(a, b) >= min(a, b) and (max(a, b) - min(a, b)) % 2 == 0)
    )
