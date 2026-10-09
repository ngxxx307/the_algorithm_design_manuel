from collections import deque
import unittest


# Leave this empty for your implementation
class Solution:

    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        def isneighbor(i: int, j: int):
            return (
                not (i < 0 or i > n_rows - 1 or j < 0 or j > n_cols - 1) and grid[i][j]
            )

        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        n_rows = len(grid)
        n_cols = len(grid[0])
        discovered = [[False] * n_cols for _ in range(n_rows)]
        max_size = 0
        for i in range(n_rows):
            for j in range(n_cols):
                if grid[i][j] and not discovered[i][j]:
                    queue = deque([(i, j)])
                    size = 0
                    discovered[i][j] = True
                    while queue:
                        curr_i, curr_j = queue.popleft()
                        size += 1
                        for x, y in direction:
                            new_i, new_j = curr_i + x, curr_j + y
                            if (
                                isneighbor(new_i, new_j)
                                and not discovered[new_i][new_j]
                            ):
                                discovered[new_i][new_j] = True
                                queue.append((new_i, new_j))
                    max_size = max(max_size, size)
        return max_size


# --- Test Suite ---
def run_tests():
    sol = Solution()

    test_cases = [
        # (Input 'grid', Expected output, Description)
        (
            [
                [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            ],
            6,
            "Standard multi-island grid (Example 1)",
        ),
        (
            [[0, 0, 0, 0, 0, 0, 0, 0]],
            0,
            "All water cells (Example 2)",
        ),
        (
            [[1]],
            1,
            "Single cell grid containing land",
        ),
        (
            [[0]],
            0,
            "Single cell grid containing water",
        ),
        (
            [[1, 1, 1, 1, 1]],
            5,
            "1D horizontal strip island",
        ),
        (
            [[1], [1], [1], [1]],
            4,
            "1D vertical strip island",
        ),
        (
            [
                [1, 0, 1],
                [0, 1, 0],
                [1, 0, 1],
            ],
            1,
            "Diagonal land cells (no 4-directional connection)",
        ),
        (
            [
                [1, 1, 0, 0, 0],
                [1, 1, 0, 0, 0],
                [0, 0, 0, 1, 1],
                [0, 0, 0, 1, 1],
            ],
            4,
            "Multiple disjoint islands of equal max size",
        ),
        (
            [
                [1, 1, 1],
                [1, 0, 1],
                [1, 1, 1],
            ],
            8,
            "Ring island surrounding water in center",
        ),
        (
            [
                [1, 1, 1, 1],
                [1, 1, 1, 1],
                [1, 1, 1, 1],
            ],
            12,
            "Entire grid is a single large island",
        ),
    ]

    all_passed = True
    for i, (grid, expected, desc) in enumerate(test_cases, 1):
        result = sol.maxAreaOfIsland(grid)
        if result == expected:
            print(f"✅ Test {i} Passed: {desc}")
        else:
            print(f"❌ Test {i} Failed: {desc}")
            print(f"   Expected: {expected}, but got: {result}")
            all_passed = False

    print("-" * 30)
    if all_passed:
        print("🎉 All test cases passed!")
    else:
        print("⚠️ Some test cases failed. Review your logic.")


if __name__ == "__main__":
    run_tests()
