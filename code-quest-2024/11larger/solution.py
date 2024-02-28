# Note: Incorrect solution
import functools

num_cases = int(input())

def custom_sorting_algo(s1, s2):
    if s1 == s2:
        return 0
    s1 = list(s1)
    s2 = list(s2)
    for i in range(min(len(s1), len(s2))):
        if s1[i] == s2[i]:
            continue
        elif int(s1[i]) > int(s2[i]):
            return 1
        else:
            return -1
    return 0

for _ in range(num_cases):
    nums = list(reversed(sorted(input().split(), key=functools.cmp_to_key(custom_sorting_algo))))
    print("".join(nums))