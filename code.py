def are_valid_groups(students,groups):
    for x in students:
        c = 0
        while c != 0 and c < 2 :
            for y in groups:
                for group_member in y :
                    if x == group_member :
                        c += 1
                if c > 1:
                    break
            if c > 1:
                break
        if c != 1:
            return False
    return True