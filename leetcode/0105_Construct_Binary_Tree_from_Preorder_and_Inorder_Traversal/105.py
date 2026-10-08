from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Leave this empty for your implementation
class Solution:
    def _build_tree(self, pre_lo: int, pre_hi: int, in_lo: int, in_hi: int):
        n = len(self.preorder)
        if (
            pre_lo < 0
            or pre_lo >= n
            or pre_hi < 0
            or pre_hi >= n
            or in_lo < 0
            or in_lo >= n
            or in_hi >= n
            or in_hi < 0
            or in_lo > in_hi
            or pre_lo > pre_hi
        ):
            return None

        num = self.preorder[pre_lo]

        node = TreeNode(num)
        if pre_lo == pre_hi:
            return node
        in_num = self.inorder_index[num]
        left_len = in_num - in_lo
        right_len = in_hi - in_num
        if pre_lo == pre_hi:
            return node
        node.left = self._build_tree(pre_lo + 1, pre_lo + left_len, in_lo, in_num - 1)
        node.right = self._build_tree(pre_lo + left_len + 1, pre_hi, in_num + 1, in_hi)
        return node

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preorder = preorder
        self.inorder = inorder
        if not inorder:
            return None
        self.inorder_index = {x: i for i, x in enumerate(inorder)}
        self.preorder_index = {x: i for i, x in enumerate(preorder)}

        return self._build_tree(0, len(preorder) - 1, 0, len(preorder) - 1)

        pass


# --- Helper functions for testing and visualization ---


def print_tree(root: Optional[TreeNode]):
    """Renders binary tree structure using box-drawing branch connectors."""
    if not root:
        print("(Empty Tree)")
        return

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


def list_to_tree(arr: List[Optional[int]]) -> Optional[TreeNode]:
    """Builds a binary tree from a level-order list (LeetCode format)."""
    if not arr:
        return None

    root = TreeNode(arr[0])
    queue = [root]
    i = 1

    while queue and i < len(arr):
        curr = queue.pop(0)

        if i < len(arr) and arr[i] is not None:
            curr.left = TreeNode(arr[i])
            queue.append(curr.left)
        i += 1

        if i < len(arr) and arr[i] is not None:
            curr.right = TreeNode(arr[i])
            queue.append(curr.right)
        i += 1

    return root


def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    """Converts a binary tree back to a level-order list representation."""
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    while result and result[-1] is None:
        result.pop()

    return result


# --- Test Suite ---
def run_tests():
    sol = Solution()

    test_cases = [
        # (preorder, inorder, Expected output (as list), Description)
        (
            [3, 9, 20, 15, 7],
            [9, 3, 15, 20, 7],
            [3, 9, 20, None, None, 15, 7],
            "Standard tree (Example 1)",
        ),
        ([-1], [-1], [-1], "Single node (Example 2)"),
        (
            [1, 2, 3],
            [3, 2, 1],
            [1, 2, None, 3],
            "Left-skewed tree (only left children)",
        ),
        (
            [1, 2, 3],
            [1, 2, 3],
            [1, None, 2, None, 3],
            "Right-skewed tree (only right children)",
        ),
        (
            [1, 2, 4, 5, 3, 6, 7],
            [4, 2, 5, 1, 6, 3, 7],
            [1, 2, 3, 4, 5, 6, 7],
            "Full perfect binary tree",
        ),
        (
            [-3, -9, -20, -15, -7],
            [-9, -3, -15, -20, -7],
            [-3, -9, -20, None, None, -15, -7],
            "Tree with negative values",
        ),
        ([1, 2], [1, 2], [1, None, 2], "Two nodes (root and right child)"),
        ([1, 2], [2, 1], [1, 2], "Two nodes (root and left child)"),
    ]

    all_passed = True
    for i, (preorder, inorder, expected_list, desc) in enumerate(test_cases, 1):
        print(f"\n--- Running Test {i}: {desc} ---")

        # Build and print the original (expected) tree
        expected_tree = list_to_tree(expected_list)
        print("Expected Tree Structure:")
        print_tree(expected_tree)

        # Run user implementation
        result_tree = sol.buildTree(preorder, inorder)
        result_list = tree_to_list(result_tree)

        if result_list == expected_list:
            print(f"✅ Test {i} Passed")
        else:
            print(f"❌ Test {i} Failed")
            print(f"   Input: preorder = {preorder}, inorder = {inorder}")
            print(f"   Expected List: {expected_list}")
            print(f"   Got List:      {result_list}")
            print("\n   Your Tree Structure:")
            print_tree(result_tree)
            all_passed = False

    print("\n" + "-" * 30)
    if all_passed:
        print("🎉 All test cases passed!")
    else:
        print("⚠️ Some test cases failed. Review your logic.")


if __name__ == "__main__":
    run_tests()
