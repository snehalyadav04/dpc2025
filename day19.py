def evaluate_postfix(expression: str) -> int:
    tokens = expression.split()
    stack = []

    for token in tokens:
        if token in "+-*/^":
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(int(a / b))  
            elif token == '^':
                stack.append(pow(a, b))
        else:
            stack.append(int(token))

    return stack[0]

expressions = [
    "5 6 +",
    "3 4 2 * 1 5 - 2 3 ^ ^ / +",
    "-5 6 -",
    "15 7 1 1 + - / 3 * 2 1 1 + + -",
    "5"
]

for expr in expressions:
    print(f'Input: "{expr}"')
    print("Output:", evaluate_postfix(expr))
    print()
