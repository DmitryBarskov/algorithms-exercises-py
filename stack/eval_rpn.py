def eval_rpn(tokens: list, operations: dict):
    stack = []
    for token in tokens:
        result = None
        if token in operations:
            right = stack.pop()
            left = stack.pop()
            result = operations[token](left, right)
        else:
            result = int(token)
        stack.append(result)
    return stack.pop()


integer_operations = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
}

if __name__ == "__main__":
    result = eval_rpn(input().split(), integer_operations)
    print(result)

