from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Helper function to build a tree from a LeetCode-style level-order list
def build_tree(values: list[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None

    root = TreeNode(values[0])
    queue = [root]
    i = 1

    while queue and i < len(values):
        current = queue.pop(0)

        # Left child
        if i < len(values) and values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1

        # Right child
        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1

    return root


# Leave this empty for your implementation
from collections import deque


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([(root, 1)])
        max_depth = 0
        while queue:
            node, d = queue.popleft()
            max_depth = max(max_depth, d)
            if node.left:
                queue.append((node.left, d + 1))
            if node.right:
                queue.append((node.right, d + 1))
        return max_depth


# --- Test Suite ---
def run_tests():
    sol = Solution()

    test_cases = [
        # (Input array representation of tree, Expected output, Description)
        ([1, 2, 3, None, None, 4], 3, "Standard tree with uneven depths (Example 1)"),
        ([], 0, "Empty tree (Example 2)"),
        ([1], 1, "Single root node"),
        ([1, 2, 3, 4, 5, 6, 7], 3, "Perfectly balanced binary tree"),
        ([1, 2, None, 3, None, 4, None, 5], 5, "Left-heavy tree (Linked List style)"),
        ([1, None, 2, None, 3, None, 4], 4, "Right-heavy tree (Linked List style)"),
        ([3, 9, 20, None, None, 15, 7], 3, "Standard LeetCode example tree"),
    ]

    all_passed = True
    for i, (tree_list, expected, desc) in enumerate(test_cases, 1):
        root = build_tree(tree_list)
        result = sol.maxDepth(root)

        if result == expected:
            print(f"✅ Test {i} Passed: {desc}")
        else:
            print(f"❌ Test {i} Failed: {desc}")
            print(f"   Input: root = {tree_list}")
            print(f"   Expected: {expected}, but got: {result}")
            all_passed = False

    print("-" * 30)
    if all_passed:
        print("🎉 All test cases passed!")
    else:
        print("⚠️ Some test cases failed. Review your logic.")


if __name__ == "__main__":
    run_tests()
