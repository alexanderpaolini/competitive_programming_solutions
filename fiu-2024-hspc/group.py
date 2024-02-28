num_students = int(input())

hours = []
for _ in range(num_students):
    student = input().split()
    num = int(student.pop(0))

    for _ in range(num):
        x, y = map(int, [student.pop(0), student.pop(0)])
        for i in range(x, y):
            hours.append(i)

hours = sorted(hours)

curr = 0
num = 0
m = 0
for i in range(len(hours)):
    if curr == hours[i]:
        num += 1
    else:
        curr = hours[i]
        num = 1

    m = max(m, num)

if m == num_students:
    print("Yes")
else:
    print("No")
