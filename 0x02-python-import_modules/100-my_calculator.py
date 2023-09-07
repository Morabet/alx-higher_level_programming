#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit

    if len(argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)

    a = int(argv[1])
    b = int(argv[3])

    match argv[2]:
        case '+':
            result = add(a, b)
        case '-':
            result = sub(a, b)
        case '*':
            result = mul(a, b)
        case '/':
            result = div(a, b)
        case _:
            result = "NULL"

    if result == "NULL":
        print("Unkown operator. Available operators: +, -, * and /")
        exit(1)

    print("{} {} {} = {}".format(a, argv[2], b, result))
