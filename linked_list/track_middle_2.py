class ListNode:
    def __init__(self, val, following = None):
        self.val = val
        self.next = following


class Queue:
    def __init__(self):
        self.size = 0
        self.tail = ListNode(None)
        self.head = ListNode(None, self.tail)
        # in odd sized list middle is the middle
        # in even sized list middle is the last of the first half
        self.middle = self.head

    def prepend(self, item: int):
        inserted = ListNode(item, self.head.next)
        self.head.next = inserted
        self.size += 1
        self._adjust_middle()

    def append(self, item: int):
        self.tail.val = item
        self.tail.next = ListNode(None)
        self.tail = self.tail.next
        self.size += 1
        self._adjust_middle()

    def insert_after_middle(self, item: int):
        inserted = ListNode(item, self.middle.next)
        self.middle.next = inserted
        self.size += 1
        self._adjust_middle()

    def pop_first(self) -> int:
        if self.size == 0:
            return None
        popped = self.head.next.val
        self.head.next = self.head.next.next
        self.size -= 1
        self._adjust_middle()
        return popped

    def _adjust_middle(self):
        if self.size % 2 == 1:
            self.middle = self.middle.next


def main():
    input_lines = int(input())
    q = Queue()
    for _ in range(input_lines):
        op, *args = input().strip().split(' ')
        args = map(int, args)
        if op == '+':
            print(q.pop_first())
        elif op == 'c':
            q.prepend(*args)
        elif op == 's':
            q.append(*args)
        elif op == 'i':
            q.insert_after_middle(*args)


if __name__ == '__main__':
    main()
