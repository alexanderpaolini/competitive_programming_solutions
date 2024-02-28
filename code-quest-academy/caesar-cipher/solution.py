# Submitted
num_cases = int(input())

def cycle(char, num):
    code = ord(char) - num

    if (code > 122):
        code = code - 26

    if (code < 97):
        code = code + 26

    return chr(code)

for _ in range(num_cases):
    change = int(input())
    orig = list(input())
    string = ""
    for c in orig:
        if (c == " "):
            string += " "
            continue
        string += cycle(c, change)

    print(string)