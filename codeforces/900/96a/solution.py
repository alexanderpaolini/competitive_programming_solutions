# 96 A - Football - https://codeforces.com/problemset/problem/96/A
s = list(input())
count = 1
curr = s[0]
for i in range(1, len(s)):
    if s[i] == curr:
        count += 1
        if count == 7:
            break
    else:
        curr = s[i]
        count = 1
if count == 7:
    print("YES")
else:
    print("NO")