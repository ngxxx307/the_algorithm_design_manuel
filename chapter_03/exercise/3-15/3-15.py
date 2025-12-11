import unittest

# -------------------------------------------------------------------------
# Data Structure Definition
# -------------------------------------------------------------------------
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val})"

# -------------------------------------------------------------------------
# Placeholder for YOUR Solution
# -------------------------------------------------------------------------
def traverse_tree(root: TreeNode) -> list[TreeNode]:
    stack: list[TreeNode] = []
    List = []
    if root is None:
        return
    curr: TreeNode | None = root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        # print(f"curr: {curr.val}")
        List.append(curr)
        curr = curr.right
    return List

def reorder(List: list[TreeNode], parent: TreeNode | None = None, is_left: bool = True) -> TreeNode:
    n = len(List)
    i = len(List)//2
    
    

    new_parent = TreeNode(List[i].val)
    if parent:
        if is_left:
            parent.left = new_parent
        else:
            parent.right = new_parent
        
    left_list = List[0:i]
    right_list = List[i+1:]
    if left_list:
        reorder(left_list, new_parent, True)
    if right_list:
        reorder(right_list, new_parent, False)
    return new_parent

def balance_bst(root: TreeNode | None) -> TreeNode | None:
    """
    Takes an n-node binary search tree and constructs an equivalent 
    height-balanced binary search tree.
    
    TODO: Implement your O(n) algorithm here.
    """
    if not root:
        return None
    List = traverse_tree(root)
    new_root = reorder(List, None)
    
    traverse_tree(new_root)
    # This is a dummy implementation that just returns the input
    # so the tests run (and fail expectedly). Replace this with your logic.
    return new_root 

# -------------------------------------------------------------------------
# Helper Functions for Verification
# -------------------------------------------------------------------------

def get_inorder(root):
    """
    Returns a list of values from an inorder traversal.
    Iterative with a Safety Limit.
    """
    res = []
    stack = []
    curr = root
    count = 0
    LIMIT = 2000 # Safety valve for cycles
    
    while (curr or stack) and count < LIMIT:
        while curr:
            stack.append(curr)
            curr = curr.left
            count += 1
            if count >= LIMIT: break 
        
        if not stack or count >= LIMIT: break
        
        curr = stack.pop()
        res.append(curr.val)
        curr = curr.right
        count += 1
        
    if count >= LIMIT:
        print("\n[WARNING] Cycle or infinite depth detected in get_inorder!")
        
    return res

def is_balanced(root, depth=0):
    """
    Checks if a tree is height-balanced.
    Returns (True/False, height).
    """
    if not root:
        return True, 0
    
    # Safety check for cycles or extreme depth
    if depth > 100: 
        return False, 999
    
    # FIX: Pass depth + 1 to recursive calls
    left_bal, left_h = is_balanced(root.left, depth + 1)
    right_bal, right_h = is_balanced(root.right, depth + 1)
    
    is_curr_balanced = (left_bal and right_bal and 
                        abs(left_h - right_h) <= 1)
    
    return is_curr_balanced, 1 + max(left_h, right_h)

class TestBalanceBST(unittest.TestCase):
    
    def check_tree_validity(self, expected_vals, new_root, description):
        """
        Generic checker that asserts:
        1. The new tree contains the same elements (BST property preserved).
        2. The new tree is height-balanced.
        """
        # 1. Check Content Integrity (BST Property)
        new_vals = get_inorder(new_root)
        
        # If lengths differ significantly, it's likely due to the cycle safety cutoff
        if len(new_vals) != len(expected_vals):
            self.fail(f"{description}: Resulting tree seems to have a cycle or lost nodes. "
                      f"Expected {len(expected_vals)} nodes, got {len(new_vals)} (or hit safety limit).")

        self.assertEqual(expected_vals, new_vals, 
                         f"{description}: In-order traversal changed. Elements lost or reordered incorrectly.")
        
        # 2. Check Balance
        balanced, height = is_balanced(new_root)
        self.assertTrue(balanced, 
                        f"{description}: Tree is not height-balanced or has a cycle. Height is {height}.")
        
        print(f"PASS: {description} (Height: {height}, Nodes: {len(new_vals)})")

    def test_01_right_skewed_linked_list(self):
        # Input: 1 -> 2 -> 3 -> 4 -> 5
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        root.right.right.right = TreeNode(4)
        root.right.right.right.right = TreeNode(5)
        
        expected = get_inorder(root)
        result = balance_bst(root)
        self.check_tree_validity(expected, result, "Right Skewed List")

    def test_02_left_skewed_linked_list(self):
        # Input: 5 -> 4 -> 3 -> 2 -> 1
        root = TreeNode(5)
        root.left = TreeNode(4)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(2)
        root.left.left.left.left = TreeNode(1)
        
        expected = get_inorder(root)
        result = balance_bst(root)
        self.check_tree_validity(expected, result, "Left Skewed List")

    def test_03_zigzag_unbalanced(self):
        # Input: A zig-zag shape
        root = TreeNode(10)
        root.left = TreeNode(5)
        root.left.right = TreeNode(8)
        root.left.right.left = TreeNode(6)
        root.left.right.left.right = TreeNode(7)
        
        expected = get_inorder(root)
        result = balance_bst(root)
        self.check_tree_validity(expected, result, "Zig-Zag Unbalanced")

    def test_04_already_balanced(self):
        # Input: Perfect tree
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        
        expected = get_inorder(root)
        result = balance_bst(root)
        self.check_tree_validity(expected, result, "Already Balanced")

    def test_05_single_node(self):
        root = TreeNode(1)
        expected = get_inorder(root)
        result = balance_bst(root)
        self.check_tree_validity(expected, result, "Single Node")

    def test_06_empty_tree(self):
        root = None
        result = balance_bst(root)
        self.assertIsNone(result, "Empty tree should return None")
        print("PASS: Empty Tree")

    def test_07_large_skewed_tree(self):
        # Performance/Correctness check for larger N
        dummy = TreeNode(-1)
        curr = dummy
        for i in range(1000):
            curr.right = TreeNode(i)
            curr = curr.right
        root = dummy.right
        
        expected = get_inorder(root)
        result = balance_bst(root)
        
        self.check_tree_validity(expected, result, "Large Skewed Tree")
        
        _, h = is_balanced(result)
        self.assertLess(h, 15, "Height of balanced tree with 1000 nodes should be small")

if __name__ == '__main__':
    unittest.main()