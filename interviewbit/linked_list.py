from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def fill_linked_list(elements: List) -> ListNode:
    if not elements:
        return None

    head = ListNode(elements[0])
    current = head

    for value in elements[1:]:
        current.next = ListNode(value)
        current = current.next

    return head

def list_to_array(head):
    array = []

    while head:
        array.append(head.val)
        head = head.next

    return array


def remove_duplicate_node(head: ListNode):
    existed_nodes = set()
    new_head = head
    previous_node = head

    existed_nodes.add(head.val)

    while previous_node.next:
        current_node = previous_node.next

        if current_node.val in existed_nodes:
            previous_node.next = current_node.next
            continue

        existed_nodes.add(current_node.val)
        previous_node = current_node

    return new_head


if __name__ == '__main__':
    input_values = input().split()
    linked_list = fill_linked_list(input_values)
    result = remove_duplicate_node(linked_list)
    print(list_to_array(result))
