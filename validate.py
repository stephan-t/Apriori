from ast import literal_eval


# Validate input function
def validate_input(m, T=None):
    while True:
        try:
            m = literal_eval(m)
        except (ValueError, SyntaxError):
            m = input("Please enter a valid number: ")
            continue

        if m <= 0:
            m = input("Please enter a positive number: ")
            continue

        if type(m) == int and T is not None:
            if m > len(T):
                m = input("Please enter a number less than or equal to " + str(len(T)) + ": ")
                continue
            else:
                m /= len(T)
                break
        elif type(m) == float:
            if m > 1.0:
                m = input("Please enter a number less than or equal to 1.0: ")
                continue
            else:
                break
    return m
