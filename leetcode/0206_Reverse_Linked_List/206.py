from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Leave this empty for your implementation
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next :
            return head
        curr = head
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

            




# --- Helper Functions for Testing ---
def build_linked_list(arr: list[int]) -> Optional[ListNode]:
    """Converts a standard Python list into a ListNode linked list."""
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

def linked_list_to_list(head: Optional[ListNode]) -> list[int]:
    """Converts a ListNode linked list back into a standard Python list."""
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result


# --- Test Suite ---
def run_tests():
    sol = Solution()

    test_cases = [
        # (Input list representation, Expected reversed list representation, Description)
        ([0, 1, 2, 3], [3, 2, 1, 0], "Standard list (Example 1)"),
        ([], [], "Empty list (Example 2)"),
        ([1], [1], "Single element list"),
        ([1, 2], [2, 1], "Two element list"),
        ([-1, -2, -3], [-3, -2, -1], "List with negative values"),
        ([5, 5, 5, 5], [5, 5, 5, 5], "List with all identical elements"),
        ([10, 20, 30, 40, 50], [50, 40, 30, 20, 10], "Longer alternating list"),
    ]

    all_passed = True
    for i, (input_arr, expected_arr, desc) in enumerate(test_cases, 1):
        # 1. Build the linked list from the input array
        head = build_linked_list(input_arr)
        
        # 2. Run the solution
        result_head = sol.reverseList(head)
        
        # 3. Convert the resulting linked list back to an array for easy validation
        result_arr = linked_list_to_list(result_head)
        
        if result_arr == expected_arr:
            print(f"✅ Test {i} Passed: {desc}")
        else:
            print(f"❌ Test {i} Failed: {desc}")
            print(f"   Input: {input_arr}")
            print(f"   Expected: {expected_arr}, but got: {result_arr}")
            all_passed = False

    print("-" * 30)
    if all_passed:
        print("🎉 All test cases passed!")
    else:
        print("⚠️ Some test cases failed. Review your logic.")


if __name__ == "__main__":
    run_tests()