def evalRPN(tokens):
    stack = []
    for item in tokens:
        if item == '+':
            stack.append(stack.pop() + stack.pop())
        elif item == '-':
            stack.append(stack.pop(-2) - stack.pop())
        elif item == '*':
            stack.append(stack.pop() * stack.pop())
        elif item == '/':
            stack.append(int(stack.pop(-2) / stack.pop()))
        else:
            stack.append(int(item))
    return stack[0]


def main():
    test1 = ['2', '1', '+', '3', '*']
    test2 = ['4', '13', '5', '/', '+']
    test3 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    print(evalRPN(test1), evalRPN(test2), evalRPN(test3))


if __name__ == '__main__':
    main()
