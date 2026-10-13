# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)


def to_list(n):
    node = ListNode(n % 10)
    if n > 9:
        node.next = to_list(n // 10)
    return node


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        1) Define the length of the l-list
        2) Calculate how many times k nodes could be reversed (times)
        3) reverse with decreasing times count
        """

        length = 0
        current = head

        while current:
            length += 1
            current = current.next

        dump = ListNode(next=head)
        prev = dump
        reverse_head = None
        reverse_end = head
        times = length // k
        i = 0
        while times > 0:
            if i and i % k or i == 0:
                next_ = head.next
                head.next = reverse_head
                reverse_head = head
                head = next_
            else:
                times -= 1
                prev.next = reverse_head
                reverse_end.next = head
                prev = reverse_end
                if head:
                    next_ = head.next
                    head.next = None
                reverse_end = head
                reverse_head = head
                if head:
                    head = next_
            i += 1

        if head:
            reverse_end.next = head

        return dump.next


if __name__ == '__main__':
    ll = to_list(21)
    Solution().reverseKGroup(ll, 2)