def are_valid_groups(students, groups):

    for student in students:
        studentCounter = 0
        for group in groups:
            if student in group:
                studentCounter += 1

        if studentCounter != 1:
            return False

    return True
