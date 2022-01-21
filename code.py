def are_valid_groups(students,groups):
    for student in students:
        c = 0
        while c != 0 and c < 2 :
            for group in groups:
                for group_member in group :
                    if student == group_member :
                        c += 1
                if c > 1:
                    break
            if c > 1:
                break
        if c != 1:
            return False
    return True
