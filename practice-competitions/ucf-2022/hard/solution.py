num_cases = int(input())

for _ in range(num_cases):
    l1, c1, l2, c2 = map(int, input().split())

    print(max(l1 * c1, l2 * c2))