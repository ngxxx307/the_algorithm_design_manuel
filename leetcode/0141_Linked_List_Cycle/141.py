from typing import Optional


# Definition for singly-linked list.
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


# Leave this empty for your implementation
class Solution:

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        runnerA = head
        runnerB = head

        count = 0
        while True:
            if runnerA is None or runnerB is None:
                return False
            if count % 2:
                runnerB = runnerB.next
            runnerA = runnerA.next
            if runnerA == runnerB:
                return True
            count +=1


# --- Helper Function to Build Linked List with Cycles ---
def create_linked_list(arr: list[int], pos: int) -> Optional[ListNode]:
    if not arr:
        return None

    # Create all nodes
    nodes = [ListNode(val) for val in arr]

    # Link nodes sequentially
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    # Create the cycle if pos is valid
    if pos != -1 and 0 <= pos < len(nodes):
        nodes[-1].next = nodes[pos]

    return nodes[0]


# --- Test Suite ---
def run_tests():
    sol = Solution()

    test_cases = [
        # (Input array, Cycle index 'pos', Expected output, Description)
        ([3, 2, 0, -4], 1, True, "Cycle connects to the second node (Example 1)"),
        ([1, 2], 0, True, "Cycle connects back to the head (Example 2)"),
        ([1], -1, False, "Single node with no cycle (Example 3)"),
        ([], -1, False, "Empty linked list"),
        ([1], 0, True, "Single node cycling back to itself"),
        ([1, 2, 3, 4, 5], -1, False, "Linear list with no cycle"),
        ([1, 2, 3, 4, 5], 0, True, "Longer list cycling back to the head"),
        ([1, 2, 3, 4, 5, 6, 7], 3, True, "Cycle connects to a middle node"),
    ]

    all_passed = True
    for i, (arr, pos, expected, desc) in enumerate(test_cases, 1):
        # Build the linked list for the current test case
        head = create_linked_list(arr, pos)

        result = sol.hasCycle(head)
        if result == expected:
            print(f"✅ Test {i} Passed: {desc}")
        else:
            print(f"❌ Test {i} Failed: {desc}")
            print(f"   Input: list = {arr}, pos = {pos}")
            print(f"   Expected: {expected}, but got: {result}")
            all_passed = False

    print("-" * 40)
    if all_passed:
        print("🎉 All test cases passed!")
    else:
        print("⚠️ Some test cases failed. Review your logic.")


if __name__ == "__main__":
    run_tests()