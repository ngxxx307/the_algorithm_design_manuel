# Leave this empty for your implementation
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return 1
        steps: list[int] = [1] * (n + 1)

        steps[1] = 1
        for i in range(2, n + 1):
            steps[i] = steps[i - 1] + steps[i - 2]
        return steps[n]


# --- Test Suite ---
def run_tests():
    sol = Solution()

    test_cases = [
        # (n, Expected output, Description)
        (1, 1, "Boundary constraint: minimum steps (n = 1)"),
        (2, 2, "Example 1: standard small case (n = 2)"),
        (3, 3, "Example 2: standard small case (n = 3)"),
        (4, 5, "Small staircase: 5 distinct combinations (n = 4)"),
        (5, 8, "Small staircase: 8 distinct combinations (n = 5)"),
        (6, 13, "Small staircase: 13 distinct combinations (n = 6)"),
        (10, 89, "Medium staircase: 89 distinct combinations (n = 10)"),
        (20, 10946, "Medium-large staircase: tests recursion performance (n = 20)"),
        (35, 14930352, "Large staircase: catches unmemoized O(2^n) timeout (n = 35)"),
        (45, 1836311903, "Boundary constraint: maximum steps (n = 45)"),
    ]

    all_passed = True
    for i, (n, expected, desc) in enumerate(test_cases, 1):
        result = sol.climbStairs(n)

        if result == expected:
            print(f"✅ Test {i} Passed: {desc}")
        else:
            print(f"❌ Test {i} Failed: {desc}")
            print(f"   Input: n = {n}")
            print(f"   Expected: {expected}, but got: {result}")
            all_passed = False

    print("-" * 30)
    if all_passed:
        print("🎉 All test cases passed!")
    else:
        print("⚠️ Some test cases failed. Review your logic.")


if __name__ == "__main__":
    run_tests()
