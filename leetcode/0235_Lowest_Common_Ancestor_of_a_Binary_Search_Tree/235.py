class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# --- Helper Functions for Test Setup ---
def build_tree(vals: list) -> TreeNode | None:
    """Builds a binary tree from a LeetCode level-order array representation."""
    if not vals:
        return None
    root = TreeNode(vals[0])
    queue = [root]
    i = 1
    while queue and i < len(vals):
        curr = queue.pop(0)
        if i < len(vals) and vals[i] is not None:
            curr.left = TreeNode(vals[i])
            queue.append(curr.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            curr.right = TreeNode(vals[i])
            queue.append(curr.right)
        i += 1
    return root


def find_node(root: TreeNode | None, val: int) -> TreeNode | None:
    """Finds and returns the node object matching `val` in the binary tree."""
    if not root:
        return None
    if root.val == val:
        return root
    return find_node(root.left, val) or find_node(root.right, val)


def dfs(
    node: TreeNode, p: TreeNode, q: TreeNode
) -> tuple[TreeNode | None, TreeNode | None, TreeNode | None]:
    left_p, left_q, right_p, right_q, left_common, right_common = (
        None,
        None,
        None,
        None,
        None,
        None,
    )
    if node.left:
        left_p, left_q, left_common = dfs(node.left, p, q)
    if node.right:
        right_p, right_q, right_common = dfs(node.right, p, q)

    if left_common:
        return left_p, left_q, left_common
    if right_common:
        return right_p, right_q, right_common

    target_p = None
    target_p = left_p if left_p else target_p
    target_p = right_p if right_p else target_p
    target_p = node if node == p else target_p

    target_q = None
    target_q = left_q if left_q else target_q
    target_q = right_q if right_q else target_q
    target_q = node if node == q else target_q

    common = None
    common = node if target_p and target_q else common

    return target_p, target_q, common


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
    return "\n".join(lines)


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        # Write your LCA logic here
        _, _, common = dfs(root, p, q)
        return common


# --- Test Suite ---
def run_tests():
    sol = Solution()

    test_cases = [
        # (Tree Array, p Value, q Value, Expected LCA Value, Description)
        (
            [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4],
            5,
            1,
            3,
            "Standard LCA: nodes in separate subtrees (Example 1)",
        ),
        (
            [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4],
            5,
            4,
            5,
            "Ancestor node: p is ancestor of q (Example 2)",
        ),
        (
            [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4],
            7,
            4,
            2,
            "Deep LCA: both target nodes are deep in left subtree",
        ),
        (
            [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4],
            0,
            8,
            1,
            "Right subtree: both nodes reside in right subtree",
        ),
        ([1, 2], 1, 2, 1, "Two-node tree: root is p (Example 3)"),
        ([1, 2, 3], 2, 3, 1, "Simple balanced 3-node tree"),
        ([1, 2, None, 3, None, 4], 3, 4, 3, "Skewed tree (linear path)"),
    ]

    all_passed = True
    for i, (tree_arr, p_val, q_val, expected_val, desc) in enumerate(test_cases, 1):
        print(f"\n==================== Test Case {i}: {desc} ====================")
        root = build_tree(tree_arr)
        p = find_node(root, p_val)
        q = find_node(root, q_val)

        print("Tree Structure:")
        t = print_tree(root)
        print(t)
        print(f"Target Nodes: p = {p_val}, q = {q_val}")

        result_node = sol.lowestCommonAncestor(root, p, q)
        result_val = result_node.val if result_node else None

        if result_val == expected_val:
            print(f"Result: ✅ Passed (LCA = {result_val})")
        else:
            print(
                f"Result: ❌ Failed (Expected LCA = {expected_val}, got = {result_val})"
            )
            all_passed = False

    print("\n" + "=" * 50)
    if all_passed:
        print("🎉 All test cases passed!")
    else:
        print("⚠️ Some test cases failed. Review your logic.")


if __name__ == "__main__":
    run_tests()
