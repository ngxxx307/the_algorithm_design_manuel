import unittest

class Solution:

    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        n_cols = len(matrix[0])
        n_rows = len(matrix)
        def to_x_y(index: int):
            x = index // n_cols
            y = index % n_cols
            return x, y
        
        lo = 0
        hi = n_cols * n_rows - 1

        while lo <hi:
            mid = (hi + lo)//2
            x, y = to_x_y(mid)
            if matrix[x][y] >= target:
                hi = mid
            else:
                lo = mid + 1
        
        x, y = to_x_y(lo)
        if matrix[x][y] == target:
            return True
        return False


# --- Test Suite ---
def run_tests():
    sol = Solution()

    test_cases = [
        # (Input matrix, Input target, Expected output, Description)
        # (
        #     [[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]],
        #     10,
        #     True,
        #     "Target exists in the middle (Example 1)",
        # ),
        # (
        #     [[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]],
        #     15,
        #     False,
        #     "Target does not exist (Example 2)",
        # ),
        # ([[5]], 5, True, "Single element matrix - target exists"),
        # ([[5]], 2, False, "Single element matrix - target does not exist"),
        ([[1, 3, 5, 7]], 3, True, "Single row matrix - target exists"),
        ([[1, 3, 5, 7]], 6, False, "Single row matrix - target does not exist"),
        ([[1], [3], [5]], 5, True, "Single column matrix - target exists"),
        ([[1], [3], [5]], 4, False, "Single column matrix - target does not exist"),
        (
            [[10, 20], [30, 40]],
            5,
            False,
            "Target is smaller than the absolute minimum",
        ),
        (
            [[10, 20], [30, 40]],
            50,
            False,
            "Target is larger than the absolute maximum",
        ),
        ([[1, 2], [3, 4]], 1, True, "Target is the first element (top-left)"),
        ([[1, 2], [3, 4]], 4, True, "Target is the last element (bottom-right)"),
        (
            [[-10, -8, -5], [-3, -1, 2], [4, 7, 9]],
            -1,
            True,
            "Matrix contains negative numbers - target exists",
        ),
    ]

    all_passed = True
    for i, (matrix, target, expected, desc) in enumerate(test_cases, 1):
        result = sol.searchMatrix(matrix, target)
        if result == expected:
            print(f"✅ Test {i} Passed: {desc}")
        else:
            print(f"❌ Test {i} Failed: {desc}")
            print(f"   Input: matrix = {matrix}, target = {target}")
            print(f"   Expected: {expected}, but got: {result}")
            all_passed = False

    print("-" * 30)
    if all_passed:
        print("🎉 All test cases passed!")
    else:
        print("⚠️ Some test cases failed. Review your logic.")


if __name__ == "__main__":
    run_tests()