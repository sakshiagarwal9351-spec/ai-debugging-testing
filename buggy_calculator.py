

def calculate_average(marks):
    if not marks:
        return 0

    total = 0

    for mark in marks:
        total += mark

    average = total / len(marks)
    return average


def check_result(average):
    if average >= 40:
        return "Pass"
    else:
        return "Fail"


marks = [75, 80, 65, 90]

average = calculate_average(marks)

print("Average:", average)
print("Result:", check_result(average))
