from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Leave this empty for your implementation
class Solution:
    def reverse(self, head: ListNode, prevGroup:ListNode | None, k: int):
        curr = head
        temp = None
        flag = False
        prev = prevGroup

        for _ in range(k):
            if not curr:
                flag = True
                break
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        tail = prev
        if flag:
            prev = curr
            curr = tail
            while curr != prevGroup:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return head, temp, True
        
        return tail, temp, False
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        Dummy = ListNode(-999, head)
        start = head
        prevGroup = Dummy
        
        while start:
            tail, next, flag = self.reverse(start, prevGroup, k)
            if flag:
                return Dummy.next
            start.next = next
            prevGroup.next = tail
            prevGroup = start
            start = next
        return Dummy.next




# --- Helper Functions for Testing ---
def build_linked_list(arr: list) -> Optional[ListNode]:
    """Converts a Python list to a linked list."""
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head: Optional[ListNode]) -> list:
    """Converts a linked list back to a Python list for easy comparison."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


# --- Test Suite ---
def run_tests():
    sol = Solution()

    test_cases = [
        # (Input 'head' as Python list, Input 'k', Expected output as Python list, Description)
        # ([1, 2, 3, 4, 5, 6], 3, [3, 2, 1, 6, 5, 4], "Perfect multiples of k (Example 1)"),
        ([1, 2, 3, 4, 5], 3, [3, 2, 1, 4, 5], "Remaining nodes fewer than k (Example 2)"),
        ([1, 2, 3, 4, 5], 1, [1, 2, 3, 4, 5], "k = 1, list should remain unchanged"),
        ([1, 2, 3, 4, 5], 5, [5, 4, 3, 2, 1], "k equals the length of the list"),
        ([1, 2, 3, 4], 2, [2, 1, 4, 3], "Even length list with k=2"),
        ([1], 1, [1], "Single element list constraint boundary"),
        ([1, 2], 2, [2, 1], "Two elements, reversed completely"),
    ]

    all_passed = True
    for i, (raw_head, k, expected, desc) in enumerate(test_cases, 1):
        # Convert the raw Python list into an actual Linked List
        head_node = build_linked_list(raw_head)
        
        # Run the user's solution
        result_node = sol.reverseKGroup(head_node, k)
        
        # Convert the resulting Linked List back to a Python list to verify
        result = linked_list_to_list(result_node)

        if result == expected:
            print(f"✅ Test {i} Passed: {desc}")
        else:
            print(f"❌ Test {i} Failed: {desc}")
            print(f"   Input: head = {raw_head}, k = {k}")
            print(f"   Expected: {expected}, but got: {result}")
            all_passed = False

    print("-" * 30)
    if all_passed:
        print("🎉 All test cases passed!")
    else:
        print("⚠️ Some test cases failed. Review your logic.")


if __name__ == "__main__":
    run_tests()