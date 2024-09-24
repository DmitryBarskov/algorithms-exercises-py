from list_node import ListNode


class Solution:
    def getDecimalValue(self, head: ListNode, acc: int = 0) -> int:
        if head is None:
            return acc
        return self.getDecimalValue(head, head.next, acc * 2 + head.val)
