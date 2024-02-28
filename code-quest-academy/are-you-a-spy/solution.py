# Submitted
import string
num_cases = int(input())

for _ in range(num_cases):
    l1,l2 = map(
            lambda x: list(filter(lambda y: y in string.ascii_lowercase, list(x))),
            input().lower().split('|')
    )

    flag = False
    for char in l2:
        if char not in l1:
            flag = True

    if flag:
        print("You're not a secret agent!")
    else:
        print("That's my secret contact!")
