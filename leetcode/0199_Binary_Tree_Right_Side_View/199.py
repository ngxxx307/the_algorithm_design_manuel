from collections import deque
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


from collections import deque


# Leave this empty for your implementation
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        view = []
        queue = deque([root])
        while queue:
            view.append(queue[-1].val)
            new_queue = deque([])
            while queue:
                node = queue.popleft()
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)
            queue = new_queue
        return view

def print_tree(root: TreeNode | None):
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


# --- Test Suite ---
def run_tests():
    sol = Solution()

    test_cases = [
        # (Input level-order array, Expected output list, Description)
        ([1, 2, 3, None, 5, None, 4], [1, 3, 4], "Standard binary tree (Example 1)"),
        (
            [1, 2, 3, 4, None, None, None, 5],
            [1, 3, 4, 5],
            "Left branch extends deeper (Example 2)",
        ),
        ([1, None, 3], [1, 3], "Right-skewed tree (Example 3)"),
        ([], [], "Empty tree (Example 4)"),
        ([1], [1], "Single node tree"),
        ([1, 2], [1, 2], "Root with only a left child"),
        (
            [1, 2, 3, None, 5, 6, None, 4],
            [1, 3, 6, 4],
            "Left subtree extends below right subtree",
        ),
        (
            [-10, -20, 0, None, -5],
            [-10, 0, -5],
            "Tree containing negative and zero values",
        ),
        ([1, 2, 2, 3, 4, 4, 3], [1, 2, 3], "Symmetric full binary tree"),
        (
            [0, 1, 2, None, 3, 4, None, None, 5, 9, None, None, 6, 10, None],
            [0, 2, 4, 9, 10],
            "Complex multi-level asymmetric tree",
        ),
    ]

    all_passed = True
    for i, (tree_list, expected, desc) in enumerate(test_cases, 1):
        root = build_tree(tree_list)
        print_tree(root)
        result = sol.rightSideView(root)
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
