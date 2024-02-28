# 1363 A - Odd Selection - https://codeforces.com/problemset/problem/1363/A
num_cases = int(input())

for _ in range(num_cases):
    _, x = map(int, input().split())

    l = list(map(lambda x: int(x) % 2, input().split()))

    n_even = len(list(filter(lambda x: x == 0, l)))
    n_odd = len(list(filter(lambda x: x == 1, l)))

    count = 0
    if n_odd == 0:
        print("No")
        continue
    else:
        n_odd -= 1
        x -= 1
    
    x -= min((x // 2) * 2, (n_odd // 2) * 2)

    if x == 0 or x <= n_even:
        print("Yes")
    else:
        print("No")