# Note: This one was written by my teamate
text = input()
seen = {}
for i in range(len(text)):
    if text[i] in seen:
        seen[text[i]] += 1
    else:
        seen[text[i]] = 1

output = 0
thing = []
for key, value in seen.items():
    thing.append(value)

thing = sorted(thing)
thing = thing[::-1]
for i in range(len(thing)):
    if i < 8:
        output += thing[i]
    elif i < 16:
        output += thing[i] * 2
    elif i < 24:
        output += thing[i] * 3
    else:
        output += thing[i] * 4

print(output)
