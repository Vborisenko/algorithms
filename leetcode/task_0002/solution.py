# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)


def to_int(node: ListNode):
    return node.val + 10 * (to_int(node.next)) if node.next else node.val


def to_list(n=148):
    node = ListNode(n % 10)
    if n > 9:
        node.next = to_list(n // 10)
    return node


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return to_list(to_int(l1) + to_int(l2))


if __name__ == '__main__':
    result = Solution().addTwoNumbers(to_list(342), to_list(465))
