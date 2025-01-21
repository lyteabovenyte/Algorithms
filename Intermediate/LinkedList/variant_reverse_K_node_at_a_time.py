'''
    Given a linkedlist and a nonnegative integer k, reverse the list k nodes at a time, 
    if k is not a multiply of n, leave the last n mod k nodes unchanged.
'''

from ListNode import ListNode, create_linked_list, print_linked_list

def reverse_k_nodes(head, k):
    if not head or k <= 1:
        return head

    # Helper function to reverse a segment of the linked list.
    # inclusive on the start node, exclusive on the end node.
    def reverse_segment(start, end):
        prev, current = None, start
        while current != end:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

    dummy = ListNode(0)  # Dummy node to simplify edge cases.
    dummy.next = head
    group_prev = dummy

    while True:
        # Identify the start and end of the current group to reverse.
        kth = group_prev
        for _ in range(k):
            kth = kth.next
            if not kth:
                return dummy.next  # If fewer than k nodes, return as is.

        group_start = group_prev.next
        group_end = kth.next

        # Reverse the current group.
        reverse_segment(group_start, group_end)

        # Connect the reversed group back to the main list.
        group_prev.next = kth
        group_start.next = group_end

        # Move to the next group.
        group_prev = group_start


values = [1, 2, 3, 4, 5, 6, 7, 8]
k = 3
head = create_linked_list(values)
print("Original list:")
print_linked_list(head)

reversed_head = reverse_k_nodes(head, k)
print(f"List after reversing in groups of {k}:")
print_linked_list(reversed_head)
