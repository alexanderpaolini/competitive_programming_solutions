# Submitted
num_cases = int(input())

for _ in range(num_cases):
    length = int(input())
    for i in range(2 ** length):
        string = bin(i).removeprefix('0b')
        while len(string) != length:
            string = "0" + string
        print(string)