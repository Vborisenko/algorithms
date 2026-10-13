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


class Solution1:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return to_list(to_int(l1) + to_int(l2))


class Solution:
    @staticmethod
    def _get_number_from_listnode(l_node) -> int:
        result_number = []

        while l_node:
            result_number.append(str(l_node.val))
            l_node = l_node.next

        result_number.reverse()
        return int("".join(result_number))

    @staticmethod
    def _get_listnode_from_number(number) -> ListNode:
        dump = ListNode(None)
        prev = dump
        for digit in str(number)[-1::-1]:
            current = ListNode(int(digit))
            prev.next = current
            prev = current
        return dump.next

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not all((l1.val, l2.val)):
            return l1 if l1.val else l2

        number1 = self._get_number_from_listnode(l1)
        number2 = self._get_number_from_listnode(l2)
        result_number = number1 + number2
        return self._get_listnode_from_number(result_number)


if __name__ == '__main__':
    l1 = to_list(753865680)
    l2 = to_list(798580876)
    # result = Solution().addTwoNumbers(to_list(342), to_list(465))
    result = Solution().addTwoNumbers(l1, l2)
