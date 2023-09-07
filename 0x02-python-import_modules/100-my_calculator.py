#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit

    if len(argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    op = argv[2]

    if op == '+':
	result = add(a, b)
    elif op == '-':
	result = sub(a, b)
    elif op == '*':
	result = mul(a, b)
    elif op == '/':
	result = div(a, b)
    else :
        print("Unkown operator. Available operators: +, -, * and /")
        exit(1)

    print("{} {} {} = {}".format(a, op, b, result))
