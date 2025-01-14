def first_greater_after(numbers: list) -> list:
    stack = [-1]
    result = [None] * len(numbers)
    for i in reversed(range(len(numbers))):
        while len(stack) > 1 and stack[-1] <= numbers[i]:
            stack.pop()
        result[i] = stack[-1]
        stack.append(numbers[i])
    return result


if __name__ == '__main__':
    numbers = list(map(int, input().split()))
    greater = first_greater_after(numbers)
    print(" ".join(map(str, greater)))
