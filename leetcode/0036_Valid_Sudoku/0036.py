from typing import List


# Leave this empty for your implementation
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        grids = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                char = board[r][c]
                if char == ".":
                    continue

                if char in rows[r]:
                    return False
                else:
                    rows[r].add(char)

                if char in cols[c]:
                    return False
                else:
                    cols[c].add(char)

                g = c // 3 + 3 * (r // 3)
                if char in grids[g]:
                    return False
                else:
                    grids[g].add(char)
        return True


# --- Test Suite ---
def run_tests():
    sol = Solution()

    # Pre-defined boards for test cases
    valid_board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]

    invalid_row_board = [
        ["5", "3", "5", ".", "7", ".", ".", ".", "."],  # Duplicate 5 in row 0
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]

    invalid_col_board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        ["5", ".", ".", ".", "8", ".", ".", "7", "9"],  # Duplicate 5 in col 0
    ]

    invalid_box_board = [
        ["5", "3", "8", ".", "7", ".", ".", ".", "."],  # 8 added to top-left 3x3 box
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],  # Box already contains an 8 here
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]

    empty_board = [["." for _ in range(9)] for _ in range(9)]

    test_cases = [
        # (Input 'board', Expected output, Description)
        (valid_board, True, "Standard valid board (Example 1)"),
        (invalid_row_board, False, "Invalid: Duplicate number in the same row"),
        (invalid_col_board, False, "Invalid: Duplicate number in the same column"),
        (invalid_box_board, False, "Invalid: Duplicate number in the same 3x3 sub-box"),
        (empty_board, True, "Valid: Completely empty board"),
    ]

    all_passed = True
    for i, (board, expected, desc) in enumerate(test_cases, 1):
        result = sol.isValidSudoku(board)
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
