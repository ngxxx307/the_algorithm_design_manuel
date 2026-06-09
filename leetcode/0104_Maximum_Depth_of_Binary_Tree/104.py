import unittest
from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# --- Helper Function for LeetCode Tree Representation ---
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    """Builds a binary tree from a level-order traversal list."""
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        curr = queue.popleft()
        if i < len(values) and values[i] is not None:
            curr.left = TreeNode(values[i])
            queue.append(curr.left)
        i += 1
        if i < len(values) and values[i] is not None:
            curr.right = TreeNode(values[i])
            queue.append(curr.right)
        i += 1
    return root


# Leave this empty for your implementation
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue: deque[tuple[TreeNode, int]] = deque([(root, 1)])
        max_depth = 0
        while queue:
            node, depth = queue.popleft()
            max_depth = max(max_depth, depth)
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
        return max_depth


# --- Test Suite ---
def run_tests():
    sol = Solution()

    test_cases = [
        # (Input list 'root', Expected depth, Description)
        ([1, 2, 3, None, None, 4], 3, "Standard tree with uneven depth (Example 1)"),
        ([], 0, "Empty tree (Example 2)"),
        ([3, 9, 20, None, None, 15, 7], 3, "Standard balanced tree"),
        ([1], 1, "Single node tree"),
        ([1, 2, None, 3, None, 4, None], 4, "Left-heavy linear tree"),
        ([1, None, 2, None, 3], 3, "Right-heavy linear tree"),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 4, "Complete binary tree"),
    ]

    all_passed = True
    for i, (val_list, expected, desc) in enumerate(test_cases, 1):
        # Convert list representation to actual TreeNodes
        root_node = build_tree(val_list)
        
        # Run user's solution
        result = sol.maxDepth(root_node)
        
        if result == expected:
            print(f"✅ Test {i} Passed: {desc}")
        else:
            print(f"❌ Test {i} Failed: {desc}")
            print(f"   Input: root = {val_list}")
            print(f"   Expected: {expected}, but got: {result}")
            all_passed = False

    print("-" * 30)
    if all_passed:
        print("🎉 All test cases passed!")
    else:
        print("⚠️ Some test cases failed. Review your logic.")


if __name__ == "__main__":
    run_tests()