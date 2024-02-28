# 1526 B - I Hate 1111 - https://codeforces.com/problemset/problem/1526/B
memo = {}

def generate_sequence_numbers_list(up_to):
    numbers = []
    num = 11
    while num <= up_to:
        numbers.append(num)
        num = int(str(num) + '1')
    return numbers

def try_subtract_memo(x, nums, memo):
    if x in memo:
        return memo[x]

    if x == 0:
        return True

    for num in nums:
        if num <= x and try_subtract_memo(x - num, nums, memo):
            memo[x] = True
            return True

    memo[x] = False
    return False

num_cases = int(input())

for  _ in range(num_cases):
    x = int(input())
    numbers = generate_sequence_numbers_list(x)
    if try_subtract_memo(x, numbers[::-1], memo):
        print("YES")
    else:
        print("NO")
