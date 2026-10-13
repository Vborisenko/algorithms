# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        dump = ListNode(next=head)
        prev = dump
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            prev = prev.next

        l1 = head
        l2 = slow
        prev.next = None

        l1 = self.sortList(l1)
        l2 = self.sortList(l2)
        dump = ListNode(next=head)
        prev = dump
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        prev.next = l1 if l1 else l2
        return dump.next