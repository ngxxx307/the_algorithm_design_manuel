import unittest
from math import inf
from collections import deque


# Leave this empty for your implementation
class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        n_rows = len(heights)
        n_cols = len(heights[0])

        def neighbor(i: int, j: int):
            for x, y in directions:
                new_i, new_j = x + i, y + j
                if (
                    new_i < 0
                    or new_j < 0
                    or new_i > n_rows - 1
                    or new_j > n_cols - 1
                    or heights[i][j] > heights[new_i][new_j]
                ):
                    continue

                yield new_i, new_j

        if not heights:
            return []
        answer = []

        state = [["undiscovered" for _ in range(n_cols)] for _ in range(n_rows)]
        cache = [[(False, False) for _ in range(n_cols)] for _ in range(n_rows)]

        def dfs(i: int, j: int, p: bool, a: bool):
            nonlocal cache
            state[i][j] = "discovered"
            flow_p, flow_a = cache[i][j]

            if i == 0 or j == 0:
                flow_p = True
            if i == n_rows - 1 or j == n_cols - 1:
                flow_a = True

            flow_a = a or flow_a
            flow_p = p or flow_p

            cache[i][j] = (flow_p, flow_a)
            for new_i, new_j in neighbor(i, j):
                new_p, new_a = cache[new_i][new_j]
                if (flow_a and not new_a) or (flow_p and not new_p):
                    dfs(new_i, new_j, flow_p, flow_a)
            state[i][j] = "processed"
            return

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if state[i][j] == "undiscovered":
                    dfs(i, j, False, False)
        for i in range(n_rows):
            for j in range(n_cols):
                if cache[i][j] == (True, True):
                    answer.append([i, j])
        return answer


# --- Test Suite ---
def run_tests():
    sol = Solution()

    test_cases = [
        # (Input 'heights', Expected output, Description)
        (
            [
                [1, 2, 2, 3, 5],
                [3, 2, 3, 4, 4],
                [2, 4, 5, 3, 1],
                [6, 7, 1, 4, 5],
                [5, 1, 1, 2, 4],
            ],
            [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]],
            "Standard island grid (Example 1)",
        ),
        ([[1]], [[0, 0]], "Single cell island (Example 2)"),
        (
            [[1, 2, 3, 4]],
            [[0, 0], [0, 1], [0, 2], [0, 3]],
            "Single row grid (all cells border both oceans)",
        ),
        (
            [[1], [2], [3], [4]],
            [[0, 0], [1, 0], [2, 0], [3, 0]],
            "Single column grid (all cells border both oceans)",
        ),
        ([[1, 2], [2, 2]], [[0, 1], [1, 0], [1, 1]], "2x2 grid with varying heights"),
        (
            [[2, 2], [2, 2]],
            [[0, 0], [0, 1], [1, 0], [1, 1]],
            "2x2 grid with uniform heights",
        ),
        (
            [[10, 10, 10], [10, 1, 10], [10, 10, 10]],
            [[0, 0], [0, 1], [0, 2], [1, 0], [1, 2], [2, 0], [2, 1], [2, 2]],
            "Central valley unable to flow outward",
        ),
        (
            [[1, 2, 3], [8, 9, 4], [7, 6, 5]],
            [[0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]],
            "High center ridge leading to both oceans",
        ),
    ]

    all_passed = True
    for i, (heights, expected, desc) in enumerate(test_cases, 1):
        result = sol.pacificAtlantic(heights)
        # Sort both lists of coordinates to allow flexible output ordering
        sorted_result = sorted(result) if result else []
        sorted_expected = sorted(expected)
        if sorted_result == sorted_expected:
            print(f"✅ Test {i} Passed: {desc}")
        else:
            print(f"❌ Test {i} Failed: {desc}")
            print(f"   Input: heights = {heights}")
            print(f"   Expected: {expected}, but got: {result}")
            all_passed = False

    print("-" * 30)
    if all_passed:
        print("🎉 All test cases passed!")
    else:
        print("⚠️ Some test cases failed. Review your logic.")


if __name__ == "__main__":
    run_tests()
