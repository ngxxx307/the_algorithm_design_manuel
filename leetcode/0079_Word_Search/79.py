from turtle import back
from typing import List


# Leave this empty for your implementation
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Leave this empty for your implementation
        visited = [[False] * len(board[0]) for _ in range(len(board))]

        def backtrack(pos: int, x: int, y: int):
            if word[pos] != board[x][y]:
                return False
            if pos == len(word) - 1:
                return True
            if x > 0 and not visited[x - 1][y]:
                visited[x - 1][y] = True
                if backtrack(pos + 1, x - 1, y):
                    return True
                visited[x - 1][y] = False
            if y > 0 and not visited[x][y - 1]:
                visited[x][y - 1] = True
                if backtrack(pos + 1, x, y - 1):
                    return True
                visited[x][y - 1] = False
            if x < len(board) - 1 and not visited[x + 1][y]:
                visited[x + 1][y] = True
                if backtrack(pos + 1, x + 1, y):
                    return True
                visited[x + 1][y] = False
            if y < len(board[0]) - 1 and not visited[x][y + 1]:
                visited[x][y + 1] = True
                if backtrack(pos + 1, x, y + 1):
                    return True
                visited[x][y + 1] = False
            return False

        for x in range(len(board)):
            for y in range(len(board[0])):
                visited[x][y] = True
                if backtrack(0, x, y):
                    return True
                visited[x][y] = False
        return False


# --- Test Suite ---
def run_tests():
    sol = Solution()

    test_cases = [
        # (board, word, expected, description)
        # (
        #     [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
        #     "ABCCED",
        #     True,
        #     "Example 1: standard multi-turn valid path",
        # ),
        # (
        #     [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
        #     "SEE",
        #     True,
        #     "Example 2: path starting from interior cell",
        # ),
        # (
        #     [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
        #     "ABCB",
        #     False,
        #     "Example 3: cannot reuse cell / cycle trap",
        # ),
        # (
        #     [["A"]],
        #     "A",
        #     True,
        #     "Boundary: 1x1 board matching single letter",
        # ),
        # (
        #     [["A"]],
        #     "B",
        #     False,
        #     "Boundary: 1x1 board mismatching single letter",
        # ),
        # (
        #     [["A"]],
        #     "AA",
        #     False,
        #     "Boundary: word length exceeds total grid capacity",
        # ),
        # (
        #     [["A", "B", "C", "D"]],
        #     "DCBA",
        #     True,
        #     "1D row grid traversed right-to-left",
        # ),
        # (
        #     [["A"], ["B"], ["C"], ["D"]],
        #     "ABCE",
        #     False,
        #     "1D column grid with dead end mismatch",
        # ),
        # (
        #     [["a", "b"], ["c", "d"]],
        #     "AB",
        #     False,
        #     "Case sensitivity: uppercase word on lowercase board",
        # ),
        # (
        #     [["A", "B"], ["C", "D"]],
        #     "ABZ",
        #     False,
        #     "Pruning: character not present anywhere on board",
        # ),
        # (
        #     [["A", "B"], ["C", "D"]],
        #     "ABDC",
        #     True,
        #     "Small loop visiting all 4 cells in 2x2 grid",
        # ),
        # (
        #     [
        #         ["A", "B", "C", "D"],
        #         ["H", "G", "F", "E"],
        #         ["I", "J", "K", "L"],
        #         ["P", "O", "N", "M"],
        #     ],
        #     "ABCDEFGHIJKLMNO",
        #     True,
        #     "Constraint boundary: max word length (15) serpentine path",
        # ),
        (
            [
                [
                    "A",
                    "A",
                ]
            ],
            "AAA",
            False,
            "leetcode",
        ),
    ]

    all_passed = True
    for i, (board, word, expected, desc) in enumerate(test_cases, 1):
        # Deep copy board to protect against in-place board modification side effects
        board_copy = [row[:] for row in board]
        result = sol.exist(board_copy, word)

        if result == expected:
            print(f"✅ Test {i} Passed: {desc}")
        else:
            print(f"❌ Test {i} Failed: {desc}")
            print(f'   Input: board = {board}, word = "{word}"')
            print(f"   Expected: {expected}, but got: {result}")
            all_passed = False

    print("-" * 40)
    if all_passed:
        print("🎉 All test cases passed!")
    else:
        print("⚠️ Some test cases failed. Review your logic.")


if __name__ == "__main__":
    run_tests()
