s = input()

for i in range(1, len(s) - 1):
    if s[i-1] == s[i]:
        print("No sleep here.")
        break

print("Goodnight!")