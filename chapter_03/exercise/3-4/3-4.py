class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next : ListNode | None = next
        self.min_next : ListNode | None = next

class stack():
    def __init__(self):
        self.min = None
        self.top = None
    
    def find_min(self):
        return self.min
    
    def push(self, node: ListNode | None):
        if not node:
            return
        # Update Top
        node.next = self.top
        self.top = node
        # Update Min
        if not self.min or node.val < self.min.val:
            node.min_next = self.min
            self.min = node
    
    def pop(self) -> ListNode | None:
        if not self.top:
            return None
        if self.top == self.min:
            self.min = self.top.min_next
        node = self.top
        self.top = node.next
        
        return node

def run_tests():
    print("--- Starting Stack Tests ---\n")

    # TEST 1: Basic Push/Pop & Empty Handling
    print("Test 1: Basic Push/Pop & Empty Handling")
    s1 = stack()
    
    # 1.1 Pop from empty
    res = s1.pop()
    print(f"Pop from empty: {res} (Expected: None)")
    
    # 1.2 Push one, check min, pop one
    s1.push(ListNode(10))
    current_min = s1.find_min()
    print(f"Push 10 -> Min: {current_min.val if current_min else None} (Expected: 10)")
    
    popped = s1.pop()
    print(f"Popped: {popped.val if popped else None} (Expected: 10)")
    print(f"Stack Empty Check: Top is {s1.top} (Expected: None)")
    print("-" * 20)

    # TEST 2: Descending Order (Updating New Minimums)
    print("Test 2: Descending Inputs (5 -> 3 -> 1)")
    s2 = stack()
    
    s2.push(ListNode(5))
    s2.push(ListNode(3))
    s2.push(ListNode(1))
    
    m = s2.find_min()
    print(f"Current Min: {m.val if m else None} (Expected: 1)")
    
    # Pop 1 (Min should revert to 3)
    p1 = s2.pop()
    m = s2.find_min()
    print(f"Popped {p1.val}. New Min: {m.val if m else None} (Expected: 3)")
    
    # Pop 3 (Min should revert to 5)
    p2 = s2.pop()
    m = s2.find_min()
    print(f"Popped {p2.val}. New Min: {m.val if m else None} (Expected: 5)")
    print("-" * 20)

    # TEST 3: Ascending Order (Min should stay constant)
    print("Test 3: Ascending Inputs (2 -> 4 -> 6)")
    s3 = stack()
    
    s3.push(ListNode(2))
    s3.push(ListNode(4))
    s3.push(ListNode(6))
    
    m = s3.find_min()
    print(f"Current Min: {m.val if m else None} (Expected: 2)")
    
    # Pop 6 (Min should STILL be 2)
    s3.pop()
    m = s3.find_min()
    print(f"Popped 6. New Min: {m.val if m else None} (Expected: 2)")
    print("-" * 20)

    # TEST 4: Duplicate Minimums (CRITICAL EDGE CASE)
    # This tests if your logic handles pushing the same minimum value twice
    print("Test 4: Duplicate Minimums (Push 2 -> Push 2)")
    s4 = stack()
    
    node_a = ListNode(2)
    node_b = ListNode(2)
    
    s4.push(node_a)
    s4.push(node_b)
    
    m = s4.find_min()
    print(f"Current Min: {m.val if m else None} (Expected: 2)")
    
    # Pop the top '2'. The remaining element is also '2'.
    # Does the stack still know the min is 2?
    popped = s4.pop()
    m = s4.find_min()
    
    print(f"Popped {popped.val}. Remaining Min: {m.val if m else 'None/Error'}")
    print(f"(Expected: 2. If None, the min_next link was broken or logic excluded the duplicate.)")
    print("-" * 20)

    # TEST 5: Interleaved Operations
    print("Test 5: Interleaved (Push 5, Push 1, Pop, Push 2)")
    s5 = stack()
    
    s5.push(ListNode(5)) # Min 5
    s5.push(ListNode(1)) # Min 1
    s5.pop()             # Pop 1, Min becomes 5
    s5.push(ListNode(2)) # Min becomes 2
    
    m = s5.find_min()
    print(f"Current Min: {m.val if m else None} (Expected: 2)")
    
    s5.pop() # Pop 2, Min becomes 5
    m = s5.find_min()
    print(f"After Pop, Min: {m.val if m else None} (Expected: 5)")

# Run the tests
if __name__ == "__main__":
    run_tests()