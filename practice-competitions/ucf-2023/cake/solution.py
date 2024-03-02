s = int(input())

def rec(num):
    if num == 0:
        return 0
    if num == 2:
        return 1

    if num % 2 == 1:
        return rec(num - 1)
    else:
        return 1 + rec(num / 2) + rec(num / 2)
    
count = rec(s)

print(count)