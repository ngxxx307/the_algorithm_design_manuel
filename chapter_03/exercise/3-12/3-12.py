# 1. Define the Node class
# This is the blueprint for every single circle (node) in your tree.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_iterative(root: TreeNode):
    stack : list[tuple[TreeNode, int]] = []
    if root is None:
        return
    curr : TreeNode | None = root
    depth = 0
    max_depth = 0
    while curr or stack:
        while curr:
            stack.append((curr, depth))
            curr = curr.left
            depth  = depth + 1
        curr, depth = stack.pop()
        max_depth = max(max_depth, depth)
        print(f"curr: {curr.val}, depth: {depth}")
        curr = curr.right
        depth  = depth + 1
    print(f"max_depth: {max_depth}")
    return max_depth

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
root.left = TreeNode(2)
root.right = TreeNode(6)

root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.left.right.right = TreeNode(40)

root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

# 4. Run the Test
print("\n--- Running Iterative In-Order Traversal ---")
output = inorder_iterative(root)
