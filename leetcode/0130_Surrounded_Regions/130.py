import unittest
import copy


# Leave this empty for your implementation
class Solution:
    def solve(self, board: list[list[str]]) -> None:
        n_rows = len(board)
        n_cols = len(board[0])

        def dfs(i: int, j: int, visited: set) -> bool:
            if i < 0 or i > n_rows - 1 or j < 0 or j > n_cols - 1:
                return True
            if board[i][j] == "X" or (i, j) in visited:
                return False

            visited.add((i, j))
            return (
                dfs(i + 1, j, visited)
                or dfs(i - 1, j, visited)
                or dfs(i, j - 1, visited)
                or dfs(i, j + 1, visited)
            )

        visited = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and (i, j) not in visited:
                    visited = set()
                    b = dfs(i, j, visited)
                    if not b:
                        for x, y in visited:
                            board[x][y] = "X"


# --- Test Suite ---
def run_tests():
    sol = Solution()

    test_cases = [
        # (Input 'board', Expected output, Description)
        (
            [
                ["X", "X", "X", "X"],
                ["X", "O", "O", "X"],
                ["X", "X", "O", "X"],
                ["X", "O", "X", "X"],
            ],
            [
                ["X", "X", "X", "X"],
                ["X", "X", "X", "X"],
                ["X", "X", "X", "X"],
                ["X", "O", "X", "X"],
            ],
            "Standard case (Example 1) - Inner O's flipped, edge O kept",
        ),
        ([["X"]], [["X"]], "Single character 'X' (Example 2)"),
        ([["O"]], [["O"]], "Single character 'O' - touches edge so not captured"),
        (
            [
                ["X", "X", "X", "X", "X"],
                ["X", "O", "O", "O", "X"],
                ["X", "O", "O", "O", "X"],
                ["X", "O", "O", "O", "X"],
                ["X", "X", "X", "X", "X"],
            ],
            [
                ["X", "X", "X", "X", "X"],
                ["X", "X", "X", "X", "X"],
                ["X", "X", "X", "X", "X"],
                ["X", "X", "X", "X", "X"],
                ["X", "X", "X", "X", "X"],
            ],
            "Large fully surrounded block of O's",
        ),
        (
            [["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]],
            [["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]],
            "All O's - everything touches an edge",
        ),
        (
            [
                ["X", "X", "X", "X"],
                ["X", "O", "O", "X"],
                ["X", "O", "X", "X"],
                ["X", "O", "X", "X"],
            ],
            [
                ["X", "X", "X", "X"],
                ["X", "O", "O", "X"],
                ["X", "O", "X", "X"],
                ["X", "O", "X", "X"],
            ],
            "O's snaking to the edge - none should be captured",
        ),
        (
            [
                ["O", "X", "X", "O", "X"],
                ["X", "O", "O", "X", "O"],
                ["X", "O", "X", "O", "X"],
                ["O", "X", "O", "O", "O"],
                ["X", "X", "O", "X", "O"],
            ],
            [
                ["O", "X", "X", "O", "X"],
                ["X", "X", "X", "X", "O"],
                ["X", "X", "X", "O", "X"],
                ["O", "X", "O", "O", "O"],
                ["X", "X", "O", "X", "O"],
            ],
            "Complex board with multiple isolated and connected regions",
        ),
    ]

    all_passed = True
    for i, (board, expected, desc) in enumerate(test_cases, 1):
        # We need to deep copy the board because it's modified in-place
        board_copy = copy.deepcopy(board)

        sol.solve(board_copy)

        if board_copy == expected:
            print(f"✅ Test {i} Passed: {desc}")
        else:
            print(f"❌ Test {i} Failed: {desc}")
            print(f"   Input: board = {board}")
            print(f"   Expected: {expected}")
            print(f"   Got:      {board_copy}")
            all_passed = False

    print("-" * 30)
    if all_passed:
        print("🎉 All test cases passed!")
    else:
        print("⚠️ Some test cases failed. Review your logic.")
        print(
            "💡 Hint for your error: A RecursionError usually means your DFS is visiting the same cells infinitely. Make sure you are marking 'visited' cells properly so you don't go back and forth between two 'O's!"
        )


if __name__ == "__main__":
    run_tests()
