from doubly_list_node import ListNode


def is_palindrome(head: ListNode, tail: ListNode) -> bool:
    if head == tail.prev or head == tail:
        return True
    return head.val == tail.val and is_palindrome(head.next, tail.prev)


class Solution:
    def isPalindrome(self, head: ListNode, tail: ListNode) -> bool:
        return is_palindrome(head, tail)
