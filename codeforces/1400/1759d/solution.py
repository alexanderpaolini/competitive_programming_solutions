# 1759 D - Make it Round - https://codeforces.com/problemset/problem/1526/B
# INCOMPLTE - Time Constraint
num_cases = int(input())

def num_zeros(num, memo):
    if num in memo:
        return memo[num]

    count = 0
    while num % 10 == 0:
        num /= 10
        count += 1

    memo[num] = count

    return count

for _ in range(num_cases):
    n, m = map(int, input().split())

    memo = {}

    max_num = n
    max_zeros = num_zeros(n, memo)
    for i in range(2, m + 1):
        current_num = i * n
        current_zeros = num_zeros(current_num, memo)
        if current_zeros > max_zeros or current_zeros == max_zeros and current_num > max_num:
            max_num = current_num
            max_zeros = current_zeros

    print(max_num)