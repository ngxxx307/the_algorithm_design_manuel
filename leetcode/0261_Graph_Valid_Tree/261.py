from multiprocessing import process
from typing import List


# Leave this empty for your implementation
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        edge_list = [[] for _ in range(n)]
        discovered = [False] * n
        processed = [False] * n
        parents = [None] * n

        for src, dest in edges:
            edge_list[src].append(dest)
            edge_list[dest].append(src)

        def dfs(node: int):
            discovered[node] = True

            for neightbor in edge_list[node]:
                if not discovered[neightbor]:
                    parents[neightbor] = node
                    discovered[neightbor] = True
                    res = dfs(neightbor)
                    if not res:
                        return False
                elif (
                    not processed[neightbor]
                    and parents[node]
                    and parents[node] != neightbor
                ):
                    return False
            processed[node] = True

            return True

        count = 0
        for i in range(n):
            if not discovered[i]:
                res = dfs(i)
                if not res:
                    return False
                count += 1
                if count > 1:
                    return False
        return True


# --- Test Suite ---
def run_tests():
    sol = Solution()

    test_cases = [
        # (n, edges, Expected output, Description)
        # (5, [[0, 1], [1, 3], [3, 2], [1, 4]], True, "neetcode"),
        # (
        #     5,
        #     [[0, 1], [0, 2], [0, 3], [1, 4]],
        #     True,
        #     "Valid tree, star-like (Example 1)",
        # ),
        (
            5,
            [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]],
            False,
            "Graph with a cycle (Example 2)",
        ),
        (1, [], True, "Single node, no edges"),
        (4, [[0, 1], [2, 3]], False, "Disconnected graph with no cycles"),
        (4, [[0, 1], [1, 2], [2, 0]], False, "Disconnected graph with a cycle"),
        (4, [[0, 1], [1, 2], [2, 3]], True, "Valid tree, straight line"),
        (
            5,
            [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]],
            False,
            "Circular graph forming one large cycle",
        ),
        (2, [[0, 1]], True, "Two nodes, one edge"),
        (3, [[0, 1], [0, 2]], True, "Three nodes, simple valid tree"),
    ]

    all_passed = True
    for i, (n, edges, expected, desc) in enumerate(test_cases, 1):
        # Passing a copy of edges just in case the implementation modifies the input list
        result = sol.validTree(n, [edge[:] for edge in edges])

        if result == expected:
            print(f"✅ Test {i} Passed: {desc}")
        else:
            print(f"❌ Test {i} Failed: {desc}")
            print(f"   Input: n = {n}, edges = {edges}")
            print(f"   Expected: {expected}, but got: {result}")
            all_passed = False

    print("-" * 30)
    if all_passed:
        print("🎉 All test cases passed!")
    else:
        print("⚠️ Some test cases failed. Review your logic.")


if __name__ == "__main__":
    run_tests()
