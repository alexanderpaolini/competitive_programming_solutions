# 1837 B - Comparison String - https://codeforces.com/problemset/problem/1837/B
num_cases = int(input())

for _ in range(num_cases):
    _ = int(input())
    s = input()

    ans = 0
    cnt = 0
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            cnt += 1
            ans = max(ans, cnt)
        else:
            cnt = 0

    print(ans + 2)