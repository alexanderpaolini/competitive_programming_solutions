# Submitted
UPPER_CASE_LETTERS = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
LOWER_CASE_LETTERS = list("abcdefghijklmnopqrstuvwxyz")
NUMBERS = list("0123456789")

cases = int(input())

for _ in range(cases):
    password = list(input())
    flag = False

    if len(password) < 8:
        flag = True

    upper_case = False
    lower_case = False
    numbers = False
    alphanumeric = False

    for i in range(len(password)):
        char = password[i]
        if (char in UPPER_CASE_LETTERS):
            upper_case = True
        if (char in LOWER_CASE_LETTERS):
            lower_case = True
        if (char in NUMBERS):
            numbers = True

    if len(list(filter(lambda x: x not in UPPER_CASE_LETTERS and x not in LOWER_CASE_LETTERS and x not in NUMBERS, password))) > 0:
        alphanumeric = True

    if len(list(filter(lambda x: x, [upper_case, lower_case, alphanumeric, numbers]))) < 3:
        flag = True

    for i in range(len(password)):
        if i + 2 >= len(password):
            break
        if password[i] == password[i + 1] and password[i] == password[i + 2]:
            flag = True

    if flag:
        print("INVALID")
    else:
        print("VALID")
