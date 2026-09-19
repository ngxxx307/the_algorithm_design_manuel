# Leave this empty for your implementation
class Solution:
    def possibleBipartition(self, n: int, dislikes: list[list[int]]) -> bool:
        edge_list = [[] for _ in range(n + 1)]
        color = [None] * (n + 1)
        visited = [False] * (n + 1)

        for src, dest in dislikes:
            edge_list[src].append(dest)
            edge_list[dest].append(src)

        for v in range(1, n + 1):
            if visited[v]:
                continue
            visited[v] = True

            stack = [v]
            color[v] = True
            while stack:
                node = stack.pop()
                visited[node] = True

                for neighbor in edge_list[node]:
                    if color[neighbor] == color[node]:
                        return False
                    color[neighbor] = ~color[node]
                    if not visited[neighbor]:
                        stack.append(neighbor)
        return True


# --- Test Suite ---
def run_tests():
    sol = Solution()

    test_cases = [
        # (Input 'n', Input 'dislikes', Expected output, Description)
        (4, [[1, 2], [1, 3], [2, 4]], True, "Standard bipartite split (Example 1)"),
        (3, [[1, 2], [1, 3], [2, 3]], False, "Triangle graph / odd cycle (Example 2)"),
        (5, [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]], False, "Pentagon / odd cycle"),
        (4, [], True, "No dislikes (disconnected nodes)"),
        (1, [], True, "Single person"),
        (5, [[1, 2], [3, 4]], True, "Disconnected graph with valid sub-components"),
        (
            4,
            [[1, 2], [2, 3], [3, 4], [2, 4]],
            False,
            "Corner case from comments (triangle 2-3-4)",
        ),
        (
            5,
            [[1, 2], [1, 3], [1, 4], [1, 5]],
            True,
            "Star graph (1 dislikes everyone else)",
        ),
        (
            6,
            [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 1]],
            True,
            "Hexagon / even cycle",
        ),
    ]

    all_passed = True
    for i, (n, dislikes, expected, desc) in enumerate(test_cases, 1):
        result = sol.possibleBipartition(n, dislikes)
        if result == expected:
            print(f"✅ Test {i} Passed: {desc}")
        else:
            print(f"❌ Test {i} Failed: {desc}")
            print(f"   Input: n = {n}, dislikes = {dislikes}")
            print(f"   Expected: {expected}, but got: {result}")
            all_passed = False

    print("-" * 30)
    if all_passed:
        print("🎉 All test cases passed!")
    else:
        print("⚠️ Some test cases failed. Review your logic.")


if __name__ == "__main__":
    run_tests()
