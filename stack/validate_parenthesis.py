def is_valid(string: str, parenthesis: dict) -> bool:
    stack = []
    for char in string:
        if char in parenthesis:
            stack.append(parenthesis[char])
        elif char in parenthesis.values():
            if len(stack) == 0 or char != stack.pop():
                return False
    return len(stack) == 0


if __name__ == "__main__":
    matching_parenthesis = {
        "(": ")",
        "{": "}",
        "[": "]",
    }
    if is_valid(input(), matching_parenthesis):
        print("CORRECT")
    else:
        print("WRONG")
