from typing import Optional


# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next




class Solution:

    def reorderList(self, head: ListNode | None ) -> None:
        """Do not return anything, modify head in-place instead."""
        if not head or head.next == None:
            return
        # Leave this empty for your implementation
        count = 0
        fast: ListNode | None = head
        slow: ListNode | None  = head
        while True:
            if fast and fast.next is None:
                break
            fast = fast.next
            if count % 2:
                slow = slow.next
            count += 1
        if slow and slow.next:
            temp = slow.next
            slow.next = None
            curr = temp
        else:
            return
        
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        curr = prev
        curr2 = head

        while curr:
            temp2 = curr2.next
            temp = curr.next
            curr2.next = curr
            curr.next = temp2
            curr2 = temp2
            curr = temp






# --- Helper Functions for Testing ---
def array_to_linked_list(arr: list[int]) -> Optional[ListNode]:
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head


def linked_list_to_array(head: Optional[ListNode]) -> list[int]:
    arr = []
    curr = head
    while curr:
        arr.append(curr.val)
        curr = curr.next
    return arr


# --- Test Suite ---
def run_tests():
    sol = Solution()

    test_cases = [
        # (Input list, Expected reordered list, Description)
        ([2, 4, 6, 8], [2, 8, 4, 6], "Even number of nodes (Example 1)"),
        ([2, 4, 6, 8, 10], [2, 10, 4, 8, 6], "Odd number of nodes (Example 2)"),
        ([1], [1], "Single node list"),
        ([1, 2], [1, 2], "Two nodes list"),
        ([1, 2, 3], [1, 3, 2], "Three nodes list"),
        ([1, 2, 3, 4, 5, 6], [1, 6, 2, 5, 3, 4], "Six nodes list"),
        (
            [10, 20, 30, 40, 50, 60, 70],
            [10, 70, 20, 60, 30, 50, 40],
            "Seven nodes list with larger values",
        ),
    ]

    all_passed = True
    for i, (input_arr, expected, desc) in enumerate(test_cases, 1):
        # Generate a fresh linked list for each test case
        head = array_to_linked_list(input_arr)

        sol.reorderList(head)
        result = linked_list_to_array(head)

        if result == expected:
            print(f"✅ Test {i} Passed: {desc}")
        else:
            print(f"❌ Test {i} Failed: {desc}")
            print(f"   Input: {input_arr}")
            print(f"   Expected: {expected}, but got: {result}")
            all_passed = False

    print("-" * 30)
    if all_passed:
        print("🎉 All test cases passed!")
    else:
        print("⚠️ Some test cases failed. Review your logic.")


if __name__ == "__main__":
    run_tests()