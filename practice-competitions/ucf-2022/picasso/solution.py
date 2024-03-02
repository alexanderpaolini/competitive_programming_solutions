num_cases = int(input())

for _ in range(num_cases):
    n, x = map(int, input().split())
    t = list(map(int, input().split()))
    m = list(map(int, input().split()))

    comparison = []
    for i in range(n):
        comparison.append((m[i] - t[i], i))
    comparison.sort(key=lambda x: x[0], reverse=True)

    print(comparison)

    total = 0
    for i in range(x):
        index = comparison[i][1]
        total += m[index]
        t[index] = 0
    total += sum(t)
    
    print(total)