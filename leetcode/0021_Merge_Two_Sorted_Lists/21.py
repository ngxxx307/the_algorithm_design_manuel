from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        if not curr1:
            return curr2
        if not curr2:
            return curr1

        if curr2.val < curr1.val:
            head = curr2
            prev = curr2
            curr2 = curr2.next
        else:
            head = curr1
            prev = curr1
            curr1 = curr1.next        

        while curr1 and curr2:
            if curr2.val < curr1.val:
                prev.next = curr2
                prev = curr2
                curr2 = curr2.next
            else:
                prev.next = curr1
                prev = curr1
                curr1 = curr1.next
        if not curr1:
            prev.next = curr2
        else:
            prev.next = curr1

        return head

        

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
        # (Input list1 representation, Input list2 representation, Expected merged list representation, Description)
        ([1, 2, 4], [1, 3, 5], [1, 1, 2, 3, 4, 5], "Standard overlapping lists (Example 1)"),
        ([], [1, 2], [1, 2], "First list empty (Example 2)"),
        ([], [], [], "Both lists empty (Example 3)"),
        ([1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6], "All elements in list1 smaller than list2"),
        ([5, 6, 7], [1, 2], [1, 2, 5, 6, 7], "All elements in list2 smaller than list1"),
        ([2], [1], [1, 2], "Single elements out of order"),
        ([-10, -5, 0], [-7, 2], [-10, -7, -5, 0, 2], "Lists with negative values"),
    ]

    all_passed = True
    for i, (arr1, arr2, expected_arr, desc) in enumerate(test_cases, 1):
        # 1. Build the linked lists from the input arrays
        l1 = build_linked_list(arr1)
        l2 = build_linked_list(arr2)
        
        # 2. Run the solution
        result_head = sol.mergeTwoLists(l1, l2)
        
        # 3. Convert the resulting linked list back to an array for validation
        result_arr = linked_list_to_list(result_head)
        
        if result_arr == expected_arr:
            print(f"✅ Test {i} Passed: {desc}")
        else:
            print(f"❌ Test {i} Failed: {desc}")
            print(f"   Input: list1 = {arr1}, list2 = {arr2}")
            print(f"   Expected: {expected_arr}, but got: {result_arr}")
            all_passed = False

    print("-" * 30)
    if all_passed:
        print("🎉 All test cases passed!")
    else:
        print("⚠️ Some test cases failed. Review your logic.")


if __name__ == "__main__":
    run_tests()