# 4 C - Registration system - https://codeforces.com/problemset/problem/4/C
n = int(input())

m = {}

for _ in range(n):
    s = input()
    if s in m:
        m[s] += 1
        print(s + str(m[s]))
    else:
        m[s] = 0
        print("OK")
