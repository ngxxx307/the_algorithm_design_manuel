# 1. Define the Node class
# This is the blueprint for every single circle (node) in your tree.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_iterative(root: TreeNode):
    stack: list[TreeNode] = []
    left: TreeNode = None
    right: TreeNode = None
    prev: TreeNode = None
    if root is None:
        return
    curr: TreeNode | None = root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        if prev and prev.val > curr.val:
            left = prev
        if left:
            if not right or right.val > curr.val:
                right = curr
        print(f"curr: {curr.val}")
        prev = curr
        curr = curr.right
    print(f"left: {left.val}, right: {right.val}")
    return


# 3. Build the Data Structure (The Test Case)
# Let's build this tree:
#       4
#      / \
#     2   6
#    / \ / \
#   1  3 5  7

print("--- Building Tree ---")
# Create the nodes
root = TreeNode(4)
root.left = TreeNode(1)
root.right = TreeNode(6)

root.left.left = TreeNode(2)
root.left.right = TreeNode(3)

root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

# 4. Run the Test
print("\n--- Running Iterative In-Order Traversal ---")
output = inorder_iterative(root)
