import unittest

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_height(root: TreeNode | None) -> tuple[int, bool]:
    if not root:
        return 0, True
    left_height, left_balance = get_height(root.left)
    right_height, right_balance = get_height(root.right)
    
    height = max(left_height, right_height) + 1
    return height, abs(left_height - right_height) <= 1 and left_balance and right_balance

class TestHeightBalanced(unittest.TestCase):

    def isBalanced(self, root: TreeNode | None) -> bool:
        """
        TODO: Implement your O(n) solution here.
        Return True if the tree is height-balanced, False otherwise.
        """
        if not root:
            return True
        
        height, balance = get_height(root)
        return balance

    # --- Test Cases ---

    def test_empty_tree(self):
        """An empty tree is considered balanced."""
        root = None
        self.assertTrue(self.isBalanced(root))

    def test_single_node(self):
        """A tree with one node is balanced."""
        root = TreeNode(1)
        self.assertTrue(self.isBalanced(root))

    def test_simple_balanced(self):
        """
        Tree:
            3
           / \
          9  20
             / \
            15  7
        Expected: True
        """
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        self.assertTrue(self.isBalanced(root))

    def test_simple_unbalanced(self):
        """
        Tree:
              1
             / \
            2   2
           / \
          3   3
         / \
        4   4
        Expected: False (Left subtree is too deep)
        """
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(3)
        root.left.left.left = TreeNode(4)
        root.left.left.right = TreeNode(4)
        self.assertFalse(self.isBalanced(root))

    def test_right_skewed_unbalanced(self):
        """
        Tree:
        1
         \
          2
           \
            3
        Expected: False (Height diff is 2 at root)
        """
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        self.assertFalse(self.isBalanced(root))

    def test_right_skewed_balanced(self):
        """
        Tree:
        1
         \
          2
        Expected: True (Height diff is 1)
        """
        root = TreeNode(1)
        root.right = TreeNode(2)
        self.assertTrue(self.isBalanced(root))

    def test_complex_balanced(self):
        """
        A larger balanced tree.
              1
            /   \
           2     3
          / \   / \
         4   5 6   7
        Expected: True
        """
        root = TreeNode(1)
        root.left = TreeNode(2, TreeNode(4), TreeNode(5))
        root.right = TreeNode(3, TreeNode(6), TreeNode(7))
        self.assertTrue(self.isBalanced(root))

    def test_zig_zag_unbalanced(self):
        """
        Tree:
           1
          /
         2
          \
           3
            \
             4
        Expected: False
        """
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.right = TreeNode(3)
        root.left.right.right = TreeNode(4)
        self.assertFalse(self.isBalanced(root))

if __name__ == '__main__':
    unittest.main()