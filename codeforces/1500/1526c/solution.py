# 1526 C1 and C2 - https://codeforces.com/problemset/problem/1526/C2
import heapq

_ = int(input())
potions = list(map(int, input().split()))

health = 0
min_heap = []
count = 0

for potion in potions:
    if potion >= 0:
        health += potion
        count += 1
    else:
        if health + potion >= 0:
            heapq.heappush(min_heap, potion)
            health += potion
            count += 1
        elif min_heap and min_heap[0] < potion:
            health += potion - heapq.heappop(min_heap)
            heapq.heappush(min_heap, potion)

print(count)