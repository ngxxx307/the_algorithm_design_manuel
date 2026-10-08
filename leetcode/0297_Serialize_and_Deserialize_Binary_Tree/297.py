import collections


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


import io


# Leave this empty for your implementation
class Codec:
    def serialize(self, root: TreeNode) -> str:
        builder = io.StringIO()

        def dfs(node: TreeNode, dir: str):
            nonlocal builder
            builder.write(f"{dir}{node.val}")
            if node.left:
                dfs(node.left, "L")
            if node.right:
                dfs(node.right, "R")
            builder.write("B")
            return

        """Encodes a tree to a single string."""
        dfs(root, "")
        result = builder.getvalue()
        return result

    def deserialize(self, data: str) -> TreeNode:
        string = ""
        direction = "L"
        dummy_root = TreeNode(0)
        stack: list[TreeNode] = [dummy_root]
        for c in data:
            match c:
                case "L" | "R" | "B":
                    if string:
                        new_node = TreeNode(int(string))
                        if direction == "L":
                            stack[-1].left = new_node
                        else:
                            stack[-1].right = new_node
                        stack.append(new_node)
                        string = ""
                    if c == "B":
                        stack.pop()
                    direction = c
                case _:
                    string += c
        return dummy_root.left


# --- Test Suite Helpers ---
def build_tree(values: list) -> TreeNode:
    """Helper to build a tree from LeetCode's level-order array representation."""
    if not values:
        return None

    root = TreeNode(values[0])
    queue = collections.deque([root])
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


def are_trees_equal(t1: TreeNode, t2: TreeNode) -> bool:
    """Helper to check if two trees are structurally and strictly equal."""
    if not t1 and not t2:
        return True
    if not t1 or not t2:
        return False
    if t1.val != t2.val:
        return False
    return are_trees_equal(t1.left, t2.left) and are_trees_equal(t1.right, t2.right)


def print_tree(root: TreeNode | None):
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


# --- Test Suite ---
def run_tests():
    test_cases = [
        # (Input array representation, Description)
        ([1, 2, 3, None, None, 4, 5], "Standard balanced-ish tree (Example 1)"),
        ([], "Empty tree (Example 2)"),
        ([1], "Single root node"),
        ([1, 2], "Tree with only a left child"),
        ([1, None, 2], "Tree with only a right child"),
        ([1, 2, 3, 4, None, None, 5], "Asymmetric tree"),
        ([1, 2, None, 3, None, 4, None], "Left-skewed (Linked List-like) tree"),
        ([-1000, 1000, 0], "Edge case node values from constraints"),
    ]

    all_passed = True
    for i, (values, desc) in enumerate(test_cases, 1):
        original_root = build_tree(values)

        # Instantiate your Codec class
        ser = Codec()
        deser = Codec()

        try:
            # The test checks if deserialize(serialize(root)) reproduces the exact same tree
            serialized_data = ser.serialize(original_root)
            deserialized_root = deser.deserialize(serialized_data)
            print_tree(original_root)
            print_tree(deserialized_root)

            if are_trees_equal(original_root, deserialized_root):
                print(f"✅ Test {i} Passed: {desc}")
            else:
                print(f"❌ Test {i} Failed: {desc}")
                print(f"   Input (Level Order): {values}")
                print(f"   Note: The tree structure was not maintained.")
                all_passed = False

        except Exception as e:
            print(f"❌ Test {i} Failed: {desc}")
            print(f"   Input: {values}")
            print(f"   Error raised during execution: {e}")
            all_passed = False

    print("-" * 30)
    if all_passed:
        print("🎉 All test cases passed!")
    else:
        print("⚠️ Some test cases failed. Review your logic.")


if __name__ == "__main__":
    run_tests()
