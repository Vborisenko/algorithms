# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or head.next is None:
            return False

        list_ids, i = list(), 0

        while head.next:
            if id(head.next) in list_ids:
                return True
            else:
                list_ids.append(id(head.next))

            head = head.next

        return False


if __name__ == '__main__':
    Solution.hasCycle()