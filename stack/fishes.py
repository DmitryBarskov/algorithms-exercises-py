# There are fishes in the river. Each of them travels either left or right.
# When two meet the bigger fish eats the smaller one and continue with
# the direction. Output how many fishes are alive when all fishes met.
# Given two lists
# - first represents size of i-th fish
# second represents direction of i-th fish: 0 stands for left, 1 for right

def fishes_alive(sizes: list, directions: list) -> int:
    stack = []
    for size, direction in zip(sizes, directions):
        while direction == 0 and len(stack) > 0 and \
                stack[-1][1] == 1 and size > stack[-1][0]:
            stack.pop()

        if len(stack) == 0 or stack[-1][1] == 0 or \
                (stack[-1][1] == 1 and direction == 1):
            stack.append((size, direction))
        elif stack[-1][1] == 1 and direction == 0 and size > stack[-1][0]:
            stack.pop()
            stack.append((size, direction))
    return len(stack)


if __name__ == '__main__':
    sizes = map(int, input().split())
    directions = map(int, input().split())
    print(fishes_alive(sizes, directions))
