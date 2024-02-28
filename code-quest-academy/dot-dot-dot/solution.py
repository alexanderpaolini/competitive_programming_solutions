# Submitted
cases = int(input())

for _ in range(cases):
    num = sum(list(map(lambda x: ord(x) - 96, list(input()))))
    print(num)
