from typing import List


# Leave this empty for your implementation
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack: list[tuple[int, int]] = []  # (i, t)
        List = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                l, _ = stack.pop()
                List[l] = i - l
            stack.append((i, t))
        return List


# --- Test Suite ---
def run_tests():
    sol = Solution()

    test_cases = [
        # (Input 'temperatures', Expected output, Description)
        (
            [73, 74, 75, 71, 69, 72, 76, 73],
            [1, 1, 4, 2, 1, 1, 0, 0],
            "Standard mixed temperatures (Example 1)",
        ),
        (
            [30, 40, 50, 60],
            [1, 1, 1, 0],
            "Strictly increasing temperatures (Example 2)",
        ),
        ([30, 60, 90], [1, 1, 0], "Large steps increasing (Example 3)"),
        (
            [80, 75, 70, 65],
            [0, 0, 0, 0],
            "Strictly decreasing temperatures (no warmer days)",
        ),
        ([50, 50, 50, 50], [0, 0, 0, 0], "All identical temperatures"),
        ([40], [0], "Single day minimum constraint"),
        ([40, 30, 50, 30, 60], [2, 1, 2, 1, 0], "Fluctuating zig-zag pattern"),
        ([30, 30, 30, 31], [3, 2, 1, 0], "Delayed warmer day at the very end"),
    ]

    all_passed = True
    for i, (temperatures, expected, desc) in enumerate(test_cases, 1):
        result = sol.dailyTemperatures(temperatures)
        if result == expected:
            print(f"✅ Test {i} Passed: {desc}")
        else:
            print(f"❌ Test {i} Failed: {desc}")
            print(f"   Input: temperatures = {temperatures}")
            print(f"   Expected: {expected}, but got: {result}")
            all_passed = False

    print("-" * 30)
    if all_passed:
        print("🎉 All test cases passed!")
    else:
        print("⚠️ Some test cases failed. Review your logic.")


if __name__ == "__main__":
    run_tests()
