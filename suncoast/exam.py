# Read the weights and number of test cases
f, c, h, num_cases = map(int, input().strip().split())

# Process each test case
for _ in range(num_cases):
    # Read the scores
    scores = input().strip().split()
    classwork_scores = [int(score[1:])
                        for score in scores if score.endswith('c')]
    homework_scores = [int(score[1:])
                       for score in scores if score.endswith('h')]

    # Calculate weighted averages for classwork and homework
    avg_classwork = sum(classwork_scores) / \
        len(classwork_scores) if classwork_scores else 0
    avg_homework = sum(homework_scores) / \
        len(homework_scores) if homework_scores else 0

    # If the weight of the final is zero, the final score depends only on classwork and homework
    if f == 0:
        final_grade = (c * avg_classwork + h * avg_homework) / (c + h)
        print("Impossible" if final_grade < 90 else "0")
    else:
        # Calculate the required score on the final
        required_final = (90 * (f + c + h) -
                          (c * avg_classwork + h * avg_homework)) / f

        # Check if the required score is possible
        if required_final <= 100:
            print(int(round(required_final, 0)))
        else:
            print("Impossible")
