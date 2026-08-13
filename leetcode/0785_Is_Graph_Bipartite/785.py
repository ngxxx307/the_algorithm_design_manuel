from collections import deque


# Leave this empty for your implementation
class Solution:

    def isBipartite(self, graph: list[list[int]]) -> bool:
        visited = [False] * len(graph)
        labels: list[bool | None] = [None] * len(graph)
        if not graph:
            return True

        def _bfs(node: int):
            queue = deque([node])
            visited[0] = True
            labels[0] = True
            while queue:
                node = queue.popleft()
                edges = graph[node]
                for e in edges:
                    if visited[e]:
                        if labels[e] == labels[node]:
                            return False
                        continue
                    visited[e] = True
                    labels[e] = not labels[node]
                    queue.append(e)
            return True

        for v in range(len(graph)):
            if not visited[v]:
                status = _bfs(v)
                if not status:
                    return False

        return True


# --- Test Suite ---
def run_tests():
    sol = Solution()

    test_cases = [
        # (Input 'graph', Expected output, Description)
        (
            [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]],
            False,
            "Example 1: Complete graph subset (contains a triangle)",
        ),
        (
            [[1, 3], [0, 2], [1, 3], [0, 2]],
            True,
            "Example 2: Standard bipartite graph (square)",
        ),
        ([[], [], []], True, "Disconnected graph with no edges"),
        (
            [[1], [0], [3], [2]],
            True,
            "Disconnected graph with independent bipartite components",
        ),
        (
            [[1, 2], [0, 2], [0, 1], []],
            False,
            "Disconnected graph where one component is not bipartite (triangle)",
        ),
        (
            [[1, 2], [0], [0]],
            True,
            "Tree structure (Star graph), which is always bipartite",
        ),
        ([[1], [0, 2], [1, 3], [2]], True, "Linear path graph (0 - 1 - 2 - 3)"),
        (
            [[1, 2, 3], [0], [0], [0]],
            True,
            "Bipartite graph with one node connected to all others",
        ),
        (
            [[1, 4], [0, 2], [1, 3], [2, 4], [0, 3]],
            False,
            "Odd length cycle (Pentagon, 5 nodes)",
        ),
        (
            [
                [],
                [2, 4, 6],
                [1, 4, 8, 9],
                [7, 8],
                [1, 2, 8, 9],
                [6, 9],
                [1, 5, 7, 8, 9],
                [3, 6, 9],
                [2, 3, 4, 6, 9],
                [2, 4, 5, 6, 7, 8],
            ],
            False,
            "",
        ),
    ]

    all_passed = True
    for i, (graph, expected, desc) in enumerate(test_cases, 1):
        result = sol.isBipartite(graph)
        if result == expected:
            print(f"✅ Test {i} Passed: {desc}")
        else:
            print(f"❌ Test {i} Failed: {desc}")
            print(f"   Input: graph = {graph}")
            print(f"   Expected: {expected}, but got: {result}")
            all_passed = False

    print("-" * 30)
    if all_passed:
        print("🎉 All test cases passed!")
    else:
        print("⚠️ Some test cases failed. Review your logic.")


if __name__ == "__main__":
    run_tests()
