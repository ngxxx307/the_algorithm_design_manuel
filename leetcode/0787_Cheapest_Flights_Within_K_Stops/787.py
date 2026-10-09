import unittest
from collections import defaultdict, deque
import math


# Leave this empty for your implementation
class Solution:

    def findCheapestPrice(
        self, n: int, flights: list[list[int]], src: int, dst: int, k: int
    ) -> int:
        adj_list = defaultdict(list)
        for i, j, cost in flights:
            adj_list[i].append((j, cost))
        costs: list[int] = [math.inf for _ in range(n)]

        queue = deque([(src, 0)])
        stop = 0
        while queue:
            stop += 1
            new_queue = deque([])
            while queue:
                node, cost = queue.popleft()
                costs[node] = min(costs[node], cost)

                for v, c in adj_list[node]:
                    c = cost + c
                    if c < costs[v]:
                        new_queue.append((v, c))

            queue = new_queue
            if stop == (k + 2):
                break
        return costs[dst] if costs[dst] != math.inf else -1


# --- Test Suite ---
def run_tests():
    sol = Solution()

    test_cases = [
        # (n, flights, src, dst, k, Expected output, Description)
        (
            5,
            [[0, 1, 5], [0, 2, 1], [2, 1, 1], [1, 3, 1], [3, 4, 1], [1, 4, 100]],
            0,
            4,
            3,
            4,
            "neetcode",
        ),
        (
            4,
            [
                [0, 1, 100],
                [1, 2, 100],
                [2, 0, 100],
                [1, 3, 600],
                [2, 3, 200],
            ],
            0,
            3,
            1,
            700,
            "Optimal path within k stops (Example 1)",
        ),
        (
            3,
            [[0, 1, 100], [1, 2, 100], [0, 2, 500]],
            0,
            2,
            1,
            200,
            "Multi-stop flight is cheaper than direct (Example 2)",
        ),
        (
            3,
            [[0, 1, 100], [1, 2, 100], [0, 2, 500]],
            0,
            2,
            0,
            500,
            "k=0 forces direct flight choice (Example 3)",
        ),
        (
            4,
            [[0, 1, 100], [2, 3, 200]],
            0,
            3,
            2,
            -1,
            "No path exists between src and dst",
        ),
        (
            5,
            [[0, 1, 100], [1, 2, 100], [2, 3, 100], [3, 4, 100]],
            0,
            4,
            2,
            -1,
            "Path exists but exceeds maximum allowed stops",
        ),
        (
            4,
            [[0, 3, 1000], [0, 1, 100], [1, 2, 100], [2, 3, 100]],
            0,
            3,
            2,
            300,
            "Path using exact k stops is cheapest",
        ),
        (
            4,
            [[0, 1, 100], [1, 0, 100], [1, 2, 100], [2, 3, 100]],
            0,
            3,
            1,
            -1,
            "Graph with cycle, path requires 2 stops but k=1",
        ),
        (
            3,
            [[0, 1, 200], [1, 2, 200]],
            0,
            2,
            5,
            400,
            "k is significantly larger than number of nodes",
        ),
        (
            2,
            [[0, 1, 300]],
            0,
            1,
            0,
            300,
            "Minimal graph with 2 nodes and direct connection",
        ),
    ]

    all_passed = True
    for i, (n, flights, src, dst, k, expected, desc) in enumerate(test_cases, 1):
        result = sol.findCheapestPrice(n, flights, src, dst, k)
        if result == expected:
            print(f"✅ Test {i} Passed: {desc}")
        else:
            print(f"❌ Test {i} Failed: {desc}")
            print(f"   Input: n={n}, flights={flights}, src={src}, dst={dst}, k={k}")
            print(f"   Expected: {expected}, but got: {result}")
            all_passed = False

    print("-" * 50)
    if all_passed:
        print("🎉 All test cases passed!")
    else:
        print("⚠️ Some test cases failed. Review your logic.")


if __name__ == "__main__":
    run_tests()
