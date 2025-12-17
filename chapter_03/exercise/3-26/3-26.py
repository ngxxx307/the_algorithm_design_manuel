import random
import time
from typing import Self

# ==========================================
# PART 1: YOUR DATA STRUCTURE
# ==========================================


class TreeNode:
    def __init__(
        self,
        limit: tuple[int, int],
        minimum: int,
        left: Self | None = None,
        right: Self | None = None,
        n: int = 0,
    ):
        self.limit: tuple[int, int] = limit
        self.minimum: int = minimum
        self.left = left
        self.right = right
        self.n = n


class RangeMinQuery:
    def __init__(self, arr: list[int]):
        node_arr = self.__build_node(arr)
        self.root = self.__build_tree(node_arr)[0]

    def __build_tree(self, arr: list[TreeNode]) -> list[TreeNode]:
        node_arr = []

        i = 0
        while i < len(arr) - 1:
            left = arr[i]
            right = arr[i + 1]
            internal_node = TreeNode(
                limit=(left.limit[0], right.limit[1]),
                minimum=min(left.minimum, right.minimum),
                left=left,
                right=right,
            )
            node_arr.append(internal_node)
            i = i + 2
        if i == len(arr) - 1:
            node_arr.append(arr[i])
        if len(node_arr) != 1:
            node_arr = self.__build_tree(node_arr)
        return node_arr

    def __build_node(self, arr: list[int]) -> list[TreeNode]:
        node_arr: list[TreeNode] = []

        i = 0
        while i < len(arr) - 1:
            left = TreeNode(limit=(i, i), minimum=arr[i])
            right = TreeNode(limit=(i + 1, i + 1), minimum=arr[i + 1])
            limit = (i, i + 1)
            interal_node = TreeNode(
                limit=limit,
                minimum=min(left.minimum, right.minimum),
                left=left,
                right=right,
            )
            node_arr.append(interal_node)
            i = i + 2
        if i == len(arr) - 1:
            interal_node = TreeNode(limit=(i, i), minimum=arr[i])
            node_arr.append(interal_node)
        return node_arr

    def __evaluate(self, i: int, j: int, curr: TreeNode) -> int:
        min_arr = []
        if (i, j) == curr.limit:
            return curr.minimum
        if i <= curr.left.limit[1]:
            min_arr.append(self.__evaluate(i, min(curr.left.limit[1], j), curr.left))
        if j >= curr.right.limit[0]:
            min_arr.append(self.__evaluate(max(i, curr.right.limit[0]), j, curr.right))
        return min(min_arr)

    def query(self, i: int, j: int) -> int:
        return self.__evaluate(i, j, self.root)

    def print_tree(self):
        """
        Prints the tree level by level from root to bottom.
        """
        if not self.root:
            print("Empty Tree")
            return

        # We use a list as a queue for Level Order Traversal
        queue = [self.root]
        level = 0

        while queue:
            level_length = len(queue)
            print(f"Level {level}: ", end="")

            # Process all nodes at the current level
            for _ in range(level_length):
                node = queue.pop(0)

                # Print the current node's data
                # Format: [Range: Value]
                print(f"[{node.limit}: {node.minimum}] ", end=" ")

                # Add children to the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            print()  # Newline after every level
            level += 1


# ==========================================
# PART 2: THE TEST SUITE
# ==========================================


def get_ground_truth(arr, i, j):
    """
    The 'Oracle'. Uses Python's built-in O(N) slice to find the absolute truth.
    """
    return min(arr[i : j + 1])


def run_correctness_tests():
    print("--- Running Correctness Tests ---")

    test_cases = [
        # (Description, Array)
        ("Small sorted", [1, 2, 3, 4, 5]),
        ("Small reverse", [5, 4, 3, 2, 1]),
        ("Random small", [10, 5, 2, 7, 8, 2]),
        ("Negatives", [-5, -10, 0, 5, 10]),
        ("All same", [7, 7, 7, 7]),
        ("Single element", [42]),
    ]

    total_passed = 0
    total_checks = 0

    for name, arr in test_cases:
        print(f"Testing: {name} (Size: {len(arr)})")

        # 1. Build your structure
        try:
            rmq = RangeMinQuery(arr)
        except Exception as e:
            print(f"CRITICAL: Crashed while building tree for {name}: {e}")
            continue

        # 2. Run every possible range query for small arrays
        n = len(arr)
        for i in range(n):
            for j in range(i, n):
                total_checks += 1

                # Get Expected (Ground Truth)
                expected = get_ground_truth(arr, i, j)

                # Get Actual (Your Solution)
                try:
                    actual = rmq.query(i, j)
                except Exception as e:
                    print(f"  [FAIL] Crashed querying range [{i}, {j}]: {e}")
                    return

                # Compare
                if actual != expected:
                    print(f"  [FAIL] Range [{i}, {j}]")
                    print(f"         Array: {arr}")
                    print(f"         Expected: {expected}")
                    print(f"         Got:      {actual}")
                    return  # Stop on first failure to let you debug

                total_passed += 1

    print(f"Success! Passed {total_passed}/{total_checks} basic logic checks.\n")


def run_random_fuzz_test():
    print("--- Running Random Fuzz Test (Stress Test) ---")
    # Generate a larger array
    size = 1000
    arr = [random.randint(-10000, 10000) for _ in range(size)]

    print(f"Building tree for {size} elements...")
    rmq = RangeMinQuery(arr)

    num_queries = 2000
    print(f"Running {num_queries} random queries...")

    for _ in range(num_queries):
        i = random.randint(0, size - 1)
        j = random.randint(i, size - 1)

        expected = get_ground_truth(arr, i, j)
        actual = rmq.query(i, j)

        if actual != expected:
            print(f"  [FAIL] Random Fuzz Test Failed!")
            print(f"         Range: [{i}, {j}]")
            print(f"         Expected: {expected}, Got: {actual}")
            print(f"         (Array too large to print)")
            return

    print("Success! Passed random fuzz tests.\n")


def run_performance_check():
    """
    Checks if the solution is likely O(log n) or O(1) vs O(n).
    """
    print("--- Running Performance/Time Complexity Check ---")
    size = 100000  # Large array
    arr = [random.randint(0, 1000000) for _ in range(size)]

    print(f"Building tree for {size} elements...")
    start_build = time.time()
    rmq = RangeMinQuery(arr)
    end_build = time.time()
    print(f"Build time: {end_build - start_build:.4f} seconds")

    # Run many queries
    queries = 10000
    print(f"Running {queries} queries...")

    start_query = time.time()
    for _ in range(queries):
        i = random.randint(0, size - 1)
        j = random.randint(i, size - 1)
        rmq.query(i, j)  # We don't check correctness here, just speed
    end_query = time.time()

    total_time = end_query - start_query
    avg_time = total_time / queries

    print(f"Total query time: {total_time:.4f} seconds")
    print(f"Avg time per query: {avg_time:.6f} seconds")

    if avg_time > 0.001:
        print(
            "WARNING: Query time seems slow. Ensure it is O(log n) or O(1), not O(n)."
        )
    else:
        print("Performance looks good (likely O(log n) or better).")


if __name__ == "__main__":
    # 1. Check if logic is correct on small cases
    run_correctness_tests()

    # 2. Check if logic holds on larger random cases
    # run_random_fuzz_test() # Uncomment this after passing step 1

    # 3. Check if it is fast enough
    # run_performance_check() # Uncomment this after passing step 2
