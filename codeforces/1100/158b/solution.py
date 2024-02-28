# 158 B - Taxi - https://codeforces.com/problemset/problem/158/B
m = {
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0,
}

n = int(input())
for i in input().split():
    m[i] += 1

# Combine to make 4
while m["1"] and m["3"]:
    m["3"] -= 1
    m["1"] -= 1
    m["4"] += 1

# Combine to make 4
while int(m["2"] / 2):
    m["2"] -= 2
    m["4"] += 1

# Combine to make 4
while m["1"] >= 4:
    m["1"] -= 4
    m["4"] += 1

# Combine to make 4
if m["2"] and m["1"] == 2:
    m["4"] += 1
    m["2"] -= 1
    m["1"] -= 2

# to make 3
if m["2"] and m["1"] == 1:
    m["2"] -= 1
    m["1"] -= 1
    m["3"] += 1
if m["1"] == 3:
    m["1"] = 0
    m["3"] += 1
if m["1"] == 2:
    m["1"] = 0
    m["2"] += 1

"""
make 4
- 1 1 1 1
3 1
2 1 1
make 3
2 1
1 1 1
make 2
1 1
"""

print(sum(m.values()))