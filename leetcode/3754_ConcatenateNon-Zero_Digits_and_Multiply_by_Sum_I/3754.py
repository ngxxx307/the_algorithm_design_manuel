import unittest


class Solution:


    def sumAndMultiply(self, n: int) -> int:
        # 🚨 PLACE YOUR IMPLEMENTATION HERE 🚨
        Sum = 0
        Total = 0
        curr = 1
        while n != 0:
            bit = n % 10
            if bit:
                Sum += bit
                Total += bit * curr
                curr *= 10
            n = n // 10
        return Total * Sum

# --- Test Suite ---
def run_tests():
    sol = Solution()

    test_cases = [
        # (Input 'n', Expected output, Description)
        (10203004, 12340, "Standard mixed digits and zeros (Example 1)"),
        (1000, 1, "Single non-zero followed by multiple zeros (Example 2)"),
        (0, 0, "Edge Case: Input is exactly 0"),
        (5, 25, "Edge Case: Single non-zero digit"),
        (40506, 6840, "Intermittent single zeros between digits"),
        (700000008, 1170, "Large gap of multiple zeros between digits"),
        (1000000000, 1, "Upper bound constraint with trailing zeros ($10^9$)"),
        (
            999999999,
            80999999919,
            "Upper bound constraint with all max non-zero digits",
        ),
    ]

    all_passed = True
    for i, (n, expected, desc) in enumerate(test_cases, 1):
        result = sol.sumAndMultiply(n)
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