# Note: This one was written by my teamate
cases = int(input())
maps = {}
for i in range(cases):
    letter, binary = input().split()
    maps[binary] = letter

text = input()
output = ""
temp = ""
for i in range(len(text)):
    temp += text[i]
    if temp in maps:
        output += maps[temp]
        temp = ""

print(output)