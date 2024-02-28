# Submitted
def dist(num1, num2):
    """Return the distance between two numbers."""
    return (num1 ** 2 + num2 ** 2) ** (.5)

num_cases = int(input())

for _ in range(num_cases):
    l = []
    for _ in range(int(input())):
        x,y = map(int, input().split())
        distance = dist(x, y)
        l.append((distance, x, y))

    l.sort(key=lambda x: x[0])

    for i in range(len(l)):
        print(l[i][1], l[i][2])