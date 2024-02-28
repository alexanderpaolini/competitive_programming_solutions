# 1 A - Theatre Square - https://codeforces.com/problemset/problem/1/A
from math import ceil

n, m, a = map(int, input().split())
n = ceil(n/a)
m = ceil(m/a)

print(n * m)