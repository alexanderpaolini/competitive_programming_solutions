num_cases = int(input())

for _ in range(num_cases):
    num = int(input()) - 3
    data = [1, 1, 1]

    for i in range(2, -1, -1):
        add = min(25, num)
        num -= add
        data[i] += add

    string = "".join(chr(x + 96) for x in data)
    print(string)
