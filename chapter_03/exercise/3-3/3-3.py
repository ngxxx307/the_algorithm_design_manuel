import unittest

# 1. The Data Structure
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next : ListNode | None= next

# 2. Your Solution Placeholders
def reverse_list(head: ListNode | None) -> ListNode | None:
    """
    Args:
        head: The first node of the singly linked list.
    Returns:
        The new head of the reversed list.
    """
    # TODO: Implement your linear time algorithm here.
    if not head:
        return
    prev = None
    curr = head
    Next = None
    while curr:
        Next = curr.next
        curr.next = prev
        prev = curr
        curr = Next
        
    return prev 

# 3. The Test Suite
class TestReverseLinkedList(unittest.TestCase):

    # Helper: Converts a Python list [1,2,3] into a Linked List 1->2->3
    def create_linked_list(self, elements):
        if not elements:
            return None
        head = ListNode(elements[0])
        current = head
        for val in elements[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    # Helper: Converts a Linked List back to a Python list for easy comparison
    def linked_list_to_list(self, head):
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
            # Safety break for infinite loops (common bug in reversal)
            if len(result) > 1000: 
                raise RuntimeError("Infinite loop detected! Tail next pointer not cleared.")
        return result

    def test_example_case_multiple_nodes(self):
        # Input: 1 -> 2 -> 3 -> 4 -> 5
        head = self.create_linked_list([1, 2, 3, 4, 5])
        
        # Execute
        new_head = reverse_list(head)
        
        # Verify: Should be 5 -> 4 -> 3 -> 2 -> 1
        result = self.linked_list_to_list(new_head)
        self.assertEqual(result, [5, 4, 3, 2, 1])

    def test_single_node(self):
        # Input: 1
        head = self.create_linked_list([1])
        
        # Execute
        new_head = reverse_list(head)
        
        # Verify: Should be 1
        result = self.linked_list_to_list(new_head)
        self.assertEqual(result, [1])

    def test_empty_list(self):
        # Input: None
        head = None
        
        # Execute
        new_head = reverse_list(head)
        
        # Verify: Should be None (empty list)
        self.assertIsNone(new_head)

    def test_two_nodes(self):
        # Input: 1 -> 2
        head = self.create_linked_list([1, 2])
        
        # Execute
        new_head = reverse_list(head)
        
        # Verify: Should be 2 -> 1
        result = self.linked_list_to_list(new_head)
        self.assertEqual(result, [2, 1])

if __name__ == '__main__':
    unittest.main()