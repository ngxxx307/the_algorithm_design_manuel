from typing import List, Optional


# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head = ListNode()
        curr =head
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10

            curr.next = ListNode(total % 10)
            curr = curr.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return head.next


# --- Helper Functions for Testing ---
def list_to_linkedlist(arr: List[int]) -> Optional[ListNode]:
    if not arr:
        return None
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next


def linkedlist_to_list(node: Optional[ListNode]) -> List[int]:
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res


# --- Test Suite ---
def run_tests():
    sol = Solution()

    test_cases = [
        # (l1_list, l2_list, expected_list, Description)
        ([2, 4, 3], [5, 6, 4], [7, 0, 8], "Standard addition (Example 1)"),
        ([0], [0], [0], "Both inputs are zero (Example 2)"),
        (
            [9, 9, 9, 9, 9, 9, 9],
            [9, 9, 9, 9],
            [8, 9, 9, 9, 0, 0, 0, 1],
            "Vastly different lengths with cascading carry (Example 3)",
        ),
        ([0], [1, 2, 3], [1, 2, 3], "Adding zero to a multi-digit number"),
        ([5], [5], [0, 1], "Single digits resulting in a carry-over digit"),
        (
            [9, 9],
            [1],
            [0, 0, 1],
            "Carry propagates through all digits to create a new node",
        ),
        ([1], [2], [3], "Single digits with no carry"),
        (
            [2, 4, 9],
            [5, 6, 4, 9],
            [7, 0, 4, 0, 1],
            "Unequal list lengths with multiple carries",
        ),
    ]

    all_passed = True
    for i, (l1_arr, l2_arr, expected, desc) in enumerate(test_cases, 1):
        # Convert plain lists to LinkedList structures for the solution
        l1 = list_to_linkedlist(l1_arr)
        l2 = list_to_linkedlist(l2_arr)

        result_node = sol.addTwoNumbers(l1, l2)

        # Convert result back to a plain list for verification
        result = linkedlist_to_list(result_node)

        if result == expected:
            print(f"✅ Test {i} Passed: {desc}")
        else:
            print(f"❌ Test {i} Failed: {desc}")
            print(f"   Input: l1 = {l1_arr}, l2 = {l2_arr}")
            print(f"   Expected: {expected}, but got: {result}")
            all_passed = False

    print("-" * 30)
    if all_passed:
        print("🎉 All test cases passed!")
    else:
        print("⚠️ Some test cases failed. Review your logic.")


if __name__ == "__main__":
    run_tests()