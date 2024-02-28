# Note: Incomplete solution -- does not account for the word appearing more than once per line.
num_cases = int(input())

for _ in range(num_cases):
    a = int(input())
    x = ""
    for _ in range(a):
        x += " " + input()
    x = x.strip()

    x = list(map(lambda x: x.strip().split(" "), x.split(".")))
    word = input()

    for i in x:
        index = i.index(word) if word in i else -1
        if not index:
            continue

        out = []

        front = []
        x = index - 1
        while (x >= 0 and index - x < 4):
            front.append(i[x])
            x -= 1
        front.reverse()

        back = []
        y = index + 1
        while (y <= len(i) - 1 and y - index < 6):
            back.append(i[y])
            y += 1

        for a in front:
            out.append(a)
        out.append(f"*{word}*")
        for a in back:
            out.append(a)

        output_str = " ".join(out)
        if out[0] != i[0]:
            output_str = "..." + output_str
        if out[len(out) - 1] != i[len(i) - 1]:
            output_str += "..."
        else:
            output_str += "."

        print(output_str)



# 3 to the left
# 5 after