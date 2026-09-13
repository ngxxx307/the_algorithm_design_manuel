from collections import deque


class Solution:

    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        print_tree(n, edges)
        if n == 1:
            return [0]
        edge_list: list[list[int]] = [[] for _ in range(n)]
        node_state = ["undiscovered"] * n
        degree = [0] * n

        for e in edges:
            edge_list[e[0]].append(e[1])
            edge_list[e[1]].append(e[0])
            degree[e[0]] += 1
            degree[e[1]] += 1
        queue = []

        for i, d in enumerate(degree):
            if d == 1:
                queue.append(i)
                node_state[i] = "discovered"
        old_queue = []
        while queue:
            new_queue = []
            for src in queue:
                for dest in edge_list[src]:
                    if node_state[dest] == "undiscovered":
                        node_state[dest] = "discovered"
                    degree[dest] -= 1
                    if degree[dest] == 1:
                        new_queue.append(dest)

                node_state[src] = "processed"
            old_queue = queue
            queue = new_queue

        return old_queue


def print_tree(n: int, edges: list[list[int]], root: int = 0) -> None:
    """Prints a visual ASCII tree structure starting from the specified root node."""
    if n == 0:
        print("(Empty tree)")
        return
    if n == 1:
        print("0")
        return

    # Build adjacency list
    adj: list[list[int]] = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    def dfs(curr: int, parent: int, prefix: str) -> None:
        children = [neighbor for neighbor in adj[curr] if neighbor != parent]
        for i, child in enumerate(children):
            is_last = i == len(children) - 1
            connector = "└── " if is_last else "├── "
            print(f"{prefix}{connector}{child}")
            new_prefix = prefix + ("    " if is_last else "│   ")
            dfs(child, curr, new_prefix)

    print(f"Node {root}")
    dfs(root, -1, "")


# --- Test Suite ---
def run_tests():
    sol = Solution()

    test_cases = [
        # (Input 'n', Input 'edges', Expected output, Description)
        # (4, [[1, 0], [1, 2], [1, 3]], [1], "Star graph (Example 1)"),
        # (
        #     6,
        #     [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]],
        #     [3, 4],
        #     "Two MHT roots (Example 2)",
        # ),
        (1, [], [0], "Single node tree"),
        # (2, [[0, 1]], [0, 1], "Two connected nodes"),
        # (3, [[0, 1], [1, 2]], [1], "Line graph with odd length"),
        # (
        #     4,
        #     [[0, 1], [1, 2], [2, 3]],
        #     [1, 2],
        #     "Line graph with even length",
        # ),
        # (
        #     7,
        #     [[0, 1], [1, 2], [1, 3], [2, 4], [3, 5], [3, 6]],
        #     [1],
        #     "Asymmetric tree with single centroid",
        # ),
        # (
        #     6,
        #     [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]],
        #     [0],
        #     "Large star graph centered at 0",
        # ),
    ]

    all_passed = True
    for i, (n, edges, expected, desc) in enumerate(test_cases, 1):
        result = sol.findMinHeightTrees(n, edges)

        # Output order does not matter for this problem
        if result is not None and sorted(result) == sorted(expected):
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
