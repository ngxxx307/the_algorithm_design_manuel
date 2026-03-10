class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        min_price = float("inf")

        for p in prices:
            if p < min_price:
                min_price = p
            if p - min_price > max_profit:
                max_profit = p - min_price
        return max_profit


# --- Test Suite ---
def run_tests():
    sol = Solution()

    test_cases = [
        # (Input prices, Expected output, Description)
        ([7, 1, 5, 3, 6, 4], 5, "Standard fluctuation (Example 1)"),
        ([7, 6, 4, 3, 1], 0, "Continuous decrease (Example 2)"),
        ([1, 2, 3, 4, 5], 4, "Continuous increase"),
        ([5], 0, "Single day"),
        ([3, 3, 3, 3, 3], 0, "Constant prices"),
        ([0, 10000], 10000, "Extreme values"),
        ([2, 4, 1], 2, "Absolute minimum occurs too late"),
        ([3, 2, 6, 5, 0, 3], 4, "Better profit before the absolute minimum"),
        ([1, 4, 2], 3, "Better profit after a smaller dip"),
    ]

    all_passed = True
    for i, (prices, expected, desc) in enumerate(test_cases, 1):
        result = sol.maxProfit(prices)
        if result == expected:
            print(f"✅ Test {i} Passed: {desc}")
        else:
            print(f"❌ Test {i} Failed: {desc}")
            print(f"   Input: {prices}")
            print(f"   Expected: {expected}, but got: {result}")
            all_passed = False

    print("-" * 30)
    if all_passed:
        print("🎉 All test cases passed!")
    else:
        print("⚠️ Some test cases failed. Review your logic.")


if __name__ == "__main__":
    run_tests()
