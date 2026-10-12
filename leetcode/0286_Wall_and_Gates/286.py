import copy
from collections import deque

INF = 2147483647


# Leave this empty for your implementation
class Solution:

    def islandsAndTreasure(self, grid: list[list[int]]) -> None:
        if not grid:
            return None
        n_rows = len(grid)
        n_cols = len(grid[0])
        visited = [[False for _ in range(n_cols)] for _ in range(n_rows)]

        def neighbor(i: int, j: int):
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for x, y in directions:
                if i + x < 0 or i + x > n_rows - 1 or j + y < 0 or j + y > n_cols - 1:
                    continue
                if grid[i + x][j + y] == INF and not visited[i + x][j + y]:
                    yield i + x, j + y

        queue = deque([])
        for i in range(n_rows):
            for j in range(n_cols):
                if grid[i][j] == 0:
                    queue.append((i, j, 0))
        while queue:
            i, j, c = queue.popleft()
            if visited[i][j]:
                continue
            visited[i][j] = True
            grid[i][j] = c
            for new_i, new_j in neighbor(i, j):
                queue.append((new_i, new_j, c + 1))


# --- Test Suite ---
def run_tests():
    sol = Solution()

    test_cases = [
        # (Input grid, Expected grid output, Description)
        (
            [
                [INF, -1, 0, INF],
                [INF, INF, INF, -1],
                [INF, -1, INF, -1],
                [0, -1, INF, INF],
            ],
            [
                [3, -1, 0, 1],
                [2, 2, 1, -1],
                [1, -1, 2, -1],
                [0, -1, 3, 4],
            ],
            "Standard multi-treasure grid (Example 1)",
        ),
        (
            [
                [0, -1],
                [INF, INF],
            ],
            [
                [0, -1],
                [1, 2],
            ],
            "Small grid with wall (Example 2)",
        ),
        (
            [
                [-1, INF],
                [-1, -1],
            ],
            [
                [-1, INF],
                [-1, -1],
            ],
            "Unreachable land cell (remains INF)",
        ),
        (
            [
                [0, 0],
                [0, 0],
            ],
            [
                [0, 0],
                [0, 0],
            ],
            "All treasure chests",
        ),
        (
            [
                [INF],
            ],
            [
                [INF],
            ],
            "Single cell grid with land only",
        ),
        (
            [
                [0],
            ],
            [
                [0],
            ],
            "Single cell grid with treasure",
        ),
        (
            [
                [INF, -1, 0, INF],
            ],
            [
                [INF, -1, 0, 1],
            ],
            "1D grid with a wall blocking access to treasure",
        ),
        (
            [
                [0, -1, INF],
                [-1, -1, -1],
                [INF, -1, 0],
            ],
            [
                [0, -1, INF],
                [-1, -1, -1],
                [INF, -1, 0],
            ],
            "Completely blocked isolated regions",
        ),
        (
            [
                [0, INF, INF, 0],
                [INF, INF, INF, INF],
            ],
            [
                [0, 1, 1, 0],
                [1, 2, 2, 1],
            ],
            "Multiple treasures competing for shortest path distance",
        ),
    ]

    all_passed = True
    for i, (grid_input, expected, desc) in enumerate(test_cases, 1):
        grid = copy.deepcopy(grid_input)
        sol.islandsAndTreasure(grid)

        if grid == expected:
            print(f"✅ Test {i} Passed: {desc}")
        else:
            print(f"❌ Test {i} Failed: {desc}")
            print(f"   Input:    {grid_input}")
            print(f"   Expected: {expected}")
            print(f"   Got:      {grid}")
            all_passed = False

    print("-" * 50)
    if all_passed:
        print("🎉 All test cases passed!")
    else:
        print("⚠️ Some test cases failed. Review your logic.")


if __name__ == "__main__":
    run_tests()
