from typing import List, Optional


# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# --- Placeholder for your implementation ---
class Solution:

    def removeNthFromEnd(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        fast = head
        for i in range(n):
            fast = fast.next
        
        prev = None
        slow = head
        while fast:
            fast = fast.next
            prev = slow
            slow = slow.next

        if prev:
            prev.next = slow.next
            slow.next = None
            return head
        else:
            return slow.next
        



# --- Helper Functions for Linked Lists ---
def build_linked_list(arr: List[int]) -> Optional[ListNode]:
    """Converts a Python list into a ListNode linked list."""
    if not arr:
        return None
    dummy = ListNode(0)
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


def linked_list_to_python_list(head: Optional[ListNode]) -> List[int]:
    """Converts a ListNode linked list back into a standard Python list."""
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
        # (Input list, n, Expected output list, Description)
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5], "Remove from near the end (Example 1)"),
        ([1], 1, [], "Single element list, remove sole node (Example 2)"),
        ([1, 2], 1, [1], "Two elements, remove the tail node (Example 3)"),
        ([1, 2], 2, [2], "Two elements, remove the head node"),
        ([1, 2, 3], 3, [2, 3], "Three elements, remove the head node"),
        ([10, 20, 30, 40], 1, [10, 20, 30], "Remove the absolute last node"),
        ([0, 100, 50], 2, [0, 50], "Verify with constraint boundary values (0, 100)"),
        (
            list(range(1, 31)),
            30,
            list(range(2, 31)),
            "Max constraint limit (sz = 30), remove the head",
        ),
    ]

    all_passed = True
    for i, (input_arr, n, expected, desc) in enumerate(test_cases, 1):
        # Generate a fresh linked list for each test run
        head = build_linked_list(input_arr)

        # Execute the user solution
        res_node = sol.removeNthFromEnd(head, n)

        # Convert result back to list for easy comparison
        result = linked_list_to_python_list(res_node)

        if result == expected:
            print(f"✅ Test {i} Passed: {desc}")
        else:
            print(f"❌ Test {i} Failed: {desc}")
            print(f"   Input: head = {input_arr}, n = {n}")
            print(f"   Expected: {expected}, but got: {result}")
            all_passed = False

    print("-" * 30)
    if all_passed:
        print("🎉 All test cases passed!")
    else:
        print("⚠️ Some test cases failed. Review your logic.")


if __name__ == "__main__":
    run_tests()