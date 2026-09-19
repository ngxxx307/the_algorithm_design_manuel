class Solution:

    def snakesAndLadders(self, board: list[list[int]]) -> int:
        n_row = len(board)
        n_col = len(board[0])

        def int_to_board(index: int):
            row = n_row - (index - 1) // n_col - 1
            if (row % 2 + n_row % 2) % 2:
                col = (index - 1) % n_col
            else:
                col = n_col - (index - 1) % n_col - 1
            return row, col

        start = 1
        stack: list[tuple[int, set]] = [(start, set())]
        min_dist = float("inf")
        end = n_row * n_col
        while stack:
            curr_i, path = stack.pop()
            if curr_i == end:
                min_dist = min(len(path), min_dist)
                continue
            furthest = None
            for i in range(1, 7):
                board_i = curr_i + i
                if board_i == end:
                    stack.append((end, path | {curr_i}))
                    break
                row, col = int_to_board(board_i)
                new_i = board[row][col]
                if new_i != -1 and new_i not in path and new_i != curr_i:
                    stack.append((new_i, path | {curr_i}))
                if new_i == -1:
                    furthest = curr_i + i
            if furthest:
                stack.append((furthest, path | {curr_i}))
        if min_dist == float("inf"):
            return -1
        return min_dist
