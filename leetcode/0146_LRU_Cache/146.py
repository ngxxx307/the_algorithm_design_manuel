# Leave this empty for your implementation
class Node:
    def __init__(self, val:int, key: int) -> None:
        self.val: int = val
        self.key: int = key
        self.next = self.prev = None
        pass

class LRUCache:
    def __init__(self, capacity: int):
        self.cache: dict[int, Node] = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left
        self.capacity = capacity
    def print_self(self):
        curr = self.left
        while curr:
            print(f"key:{curr.key} value:{curr.val} ", end=' -> ')
            curr= curr.next
        print()
    def remove(self, node: Node):
        next, prev = node.next, node.prev
        next.prev = prev
        prev.next = next

    def insert(self, node: Node):
        left = self.left
        next =self.left.next
        node.next, node.prev = next , left
        next.prev = node
        left.next = node


    def put(self, key: int, val:int):
        if key in self.cache:
            self.remove(self.cache[key])
        node = Node(val, key)
        self.insert(node)
        self.cache[key] = node
        if len(self.cache) > self.capacity:
            node = self.right.prev
            self.remove(self.right.prev)
            del self.cache[node.key]
        # self.print_self()


    def get(self, key: int):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        # self.print_self()
        return node.val
            

        


# --- Test Suite ---
def run_tests():
    test_cases = [
        # (List of operations, List of arguments, Expected output, Description)
        (
            ["LRUCache", "put", "get", "put", "put", "get", "get"],
            [[2], [1, 10], [1], [2, 20], [3, 30], [2], [1]],
            [None, None, 10, None, None, 20, -1],
            "Standard execution (Example 1)"
        ),
        (
            ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"],
            [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]],
            [None, None, None, 1, None, -1, None, -1, 3, 4],
            "Eviction with multiple gets updating recency"
        ),
        (
            ["LRUCache", "put", "get", "put", "get", "get"],
            [[1], [2, 1], [2], [3, 2], [2], [3]],
            [None, None, 1, None, -1, 2],
            "Capacity of exactly 1"
        ),
        (
            ["LRUCache", "put", "put", "get", "put", "get"],
            [[2], [2, 1], [2, 2], [2], [1, 1], [2]],
            [None, None, None, 2, None, 2],
            "Updating an existing key's value"
        ),
(
            ["LRUCache", "put", "put", "get", "put", "put", "get"],
            [[2], [2, 1], [1, 1], [2], [4, 1], [1, 2], [1]],
            [None, None, None, 1, None, None, 2], # Changed the last element to 2
            "Re-adding a previously evicted key"
        ),
    ]

    all_passed = True
    for i, (ops, args, expected, desc) in enumerate(test_cases, 1):
        cache = None
        actual = []
        
        # Simulate LeetCode's execution of operations
        for op, arg in zip(ops, args):
            if op == "LRUCache":
                cache = LRUCache(arg[0])
                actual.append(None)
            elif op == "put":
                actual.append(cache.put(arg[0], arg[1]))
            elif op == "get":
                actual.append(cache.get(arg[0]))
                
        # Evaluate results
        if actual == expected:
            print(f"✅ Test {i} Passed: {desc}")
        else:
            print(f"❌ Test {i} Failed: {desc}")
            print(f"   Operations: {ops}")
            print(f"   Arguments:  {args}")
            print(f"   Expected:   {expected}")
            print(f"   Got:        {actual}")
            all_passed = False

    print("-" * 30)
    if all_passed:
        print("🎉 All test cases passed!")
    else:
        print("⚠️ Some test cases failed. Review your logic.")


if __name__ == "__main__":
    run_tests()