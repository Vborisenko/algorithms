# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        id_set = set()

        while headA:
            id_set.add(id(headA))
            headA = headA.next

        while headB:
            if id(headB) in id_set:
                return headB

            headB = headB.next
