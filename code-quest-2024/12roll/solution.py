# Submitted
num_cases = int(input())

for _ in range(num_cases):
    c, p = map(int, input().split())

    classes = {}
    for _ in range(c):
        classs = input().split()
        classes[classs.pop(0)] = classs

    for _ in range(p):
        d = input().split()

        name = d.pop(0)

        nums = list(reversed(sorted(list(map(int, d)))))

        print(name)
        # STR
        print("STR: " + str(nums[classes.get(name).index("STR")]))
        print("DEX: " + str(nums[classes.get(name).index("DEX")]))
        print("CON: " + str(nums[classes.get(name).index("CON")]))
        print("INT: " + str(nums[classes.get(name).index("INT")]))
        print("WIS: " + str(nums[classes.get(name).index("WIS")]))
        print("CHA: " + str(nums[classes.get(name).index("CHA")]))