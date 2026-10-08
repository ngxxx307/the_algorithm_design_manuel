from collections import deque
import math
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Helper function to build a binary tree from LeetCode level-order array
def build_tree(vals: List[Optional[int]]) -> Optional[TreeNode]:
    if not vals:
        return None
    root = TreeNode(vals[0])
    queue = deque([root])
    i = 1
    while queue and i < len(vals):
        node = queue.popleft()
        if i < len(vals) and vals[i] is not None:
            node.left = TreeNode(vals[i])
            queue.append(node.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            node.right = TreeNode(vals[i])
            queue.append(node.right)
        i += 1
    return root


def print_tree(root: TreeNode | None) -> str:
    """Renders binary tree structure using box-drawing branch connectors."""
    if not root:
        return ""
    lines: list[str] = []

    def walk(node: TreeNode, prefix: str, is_last: bool, is_root: bool) -> None:
        label = str(node.val)
        if is_root:
            lines.append(label)
            branch = ""
        else:
            connector = "└── " if is_last else "├── "
            lines.append(prefix + connector + label)
            branch = prefix + ("    " if is_last else "│   ")

        children = [c for c in (node.left, node.right) if c is not None]
        for i, child in enumerate(children):
            walk(child, branch, i == len(children) - 1, is_root=False)

    walk(root, prefix="", is_last=True, is_root=True)
    print("\n".join(lines))
    return

# Leave this empty for your implementation
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        curr_max = -math.inf

        def dfs(node: TreeNode):
            nonlocal curr_max
            if node.left:
                res = dfs(node.left)
                if res == False:
                    return False
            if curr_max >= node.val:
                return False
            curr_max = node.val

            if node.right:
                res = dfs(node.right)
                if res == False:
                    return False
            return True

        res = dfs(root)
        return res


# --- Test Suite ---
def run_tests():
    sol = Solution()

    test_cases = [
        # (Input level-order array, Expected output, Description)
        ([2, 1, 3], True, "Standard valid BST (Example 1)"),
        (
            [5, 1, 4, None, None, 3, 6],
            False,
            "Right child is smaller than parent (Example 2)",
        ),
        ([1], True, "Single node tree"),
        ([2, 2, 2], False, "Duplicate values violate strict inequality"),
        (
            [5, 4, 6, None, None, 3, 7],
            False,
            "Node in right subtree is smaller than root (3 < 5)",
        ),
        (
            [10, 5, 15, None, None, 6, 20],
            False,
            "Deep node in right subtree violates root lower bound",
        ),
        ([2147483647], True, "Single node with 32-bit MAX_INT value"),
        (
            [-2147483648, None, 2147483647],
            True,
            "Tree spanning 32-bit MIN_INT to MAX_INT",
        ),
        ([1, 1], False, "Left child equals parent value"),
    ]

    all_passed = True
    for i, (tree_list, expected, desc) in enumerate(test_cases, 1):
        root = build_tree(tree_list)
        # print_tree(root)
        result = sol.isValidBST(root)

        if result == expected:
            print(f"✅ Test {i} Passed: {desc}")
        else:
            print(f"❌ Test {i} Failed: {desc}")
            print(f"   Input Tree: {tree_list}")
            print(f"   Expected: {expected}, but got: {result}")
            all_passed = False

    print("-" * 30)
    if all_passed:
        print("🎉 All test cases passed!")
    else:
        print("⚠️ Some test cases failed. Review your logic.")


if __name__ == "__main__":
    run_tests()
