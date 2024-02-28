# Submitted
num_cases = int(input())

alphabet = list(input())

for _ in range(num_cases - 1):
    nums = map(lambda x: x.split("-"), input().split(" "))

    string = ""
    for l in nums:
        for c in l:
            string += alphabet[int(c) - 1]
        string += " "

    print(string.strip())