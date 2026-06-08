from typing import Optional


# Definition for a Node.
class Node:

    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:

    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return head
        oldToCopy = {None: None}
        curr = head
        copyHead = Node(curr.val)
        oldToCopy[curr] = copyHead
        
        while curr:
            if curr not in oldToCopy:
                copy = Node(curr.val)
                oldToCopy[curr] = copy
            if curr.next not in oldToCopy:
                copyNext = Node(curr.next.val)
                oldToCopy[curr.next] = copyNext
            if curr.random not in oldToCopy:
                copyRandom = Node(curr.random.val)
                oldToCopy[curr.random] = copyRandom 
            oldToCopy[curr].next = oldToCopy[curr.next]
            oldToCopy[curr].random = oldToCopy[curr.random]       
            curr = curr.next
        return copyHead


# --- Helper Functions for Testing ---
def build_list(data: list[list]) -> Optional[Node]:
    """Builds a linked list with random pointers from a list of [val, random_index] pairs."""
    if not data:
        return None

    # Step 1: Create all nodes
    nodes = [Node(val) for val, _ in data]

    # Step 2: Assign next and random pointers
    for i, (_, rand_idx) in enumerate(data):
        if i < len(nodes) - 1:
            nodes[i].next = nodes[i + 1]
        if rand_idx is not None:
            nodes[i].random = nodes[rand_idx]

    return nodes[0]


def list_to_array(head: Optional[Node]) -> list[list]:
    """Converts a linked list with random pointers back into a list of [val, random_index] pairs."""
    if not head:
        return []

    # Map each node to its 0-based index
    node_to_idx = {}
    nodes = []
    curr = head
    idx = 0

    while curr:
        nodes.append(curr)
        node_to_idx[curr] = idx
        curr = curr.next
        idx += 1

    # Reconstruct the serialized format
    result = []
    for node in nodes:
        rand_idx = (
            node_to_idx[node.random] if node.random in node_to_idx else None
        )
        result.append([node.val, rand_idx])

    return result


def verify_deep_copy(original: Optional[Node], cloned: Optional[Node]) -> bool:
    """Verifies that the cloned list does not share memory references with the original list."""
    if not original and not cloned:
        return True
    if not original or not cloned:
        return False

    # Track all original node addresses
    original_refs = set()
    curr = original
    while curr:
        original_refs.add(id(curr))
        curr = curr.next

    # Check if any cloned node points to an original node reference
    curr = cloned
    while curr:
        if id(curr) in original_refs:
            return False  # Shallow copy detected!
        curr = curr.next

    return True


# --- Test Suite ---
def run_tests():
    sol = Solution()

    test_cases = [
        (
            [[3, None], [7, 3], [4, 0], [5, 1]],
            "Standard structure (Example 1)",
        ),
        ([[1, None], [2, 2], [3, 2]], "Multiple nodes pointing to same random"),
        ([], "Empty list edge case"),
        ([[10, None]], "Single node with no random pointer"),
        ([[5, 0]], "Single node pointing to itself"),
        (
            [[1, 2], [1, 0], [1, 1]],
            "Duplicate values with criss-crossed random pointers",
        ),
        (
            [[1, None], [2, None], [3, None]],
            "All random pointers are null/None",
        ),
    ]

    all_passed = True
    for i, (data, desc) in enumerate(test_cases, 1):
        # Generate the original linked list structure
        original_head = build_list(data)

        # Run implementation
        cloned_head = sol.copyRandomList(original_head)

        # Evaluate structural correctness and deep copy isolation
        result_array = list_to_array(cloned_head)
        is_deep = verify_deep_copy(original_head, cloned_head)

        if result_array == data and is_deep:
            print(f"✅ Test {i} Passed: {desc}")
        else:
            print(f"❌ Test {i} Failed: {desc}")
            print(f"   Input:            {data}")
            print(f"   Got Structure:    {result_array}")
            print(
                f"   Is Deep Copy?     {'Yes' if is_deep else 'No (Shallow copy detected!)'}"
            )
            all_passed = False

    print("-" * 50)
    if all_passed:
        print("🎉 All test cases passed successfully!")
    else:
        print("⚠️ Some test cases failed. Check your deep copy connections.")


if __name__ == "__main__":
    run_tests()