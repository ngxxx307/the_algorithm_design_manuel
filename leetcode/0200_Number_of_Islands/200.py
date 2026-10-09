import copy
import unittest

from collections import deque


# Leave this empty for your implementation
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        n_row = len(grid)  # num rows
        n_col = len(grid[0])  # num cols

        def is_neighbor(i: int, j: int):
            return (
                not (i < 0 or i > n_row - 1 or j < 0 or j > n_col - 1)
                and grid[i][j] == "1"
            )

        discovered = [[False for _ in range(n_col)] for _ in range(n_row)]

        parents: list[list[tuple | None]] = [
            [None for _ in range(n_col)] for _ in range(n_row)
        ]
        count = 0
        for i in range(n_row):
            for j in range(n_col):
                if not discovered[i][j] and grid[i][j] == "1":
                    queue = deque([(i, j)])
                    count += 1
                    while queue:
                        curr_i, curr_j = queue.popleft()
                        for x, y in direction:
                            new_i, new_j = curr_i + x, curr_j + y
                            if (
                                is_neighbor(new_i, new_j)
                                and not discovered[new_i][new_j]
                            ):
                                queue.append((new_i, new_j))
                                discovered[new_i][new_j] = True
                                parents[new_i][new_j] = (curr_i, curr_j)

        return count


# --- Test Suite ---
def run_tests():
    sol = Solution()

    test_cases = [
        # (Input grid, Expected output, Description)
        (
            [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ],
            1,
            "Single connected island (Example 1)",
        ),
        (
            [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ],
            3,
            "Multiple disconnected islands (Example 2)",
        ),
        (
            [["1"]],
            1,
            "Single land cell",
        ),
        (
            [["0"]],
            0,
            "Single water cell",
        ),
        (
            [
                ["1", "1"],
                ["1", "1"],
            ],
            1,
            "All land grid",
        ),
        (
            [
                ["0", "0"],
                ["0", "0"],
            ],
            0,
            "All water grid",
        ),
        (
            [
                ["1", "0"],
                ["0", "1"],
            ],
            2,
            "Diagonally adjacent lands (should count as separate islands)",
        ),
        (
            [["1", "0", "1", "1", "0", "1"]],
            3,
            "1D horizontal row grid",
        ),
        (
            [["1"], ["0"], ["1"], ["0"], ["1"], ["1"]],
            3,
            "1D vertical column grid",
        ),
        (
            [
                ["1", "1", "1"],
                ["1", "0", "1"],
                ["1", "1", "1"],
            ],
            1,
            "Ring-shaped island surrounding water",
        ),
    ]

    all_passed = True
    for i, (grid, expected, desc) in enumerate(test_cases, 1):
        grid_copy = copy.deepcopy(grid)
        result = sol.numIslands(grid_copy)

        if result == expected:
            print(f"✅ Test {i} Passed: {desc}")
        else:
            print(f"❌ Test {i} Failed: {desc}")
            print(f"   Input grid: {grid}")
            print(f"   Expected: {expected}, but got: {result}")
            all_passed = False

    print("-" * 30)
    if all_passed:
        print("🎉 All test cases passed!")
    else:
        print("⚠️ Some test cases failed. Review your logic.")


if __name__ == "__main__":
    run_tests()
