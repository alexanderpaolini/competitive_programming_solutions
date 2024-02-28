# Submitted
import string

num_cases = int(input())

for _ in range(num_cases):
    x = list(filter(lambda x: x != " ", list(input())))

    obj = {}
    
    for l in x:
        if l in obj:
            obj[l] = obj[l] + 1
        else:
            obj[l] = 1

    print(max(obj.values()))