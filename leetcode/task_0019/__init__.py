from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val} -> {self.next}'


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        while n and fast:
            fast = fast.next
            n -= 1

        dump = ListNode(None, head)
        prev =
        while fast:
            fast = fast.next
            prev = head
            head = head.next

        prev.next = head.next
        return dump.next
