num_cases = int(input())

for _ in range(num_cases):
    s = input()

    out = ""
    curr = ""
    for i in range(len(s)):
        c = s[i]
        if c == "A" or c == "T":
            curr += "0"
        else:
            curr += "1"

        if i % 7 == 6:
            out += chr(int(curr, 2))
            curr = ""

    print(out)