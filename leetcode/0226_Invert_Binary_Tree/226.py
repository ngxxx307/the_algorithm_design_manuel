import unittest
from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# --- Helper Functions for LeetCode Tree Representation ---
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

def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    """Converts a binary tree to a level-order traversal list."""
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        curr = queue.popleft()
        if curr:
            result.append(curr.val)
            queue.append(curr.left)
            queue.append(curr.right)
        else:
            result.append(None)
    # Strip trailing Nones to match LeetCode's exact output format
    while result and result[-1] is None:
        result.pop()
    return result


# Leave this empty for your implementation
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        queue: deque[TreeNode] = deque()
        queue.append(root)

        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root




# --- Test Suite ---
def run_tests():
    sol = Solution()

    test_cases = [
        # (Input list 'root', Expected output list, Description)
        ([1, 2, 3, 4, 5, 6, 7], [1, 3, 2, 7, 6, 5, 4], "Standard balanced tree (Example 1)"),
        ([3, 2, 1], [3, 1, 2], "Three-node tree (Example 2)"),
        ([], [], "Empty tree (Example 3)"),
        ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1], "Classic full binary tree"),
        ([1], [1], "Single node tree"),
        ([1, 2], [1, None, 2], "Left child only becomes right child only"),
        ([1, None, 2], [1, 2], "Right child only becomes left child only"),
        ([1, 2, None, 3], [1, None, 2, None, 3], "Unbalanced left-heavy tree inverted"),
    ]

    all_passed = True
    for i, (val_list, expected, desc) in enumerate(test_cases, 1):
        # Convert list representation to actual TreeNodes
        root_node = build_tree(val_list)
        
        # Run user's solution
        result_node = sol.invertTree(root_node)
        
        # Convert resulting TreeNodes back to list for comparison
        result = tree_to_list(result_node)
        
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