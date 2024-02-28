# Submitted
def slg (n, s, d, t, h):
    total = (n + s + d + t + h)
    if total == 0:
        return 0
    return (1 * s + 2 * d + 3 * t + 4 * h) / total

num_cases = int(input())

for _ in range(num_cases):
    name,data = input().split(":")
    n = 0
    s = 0
    d = 0
    t = 0
    h = 0

    for play in data.split(","):
        if play == "K":
            n += 1
        elif play == "1B":
            s += 1
        elif play == "2B":
            d += 1
        elif play == "3B":
            t += 1
        elif play == "HR":
            h += 1
    
    print("{}={:.3f}".format(name, round(slg(n, s, d, t, h), 3)))