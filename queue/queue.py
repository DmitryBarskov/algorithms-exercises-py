import sys


class Queue:
    """A simple queue based on list"""
    queue = []
    start = 0

    def enqueue(self, item: any) -> None:
        self.queue.append(item)

    def dequeue(self) -> any:
        item = self.queue[self.start]
        self.start += 1
        return item

    def __len__(self) -> int:
        return len(self.queue) - self.start


def main():
    queue = Queue()
    for line in sys.stdin:
        if line == "+\n":
            print(queue.dequeue())
        elif len(queue) <= 4:
            queue.enqueue(line.strip())


if __name__ == "__main__":
    main()
