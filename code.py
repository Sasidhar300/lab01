def are_valid_groups(students, groups):
    NumOfStudentsfound = 0
    for student in students:
        c = 0
        for group in groups:
            if student in group:
                c += 1

        if (c != 1):
            return False
        else:
            NumOfStudentsfound += 1
    
    if NumOfStudentsfound == len(students):
        return True
    else:
        return False
        