from list_node import ListNode


def cons(val: int, rest: ListNode) -> ListNode:
    l = ListNode(val)
    l.next = rest
    return l


def insert_into_sorted(head: ListNode, new_value: int) -> ListNode:
    if head is None or new_value >= head.val:
        return cons(new_value, head)
    return cons(head.val, insertIntoSorted(head.next, new_value))
    

class Solution:
    # Insert a value into non-increasing list
    def insertIntoSorted(self, head: ListNode, new_value: int) -> ListNode:
        return insert_into_sorted(head, new_value)
