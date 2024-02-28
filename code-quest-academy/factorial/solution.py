# Submitted
num_cases = int(input())


def factorial(num):
    output = 1
    while (num > 0):
        output *= num
        num -= 1
    return output


for _ in range(num_cases):
    print(factorial(int(input())))
