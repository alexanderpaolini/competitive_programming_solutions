s, x = input().split()
x = int(x)

delim = ' '
for i in range(26):
    ch = chr(i + ord('a'))
    if not s.count(ch):
        delim = ch

print(delim.join([s] * x))