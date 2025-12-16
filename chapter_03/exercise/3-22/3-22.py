class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.parent: None | TreeNode = None
        self.left: None | TreeNode = left
        self.right: None | TreeNode = right
        self.subtree_height = 0
        self.n = 1


class binary_tree:
    def __init__(self):
        self.root: None | TreeNode = None
        return

    def insert(self, node: TreeNode):
        if not self.root:
            self.root = node
            return
        curr: TreeNode = self.root

        while curr:
            curr.n = curr.n + 1
            parent = curr

            if node.val < curr.val:
                curr = curr.left
                if not curr:
                    parent.left = node
                    node.parent = parent
                    break
            else:
                curr = curr.right
                if not curr:
                    parent.right = node
                    node.parent = parent
                    break

        self.propagate(node)

    # Propagate and update new subtree height
    def propagate(self, node: TreeNode, height=1):
        curr = node
        while curr:
            curr.subtree_height = max(curr.subtree_height, height)
            curr = curr.parent

            if curr:
                left_subtree_height = curr.left.subtree_height if curr.left else 0
                right_subtree_height = curr.right.subtree_height if curr.right else 0
                if abs(left_subtree_height - right_subtree_height) > 1:
                    height = self.rebalance(
                        curr, left_subtree_height, right_subtree_height
                    )
                    continue
            height = height + 1

    def rebalance(self, node: TreeNode, left_height: int, right_height: int) -> int:
        if right_height - left_height > 1:
            new_parent = node.right

            # Wire up new parent and node parent
            new_parent.parent = node.parent
            if node.parent:
                node.parent.right = new_parent
            else:
                self.root = new_parent

            # Wire up node and new parent's left
            node.right = new_parent.left
            if new_parent.left:
                new_parent.left.parent = node

            # Wire up new parent and node
            node.parent = new_parent
            new_parent.left = node

            new_left_height = node.left.subtree_height if node.left else 0
            new_right_height = node.right.subtree_height if node.right else 0
            node.subtree_height = max(new_left_height, new_right_height) + 1

            left_n = node.left.n if node.left else 0
            right_n = node.right.n if node.right else 0
            node.n = left_n + right_n + 1

            left_n = new_parent.left.n if new_parent.left else 0
            right_n = new_parent.right.n if new_parent.right else 0
            new_parent.n = left_n + right_n + 1
            return node.subtree_height
        if left_height - right_height > 1:
            new_parent = node.left

            new_parent.parent = node.parent
            if node.parent:
                node.parent.left = new_parent
            else:
                self.root = new_parent

            node.left = new_parent.right
            if new_parent.right:
                new_parent.right.parent = node

            node.parent = new_parent
            new_parent.right = node
            node.subtree_height = max(left_height, right_height) + 1

            left_n = node.left.n if node.left else 0
            right_n = node.right.n if node.right else 0
            node.n = left_n + right_n + 1

            left_n = new_parent.left.n if new_parent.left else 0
            right_n = new_parent.right.n if new_parent.right else 0
            new_parent.n = left_n + right_n + 1
            return node.subtree_height

    def find_left_most(self, curr: TreeNode) -> TreeNode:
        while curr.left:
            curr = curr.left
        return curr

    def find_right_most(self, curr: TreeNode) -> TreeNode:
        while curr.right:
            curr = curr.right
        return curr

    def median(self):
        curr = self.root
        left = 0
        right = 0
        target = curr.n / 2

        while curr:
            left_n = curr.left.n if curr.left else 0
            right_n = curr.right.n if curr.right else 0

            diff = left_n + left - (right_n + right)
            if diff == 0:
                return curr.val
            if diff == 1:
                temp = self.find_right_most(curr.left)
                return (curr.val + temp.val) / 2
            if diff == -1:
                temp = self.find_left_most(curr.right)
                return (curr.val + temp.val) / 2
            if diff > 1:
                right = right_n + 1
                curr = curr.left
            elif diff < -1:
                left = left_n + 1
                curr = curr.right
        print(f"final curr:{curr.val}")
        print("left and right:", left, right)


def print_tree(node: TreeNode, level=0, prefix="Root:"):
    """
    Helper function to print a binary tree structure with indentation.
    """
    if node is not None:
        # print(" " * (level * 4) + prefix, node.val, f"(h:{node.subtree_height})")
        print(" " * (level * 4) + prefix, node.val, f"(n:{node.n})")
        if node.left:
            print_tree(node.left, level + 1, "L:")
        if node.right:
            print_tree(node.right, level + 1, "R:")


if __name__ == "__main__":
    bt = binary_tree()
    bt.insert(TreeNode(1))
    bt.insert(TreeNode(2))
    bt.insert(TreeNode(3))
    bt.insert(TreeNode(4))
    bt.insert(TreeNode(5))
    bt.insert(TreeNode(6))
    bt.insert(TreeNode(7))
    bt.insert(TreeNode(8))
    bt.insert(TreeNode(9))
    bt.insert(TreeNode(10))
    bt.insert(TreeNode(11))
    bt.insert(TreeNode(12))
    bt.insert(TreeNode(13))
    bt.insert(TreeNode(14))

    print_tree(bt.root)
    print(bt.median())
