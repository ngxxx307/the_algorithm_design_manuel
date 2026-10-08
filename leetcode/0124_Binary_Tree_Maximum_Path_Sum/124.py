from collections import deque
import math
from typing import Optional, List


# Standard LeetCode TreeNode definition
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Helper function to build a binary tree from a level-order list
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        # Left child
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        # Right child
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root


def print_tree(root: Optional[TreeNode]):
    """Renders binary tree with L/R labels so a lone child is unambiguous."""
    if not root:
        print("(Empty Tree)")
        return

    lines: list[str] = []

    def walk(
        node: TreeNode, prefix: str, is_last: bool, is_root: bool, side: str
    ) -> None:
        label = f"{side}: {node.val}" if side else str(node.val)
        if is_root:
            lines.append(label)
            branch = ""
        else:
            connector = "└── " if is_last else "├── "
            lines.append(prefix + connector + label)
            branch = prefix + ("    " if is_last else "│   ")

        present = [
            (c, s) for c, s in ((node.left, "L"), (node.right, "R")) if c is not None
        ]
        for i, (child, s) in enumerate(present):
            walk(child, branch, i == len(present) - 1, False, s)

    walk(root, "", True, True, "")
    print("\n".join(lines))


# Leave this empty for your implementation
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maximum = -math.inf

        def dfs(node: TreeNode) -> int:
            nonlocal maximum
            node_max, left_max, right_max = 0, 0, 0
            if node.left:
                left_max = dfs(node.left)
            if node.right:
                right_max = dfs(node.right)
            node_max = max(right_max + node.val, left_max + node.val, node.val)
            maximum = max(maximum, node_max, left_max + node.val + right_max)
            return node_max

        if not root:
            return 0
        dfs(root)
        return maximum


# --- Test Suite ---
def run_tests():
    sol = Solution()

    # Including standard examples, edge cases, and popular discussion test cases
    test_cases = [
        # (Input array, Expected output, Description)
        ([1, 2, 3], 6, "Standard positive tree (Example 1)"),
        (
            [-10, 9, 20, None, None, 15, 7],
            42,
            "Mixed values with larger right subtree (Example 2)",
        ),
        ([-3], -3, "Single negative node"),
        ([2, -1], 2, "Path is just the root (ignore negative child)"),
        ([2, -1, -2], 2, "Path is just the root (ignore both negative children)"),
        ([1, -2, 3], 4, "Skip negative left branch, take root + right branch"),
        (
            [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1],
            48,
            "Complex tree (Discussion favorite)",
        ),
        ([-10, -20, -30], -10, "All negative nodes (must take least negative node)"),
        ([1, 2, None, 3, None, 4, None, 5], 15, "Unbalanced right-heavy tree"),
    ]

    all_passed = True
    for i, (values, expected, desc) in enumerate(test_cases, 1):
        root = build_tree(values)
        result = sol.maxPathSum(root)
        print_tree(root)

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
