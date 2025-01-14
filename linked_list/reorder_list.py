from doubly_list_node import ListNode


def reorder_list(head: ListNode, tail: ListNode) -> ListNode:
    reordered = ListNode(0)
    i = head
    j = tail
    k = reordered
    while i != j and i.prev != j:
        k.next = ListNode(i.val)
        k.next.prev = k
        k = k.next
        i = i.next
        k.next = ListNode(j.val)
        k.next.prev = k
        k = k.next
        j = j.prev

    reordered.next.prev = None
    return reordered.next


class Solution:
    def reorderList(self, head: ListNode, tail: ListNode) -> ListNode:
        return reorder_list(head, tail)
