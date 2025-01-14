from list_node import ListNode


def cons(val: int, rest: ListNode) -> ListNode:
    l = ListNode(val)
    l.next = rest
    return l


def reverse(head: ListNode, acc: ListNode) -> ListNode:
    if head is None:
        return acc
    return reverse(head.next, cons(head.val, acc))


class Solution:
    def reverse(self, head: ListNode) -> ListNode:
        return reverse(head, None)
