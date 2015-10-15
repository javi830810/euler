
def f(digits, target, current=None, rest=None):
    """
        It doesnt work for the given case, it does for small runs
        Some performance situation...

        The idea is to try each digit with each of the operators
        once the digit have been used, it will be appended to the current
        and a new iteration will be done with the other digits.

        It's important to notice that each digit will be tried recursively and exhaustively with every operator
    """
    if not digits:
        return

    if not current and not rest:
        current = ""
        rest = digits

    if not rest:
        return

    operators = ['+', '-', '*', '/']
    index = 1

    for digit in rest:
        temp_current = current
        temp_rest = rest[index:]
        if temp_rest:
            for operator in operators:
                current += digit + " " + operator
                expression = current + temp_rest

                if eval(expression) == target:
                    print expression

                f(digits, target, current, temp_rest)

                current = temp_current

        current = temp_current + digit

        index += 1

f("314159265358",27182)
