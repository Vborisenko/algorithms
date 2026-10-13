from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        We are crating dump pointer to store the head of the list.
        prev is a refference to a previous node.
        current is a reff to a current node.

        The goal is to iterate through the list and check
        if the current.val equals prev.val and if yes, we have to move pointer to the current.next
        """
        dump = ListNode(None, head)
        [None, 1, 2, 2, 3, 3, 4, 5]
        current = head
        prev = dump

        while current:
            if current.val == dump.val:
                prev.next = current.next
                current = current.next
            else:
                prev = current
                current = current.next

        return dump.next

if __name__ == '__main__':
    head0 = ListNode(1)
    head1 =  ListNode(2)
    head0.next = head1
    head2 = ListNode(2)
    head1.next = head2
    head3 = ListNode(3)
    head2.next = head3
    Solution().deleteDuplicates(head0)