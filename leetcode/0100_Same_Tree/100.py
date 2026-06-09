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
    def isBalanced(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if (p and not q) or (not p and q):
            return False
        if (p.left and not q.left) or (not p.left and q.left):
            return False
        if (p.right and not q.right) or (not p.right and q.right):
            return False
        left = self.isBalanced(p.left, q.left)
        right = self.isBalanced(p.right, q.right)

        return left and right and (p.val == q.val)

# --- Test Suite ---
def run_tests():
    sol = Solution()

    test_cases = [
        # (Input array p, Input array q, Expected output, Description)
        ([1, 2, 3], [1, 2, 3], True, "Identical trees (Example 1)"),
        ([4, 7], [4, None, 7], False, "Same values, different structure (Example 2)"),
        ([1, 2, 3], [1, 3, 2], False, "Same structure, different values (Example 3)"),
        ([], [], True, "Both trees are empty"),
        ([], [1], False, "One tree is empty, the other is not"),
        ([1, 2], [1, None, 2], False, "Left child vs Right child"),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], True, "Larger identical trees"),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, None], False, "Larger trees with one missing node"),
    ]

    all_passed = True
    for i, (vals_p, vals_q, expected, desc) in enumerate(test_cases, 1):
        p = build_tree(vals_p)
        q = build_tree(vals_q)
        result = sol.isSameTree(p, q)
        
        if result == expected:
            print(f"✅ Test {i} Passed: {desc}")
        else:
            print(f"❌ Test {i} Failed: {desc}")
            print(f"   Input: p = {vals_p}, q = {vals_q}")
            print(f"   Expected: {expected}, but got: {result}")
            all_passed = False

    print("-" * 30)
    if all_passed:
        print("🎉 All test cases passed!")
    else:
        print("⚠️ Some test cases failed. Review your logic.")


if __name__ == "__main__":
    run_tests()