# 455 A - Boredome - https://codeforces.com/problemset/problem/455/A
from collections import Counter

_ = int(input())
sequence = list(map(int, input().split()))

freq = Counter(sequence)
max_num = max(sequence)

dp = [0] * (max_num + 1)

for i in range(1, max_num + 1):
    dp[i] = max(dp[i - 1], (dp[i - 2] if i - 2 >= 0 else 0) + i * freq[i])

print(dp[max_num])