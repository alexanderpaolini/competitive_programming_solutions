# Wrong answer (Not sure why)
def determine_grade(g):
    if g >= 90:
        return 'A'
    if g >= 80:
        return 'B'
    if g >= 70:
        return 'C'
    if g >= 60:
        return 'D'
    return 'F'


num_cases = int(input())


for _ in range(num_cases):
    l1 = input().split(' ')

    num_students = int(l1[0])
    correct_answers = l1[1]
    num_answers = len(correct_answers)

    for student in range(num_students):
        studentInfo = input().split(' ')
        student_name = studentInfo[0]
        student_answers = studentInfo[1]

        count = 0
        for index, answer in enumerate(student_answers):
            if answer == correct_answers[index]:
                count += 1

        # rounding error???
        percentage = count / num_answers * 100
        print(f"{student_name} {round(percentage, 1)}% " +
              f"{determine_grade(percentage)}")