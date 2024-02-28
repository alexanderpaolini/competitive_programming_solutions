# 987 C - Three displays - https://codeforces.com/problemset/problem/987/C
n = int(input())
nums = list(map(int, input().split()))
values = list(map(int, input().split()))

min_value = 1e99

for i in range(1, n-1):
    left = -1
    for j in range(i):
        if nums[j] < nums[i]:
            if left == -1 or values[j] < values[left]:
                left = j

    right = -1
    for k in range(i+1, n):
        if nums[i] < nums[k]:
            if right == -1 or values[k] < values[right]:
                right = k

    if left != -1 and right != -1:
        min_value = min(min_value, values[left] + values[i] + values[right])

print(min_value if min_value != 1e99 else -1)