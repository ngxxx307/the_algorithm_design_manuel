from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Helper function to build a binary tree from LeetCode's level-order list format
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(values):
        current = queue.popleft()
        
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
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalance = True
        def dfs(node: TreeNode):
            nonlocal isBalance
            if not node.left and not node.right:
                return 1
            left_depth, right_depth = 0, 0
            if node.left:
                left_depth = dfs(node.left)
            if node.right:
                right_depth = dfs(node.right) 

            if abs(left_depth - right_depth) > 1:
                isBalance = False
            return max(left_depth,right_depth) + 1
        if not root:
            return True
        dfs(root)
        return isBalance


# --- Test Suite ---
def run_tests():
    sol = Solution()

    test_cases = [
        # (Input array representing tree, Expected output, Description)
        ([1, 2, 3, None, None, 4], True, "Standard balanced tree (Example 1)"),
        ([1, 2, 3, None, None, 4, None, 5], False, "Unbalanced right subtree (Example 2)"),
        ([], True, "Empty tree (Example 3)"),
        ([1, 2, 2, 3, 3, None, None, 4, 4], False, "Deeply unbalanced tree"),
        ([1], True, "Single node tree"),
        ([1, 2, None, 3, None, 4], False, "Left-heavy straight line"),
        ([1, None, 2, None, 3], False, "Right-heavy straight line"),
        ([1, 2, 3, 4, 5, 6, None, 8], True, "Larger balanced tree"),
    ]

    all_passed = True
    for i, (values, expected, desc) in enumerate(test_cases, 1):
        root = build_tree(values)
        result = sol.isBalanced(root)
        
        if result == expected:
            print(f"✅ Test {i} Passed: {desc}")
        else:
            print(f"❌ Test {i} Failed: {desc}")
            print(f"   Input: root = {values}")
            print(f"   Expected: {expected}, but got: {result}")
            all_passed = False

    print("-" * 30)
    if all_passed:
        print("🎉 All test cases passed!")
    else:
        print("⚠️ Some test cases failed. Review your logic.")


if __name__ == "__main__":
    run_tests()