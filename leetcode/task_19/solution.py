from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val} -> {self.next}'


def array_to_linked_list(array: list) -> ListNode:
    if array:
        head = current = ListNode(val=array[0], next=None)

        for i in range(1, len(array)):
            next_ = ListNode(val=array[i])
            current.next = next_
            current = next_

        return head
    return ListNode(None, None)


class Solution:
    @staticmethod
    def remove_nth_from_start(head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.val or not head.next:
            return ListNode()

        if n == 1:
            return head.next

        new_head = current = ListNode(head.val)
        counter = 1

        while head.next:
            counter += 1
            head = head.next

            if counter != n:
                current.next = ListNode(head.val)
                current = current.next

        return new_head

    @staticmethod
    def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n == 1 and not head.next:
            return None

        if not head or not head.val:
            return ListNode()

        node_counter = 0
        new_head = current = None
        head_duplicate = ListNode(head.val, head.next)
        head = head.next

        while head_duplicate:
            node_counter += 1

            if node_counter > n:
                if not head:
                    head_duplicate = head_duplicate.next

                if not new_head:
                    new_head = current = ListNode(val=head_duplicate.val)
                    head_duplicate = head_duplicate.next

                if head_duplicate:
                    next_ = ListNode(val=head_duplicate.val)
                    current.next = next_
                    current = next_
                    head_duplicate = head_duplicate.next

            if head:
                head = head.next

        return new_head


if __name__ == '__main__':
    head = array_to_linked_list(array=[1,2,3,4,5])
    result = Solution.remove_nth_from_end(head=head, n=2)
    print(result)
