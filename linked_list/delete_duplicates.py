from list_node import ListNode


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        return Solution.__recur(head, set())

    def __recur(head: ListNode, uniq: set) -> ListNode:
        if head is None:
            return None
        if head.val in uniq:
            return Solution.__recur(head.next, uniq)
        uniq.add(head.val)
        rest = ListNode(head.val)
        rest.next = Solution.__recur(head.next, uniq)
        return rest
