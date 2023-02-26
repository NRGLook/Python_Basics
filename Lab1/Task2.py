def simple_calculator(num1, num2,
                      operation):
    operation = operation.lower()
    match operation:
        case "add":
            return num1 + num2
        case "sub":
            return num1 - num2
        case "mult":
            return num1 * num2
        case "div":
            if num2 == 0:
                return "Infinity"
            return num1 / num2
        case _:
            return "Check your input!" \
                   " Something is incorrect!" \
                   " Try Again!"\

print(simple_calculator(1, 2,
                        "add"))
print(simple_calculator(1, 2,
                        "mult"))
print(simple_calculator(0, 0,
                        "div"))
print(simple_calculator(1, 0,
                        "div"))
print(simple_calculator(1, 0,
                        "way"))


