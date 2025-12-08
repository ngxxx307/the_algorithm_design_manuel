from typing import Optional, List
from collections import deque

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        
        curr = head
        length = 1
        while curr.next != None:
            curr = curr.next
            length = length + 1
        
        tail = curr
        position = k % length
        
        
        if position == 0:
            return head
        
        curr = head
        for _ in range( length - position - 1):
            curr = curr.next
            
        new_head = curr.next
        curr.next = None
        tail.next = head
        
        return new_head

# --- Helper Functions for Testing ---
def list_to_linked_list(elements: List[int]) -> Optional[ListNode]:
    """Creates a Linked List from a Python list."""
    if not elements:
        return None
    dummy = ListNode(0)
    current = dummy
    for val in elements:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    """Converts a Linked List back to a Python list for easy comparison."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# --- Test Runner ---
def run_tests():
    solver = Solution()
    
    test_cases = [
        # --- Standard Examples ---
        {
            "name": "Ex 1: Standard Rotation",
            "input_list": [1, 2, 3, 4, 5],
            "k": 2,
            "expected": [4, 5, 1, 2, 3]
        },
        {
            "name": "Ex 2: k > Length (Modulo)",
            "input_list": [0, 1, 2],
            "k": 4,
            "expected": [2, 0, 1] 
            # Length is 3. Rotating by 4 is same as rotating by 1.
        },

        # --- Identity Cases (No Change) ---
        {
            "name": "k = 0 (No rotation)",
            "input_list": [1, 2, 3],
            "k": 0,
            "expected": [1, 2, 3]
        },
        {
            "name": "k = Length (Full cycle)",
            "input_list": [1, 2, 3],
            "k": 3,
            "expected": [1, 2, 3]
        },
        {
            "name": "k is multiple of Length",
            "input_list": [1, 2],
            "k": 6,
            "expected": [1, 2]
        },

        # --- Edge Cases ---
        {
            "name": "Empty List",
            "input_list": [],
            "k": 1,
            "expected": []
        },
        {
            "name": "Single Node",
            "input_list": [100],
            "k": 99,
            "expected": [100]
        },
        
        # --- Large k ---
        {
            "name": "Large k",
            "input_list": [1, 2, 3],
            "k": 2000000000, # 2 billion
            "expected": [2, 3, 1]
            # 2e9 % 3 = 2. Rotate by 2.
        }
    ]

    print(f"{'Test Name':<30} | {'Status':<10} | {'Result'}")
    print("-" * 65)

    for case in test_cases:
        # Prepare input
        head = list_to_linked_list(case["input_list"])
        k = case["k"]
        expected = case["expected"]
        
        # Run solution
        # We wrap in try/except to catch common Linked List errors like AttributeError on None
        try:
            result_head = solver.rotateRight(head, k)
            result_list = linked_list_to_list(result_head)
            status = "PASS" if result_list == expected else "FAIL"
        except Exception as e:
            status = "ERROR"
            result_list = str(e)

        print(f"{case['name']:<30} | {status:<10} | {result_list if status != 'PASS' else 'Correct'}")
        
        if status == "FAIL":
            print(f"   Input:    {case['input_list']}, k={k}")
            print(f"   Expected: {expected}")
            print(f"   Got:      {result_list}")
            print("-" * 65)

if __name__ == "__main__":
    run_tests()