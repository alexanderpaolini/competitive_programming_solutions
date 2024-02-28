num_cases = int(input())

for _ in range(num_cases):
    _ = int(input())

    data = sum(list(map(lambda x: abs(int(x)), input().split())))

    print(data)