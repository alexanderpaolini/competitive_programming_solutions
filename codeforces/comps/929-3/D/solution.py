# Unsolved
num_cases = int(input())

def is_prime(n):
    if n == 0:
        return False
    for i in range(2, int(n ** .5)):
        if n % i == 0:
            return False
    return True

for _ in range(num_cases):
    _ = int(input())

    data = list(map(int, input().split()))
    new_data = []

    while len(data):
        curr = data[0]
        found = 0
        for i in data:
            if curr % i != 0:
                found = i
                break
        if found:
            data.remove(found)
        else:
            print("NO")
    if not data:
        print("YES")