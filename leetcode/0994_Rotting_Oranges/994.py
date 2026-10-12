import unittest
from collections import deque


# Leave this empty for your implementation
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        n_cols = len(grid[0])
        n_rows = len(grid)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def neighbor(i: int, j: int):
            for x, y in directions:
                new_i, new_j = i + x, j + y
                if (
                    new_i < 0
                    or new_j < 0
                    or new_i > n_rows - 1
                    or new_j > n_cols - 1
                    or grid[new_i][new_j] != 1
                ):
                    continue
                yield new_i, new_j

        n_orange = 0
        count = 0
        queue = deque([])
        visited = [[False for _ in range(n_cols)] for _ in range(n_rows)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    n_orange += 1
                elif grid[i][j] == 2:
                    n_orange += 1
                    queue.append((i, j, 0))
                    visited[i][j] = True
                    count += 1
        rate = 0
        while queue:
            i, j, c = queue.popleft()
            rate = max(rate, c)
            for new_i, new_j in neighbor(i, j):
                if not visited[new_i][new_j]:
                    count += 1
                    visited[new_i][new_j] = True
                    queue.append((new_i, new_j, c + 1))
        if count != n_orange:
            return -1
        return rate


# --- Test Suite ---
def run_tests():
    sol = Solution()

    test_cases = [
        # (Input grid, Expected output, Description)
        ([[2, 1, 1], [1, 1, 0], [0, 1, 1]], 4, "Standard BFS propagation (Example 1)"),
        ([[2, 1, 1], [0, 1, 1], [1, 0, 1]], -1, "Unreachable fresh orange (Example 2)"),
        ([[0, 2]], 0, "No fresh oranges initially (Example 3)"),
        ([[0, 0], [0, 0]], 0, "Grid with only empty cells"),
        ([[1]], -1, "Single fresh orange with no rotten oranges"),
        ([[2]], 0, "Single rotten orange with no fresh oranges"),
        ([[0]], 0, "Single empty cell"),
        (
            [[2, 1, 1], [1, 1, 1], [1, 1, 2]],
            2,
            "Simultaneous propagation from multiple sources",
        ),
        ([[2, 1, 0, 1]], -1, "Disconnected unreachable orange separated by empty cell"),
        ([[2, 1, 1, 1, 1]], 4, "1D row propagation"),
        ([[2, 2], [2, 2]], 0, "Grid with only rotten oranges"),
    ]

    all_passed = True
    for i, (grid, expected, desc) in enumerate(test_cases, 1):
        grid_copy = [row[:] for row in grid]
        result = sol.orangesRotting(grid_copy)
        if result == expected:
            print(f"✅ Test {i} Passed: {desc}")
        else:
            print(f"❌ Test {i} Failed: {desc}")
            print(f"   Input: grid = {grid}")
            print(f"   Expected: {expected}, but got: {result}")
            all_passed = False

    print("-" * 30)
    if all_passed:
        print("🎉 All test cases passed!")
    else:
        print("⚠️ Some test cases failed. Review your logic.")


if __name__ == "__main__":
    run_tests()
