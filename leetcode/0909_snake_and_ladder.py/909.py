from __future__ import annotations
import unittest
from collections import deque


class Solution:

    def snakesAndLadders(self, board: list[list[int]]) -> int:
        n = len(board)

        def get_coordinates(pos: int) -> tuple[int, int]:
            """Convert 1-based position to (row, col) with zig-zag handling."""
            r, c = divmod(pos - 1, n)
            row = n - 1 - r
            col = c if r % 2 == 0 else n - 1 - c
            return row, col

        queue = deque([(1, 0)])
        visited = set()

        while queue:
            curr_i, moves = queue.popleft()
            furthest = 0
            for i in range(1, 7):
                new_pos = curr_i + i
                if new_pos > n * n:
                    break
                r, c = get_coordinates(new_pos)
                if board[r][c] != -1:
                    new_pos = board[r][c]
                if new_pos == n * n:
                    return moves + 1
                if new_pos not in visited:
                    visited.add(new_pos)
                    if board[r][c] == -1:
                        furthest = max(furthest, new_pos)
                    else:
                        queue.append((new_pos, moves + 1))
            if furthest:
                queue.append((furthest, moves + 1))
        return -1


# --- Test Suite ---
def run_tests():
    sol = Solution()

    test_cases = [
        # (Input 'board', Expected output, Description)
        (
            [
                [-1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1],
                [-1, 35, -1, -1, 13, -1],
                [-1, -1, -1, -1, -1, -1],
                [-1, 15, -1, -1, -1, -1],
            ],
            4,
            "Standard game with snakes and ladders (Example 1)",
        ),
        ([[-1, -1], [-1, 3]], 1, "Small board, jump directly to end (Example 2)"),
        (
            [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]],
            2,
            "No snakes or ladders, just pure dice rolls (3x3 grid)",
        ),
        (
            [[1, -1, -1], [1, 1, 1], [-1, 1, 1]],
            -1,
            "Impossible to win (All reachable squares snake back to start)",
        ),
        ([[-1, -1], [-1, 4]], 1, "Immediate ladder to the winning square"),
        (
            [
                [2, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1],
            ],
            4,
            "",
        ),
    ]

    all_passed = True
    for i, (board, expected, desc) in enumerate(test_cases, 1):
        result = sol.snakesAndLadders(board)
        if result == expected:
            print(f"✅ Test {i} Passed: {desc}")
        else:
            print(f"❌ Test {i} Failed: {desc}")
            print(f"   Input board size: {len(board)}x{len(board)}")
            print(f"   Expected: {expected}, but got: {result}")
            all_passed = False

    print("-" * 30)
    if all_passed:
        print("🎉 All test cases passed!")
    else:
        print("⚠️ Some test cases failed. Review your logic.")


if __name__ == "__main__":
    run_tests()
