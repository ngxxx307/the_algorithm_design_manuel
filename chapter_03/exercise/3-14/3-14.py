# ==========================================
# 1. Data Structures & Helpers
# ==========================================


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dll_to_list(head):
    """Helper to convert the resulting DLL into a Python list for printing."""
    if not head:
        return []

    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.right  # In a DLL, right acts as 'next'
    return result


def get_all_values(root):
    """Helper to get all values from a tree for generating Expected Result."""
    vals = []
    if not root:
        return vals

    def dfs(node):
        if not node:
            return
        dfs(node.left)
        vals.append(node.val)
        dfs(node.right)

    dfs(root)
    return vals


# ==========================================
# 2. YOUR IMPLEMENTATION HERE
# ==========================================
def traverse(curr, stack: list[TreeNode]):
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        next = curr.right
        return curr, next, stack
    return None, None, stack


def inorder_iterative(root: TreeNode):
    stack: list[tuple[TreeNode, int]] = []
    if root is None:
        return
    curr: TreeNode | None = root
    depth = 0
    max_depth = 0
    while curr or stack:
        while curr:
            stack.append((curr, depth))
            curr = curr.left
            depth = depth + 1
        curr, depth = stack.pop()
        max_depth = max(max_depth, depth)
        print(f"curr: {curr.val}, depth: {depth}")
        curr = curr.right
        depth = depth + 1
    print(f"max_depth: {max_depth}")
    return max_depth


def merge_bsts_to_dll(root1, root2):
    stack1 = []
    stack2 = []
    curr1, next1, stack1 = traverse(root1, stack1)
    curr2, next2, stack2 = traverse(root2, stack2)

    List = []

    while curr1 or curr2:
        if not curr2 or (curr1 and curr1.val < curr2.val):
            List.append(curr1)
            curr1, next1, stack1 = traverse(next1, stack1)
        else:
            List.append(curr2)
            curr2, next2, stack2 = traverse(next2, stack2)
    print([x.val for x in List])
    return None


# ==========================================
# 3. Test Cases & Runner
# ==========================================


def run_all_tests():
    test_cases = []

    # Case 1: Basic Unique Values
    t1 = TreeNode(5, TreeNode(1), TreeNode(8))
    t2 = TreeNode(2, TreeNode(0), TreeNode(4))
    test_cases.append(("Basic Unique", t1, t2))

    # Case 2: With Duplicates
    t1 = TreeNode(3, TreeNode(1), TreeNode(5))
    t2 = TreeNode(3, TreeNode(2), TreeNode(5))
    test_cases.append(("With Duplicates", t1, t2))

    # Case 3: One Tree Empty
    t1 = TreeNode(5, TreeNode(3), None)
    t2 = None
    test_cases.append(("One Tree Empty", t1, t2))

    # Case 4: Both Trees Empty
    t1 = None
    t2 = None
    test_cases.append(("Both Trees Empty", t1, t2))

    # Case 5: Disjoint Ranges
    t1 = TreeNode(2, TreeNode(1), TreeNode(3))
    t2 = TreeNode(10, TreeNode(8), TreeNode(12))
    test_cases.append(("Disjoint Ranges", t1, t2))

    # Case 6: Unbalanced Trees
    t1 = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
    t2 = TreeNode(8, TreeNode(7, TreeNode(6), None), None)
    test_cases.append(("Unbalanced Trees", t1, t2))

    # Case 7: Single Nodes (Duplicate)
    t1 = TreeNode(10)
    t2 = TreeNode(10)
    test_cases.append(("Single Nodes", t1, t2))

    print(f"{'TEST CASE':<20} | {'TYPE':<8} | {'RESULT'}")
    print("=" * 70)

    for name, r1, r2 in test_cases:
        # Calculate Expected Result (Get all values -> Sort them)
        vals1 = get_all_values(r1)
        vals2 = get_all_values(r2)
        expected_list = sorted(vals1 + vals2)

        # Calculate Actual Result
        try:
            result_head = merge_bsts_to_dll(r1, r2)
            actual_list = dll_to_list(result_head)
        except Exception as e:
            actual_list = f"Error: {e}"

        # Print Expected
        print(f"{name:<20} | {'Expect':<8} | {expected_list}")
        # Print Actual
        print(f"{'':<20} | {'Actual':<8} | {actual_list}")

        # Visual separator if match or mismatch
        match = "PASS" if expected_list == actual_list else "FAIL"
        print(f"{'':<20} | {'Status':<8} | {match}")
        print("-" * 70)


if __name__ == "__main__":
    run_all_tests()
