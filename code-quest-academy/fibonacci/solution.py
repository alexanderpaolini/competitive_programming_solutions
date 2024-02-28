# Submitted
num_cases = int(input())

def fib(n, memo={}):
    if n in memo:
        return memo[n]
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
        return memo[n]

for _ in range(num_cases):
    num = int(input())
    f = fib(num)

    print(f"{num} = {f}")
