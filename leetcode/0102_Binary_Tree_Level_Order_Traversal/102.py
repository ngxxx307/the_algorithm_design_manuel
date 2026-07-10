from typing import List, Optional
from collections import deque 

# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Helper function to build a tree from LeetCode's list representation
def build_tree(arr: List[Optional[int]]) -> Optional[TreeNode]:
    if not arr:
        return None

    root = TreeNode(arr[0])
    queue = [root]
    i = 1

    while queue and i < len(arr):
        curr = queue.pop(0)

        if curr:
            # Assign left child
            if i < len(arr) and arr[i] is not None:
                curr.left = TreeNode(arr[i])
                queue.append(curr.left)
            i += 1

            # Assign right child
            if i < len(arr) and arr[i] is not None:
                curr.right = TreeNode(arr[i])
                queue.append(curr.right)
            i += 1

    return root


# Leave this empty for your implementation
class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        Output = []
        queue = deque([(0, root)])

        while queue:
            level, node = queue.popleft()
            if (level) >= len(Output):
                Output.append([])
            Output[level].append(node.val)
            if node.left:
                queue.append((level + 1, node.left))
            if node.right:
                queue.append((level + 1, node.right))
        return Output


# --- Test Suite ---
def run_tests():
    sol = Solution()

    test_cases = [
        # (Input array, Expected level order list, Description)
        (
            [3, 9, 20, None, None, 15, 7],
            [[3], [9, 20], [15, 7]],
            "Standard balanced tree (Example 1)",
        ),
        ([1], [[1]], "Single node tree (Example 2)"),
        ([], [], "Empty tree (Example 3)"),
        (
            [1, 2, None, 3, None, 4, None, 5],
            [[1], [2], [3], [4], [5]],
            "Left-skewed tree (Deep linear structure)",
        ),
        (
            [1, None, 2, None, 3, None, 4, None, 5],
            [[1], [2], [3], [4], [5]],
            "Right-skewed tree",
        ),
        (
            [1, 2, 3, 4, 5, 6, 7],
            [[1], [2, 3], [4, 5, 6, 7]],
            "Perfect binary tree",
        ),
        (
            [-1000, 1000, -500],
            [[-1000], [1000, -500]],
            "Negative and boundary values",
        ),
        (
            [1, 2, 3, None, 4, 5, None],
            [[1], [2, 3], [4, 5]],
            "Asymmetric tree with missing outer children",
        ),
    ]

    all_passed = True
    for i, (arr, expected, desc) in enumerate(test_cases, 1):
        # Construct the tree structure from the flat array representation
        root = build_tree(arr)
        result = sol.levelOrder(root)

        if result == expected:
            print(f"✅ Test {i} Passed: {desc}")
        else:
            print(f"❌ Test {i} Failed: {desc}")
            print(f"   Input Tree Array: {arr}")
            print(f"   Expected: {expected}")
            print(f"   Got:      {result}")
            all_passed = False

    print("-" * 30)
    if all_passed:
        print("🎉 All test cases passed!")
    else:
        print("⚠️ Some test cases failed. Review your logic.")


if __name__ == "__main__":
    run_tests()
