from typing import Optional, List
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Helper function to build a tree from LeetCode's level-order array format
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = collections.deque([root])
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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def dfs(node: TreeNode):
            nonlocal diameter

            if not node.left and not node.right:
                return 1
            left_depth, right_depth = 0, 0
            if node.left:
                left_depth = dfs(node.left)
            if node.right:
                right_depth = dfs(node.right) 
            
            diameter = max(diameter, left_depth + right_depth)
            return max(left_depth,right_depth) + 1
        if not root:
            return 0
        dfs(root)
        return  diameter


# --- Test Suite ---
def run_tests():
    sol = Solution()

    test_cases = [
        # (Input array representation, Expected output, Description)
        ([1, 2, 3, 4, 5], 3, "Standard tree (Example 1)"),
        ([1, 2], 1, "Small tree (Example 2)"),
        ([1], 0, "Single node tree"),
        ([1, 2, None, 3, None, 4], 3, "Left-skewed linear tree"),
        ([1, None, 2, None, 3, None, 4], 3, "Right-skewed linear tree"),
        # Tree where diameter does not pass through the root:
        ([1, 2, 3, 4, 5, None, None, 6, None, 7, 8], 4, "Diameter bypasses the root"),
        ([4, -7, -3, None, None, -9, -3, 9, -7, -4, None, 6, None, -6, -6, None, None, 0, 6, 5, None, 9, None, None, -1, -4, None, None, None, -2], 8, "Complex large tree"),
    ]

    all_passed = True
    for i, (arr, expected, desc) in enumerate(test_cases, 1):
        root = build_tree(arr)
        result = sol.diameterOfBinaryTree(root)
        
        if result == expected:
            print(f"✅ Test {i} Passed: {desc}")
        else:
            print(f"❌ Test {i} Failed: {desc}")
            print(f"   Input array: {arr}")
            print(f"   Expected: {expected}, but got: {result}")
            all_passed = False

    print("-" * 30)
    if all_passed:
        print("🎉 All test cases passed!")
    else:
        print("⚠️ Some test cases failed. Review your logic.")


if __name__ == "__main__":
    run_tests()