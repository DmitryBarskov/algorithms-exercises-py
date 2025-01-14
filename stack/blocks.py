# Finds minimum amount of rectangular blocks required to build a wall
# with given heights. E.g. [2 2 1 2 3] means that first meter of wall is
# 2 meters high, second meter as well, third is 1m high, fourth is 2m high,
# and the fifth is 3m high.
#     x
# xx xx
# xxxxx
# So the wall looks like this. We can build this wall out of 4 blocks:
#     d
# aa cc
# aabcc one letter = one block
# or
#     d
# aa cc
# bbbbb
# Blocks should have rectangular shape.
def min_blocks(heights: list) -> int:
    growing = [0]
    blocks = 0
    for i in range(0, len(heights)):
        while growing[-1] > heights[i]:
            growing.pop()
            blocks += 1
        if growing[-1] == heights[i]:
            continue
        growing.append(heights[i])
    return blocks + len(growing) - 1


def test(heights, expected):
    result = min_blocks(heights)
    if result != expected:
        print(f'❌ {heights} => Expected {expected}, got {result}')
    else:
        print(f'✅ {heights} => {result} pass')


def run_tests():
    test([1, 3, 4, 1, 4, 4], 4)
    test([2, 2, 3, 2, 3], 3)
    test([2, 2, 1, 2, 3], 4)
    test([1, 10, 12, 10, 1], 3)
    test([1, 10, 12, 15, 10, 1], 4)
    test([1, 10, 12, 15, 12, 10, 1], 4)


if __name__ == '__main__':
    print(min_blocks(list(map(int, input().split()))))
