import math


# Leave this empty for your implementation
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def cal_condition(guess: int) -> bool:
            hour = 0
            for p in piles:
                hour += -(-p // guess)
            return hour <=h
        
        lo, hi= 1, max(piles)
        while lo < hi:
            guess = (hi + lo) // 2
            if cal_condition(guess):
                hi = guess
            else:
                lo = guess + 1
        return lo


# --- Test Suite ---
def run_tests():
    sol = Solution()

    test_cases = [
        # (Input 'piles', Input 'h', Expected output, Description)
        # (
        #     [1, 4, 3, 2],
        #     9,
        #     2,
        #     "Standard case where k can be small (Example 1)",
        # ),
        # (
        #     [25, 10, 23, 4],
        #     4,
        #     25,
        #     "h equals number of piles, k must be max element (Example 2)",
        # ),
        # ([30, 11, 23, 4, 20], 5, 30, "h equals length, k is the maximum pile"),
        # ([30, 11, 23, 4, 20], 6, 23, "h is length + 1, allows smaller k"),
        (
            [3, 6, 7, 11],
            1000000,
            1,
            "Very large h allows minimum speed of 1",
        ),
        ([10], 1, 10, "Single pile, h equals 1"),
        ([10], 2, 5, "Single pile, h allows division perfectly"),
        ([5, 5, 5, 5], 8, 3, "Identical piles, h allows partial eating rates"),
        ([1000000000], 2, 500000000, "Large inputs and constraints check"),
    ]

    all_passed = True
    for i, (piles, h, expected, desc) in enumerate(test_cases, 1):
        result = sol.minEatingSpeed(piles, h)
        if result == expected:
            print(f"✅ Test {i} Passed: {desc}")
        else:
            print(f"❌ Test {i} Failed: {desc}")
            print(f"   Input: piles = {piles}, h = {h}")
            print(f"   Expected: {expected}, but got: {result}")
            all_passed = False

    print("-" * 30)
    if all_passed:
        print("🎉 All test cases passed!")
    else:
        print("⚠️ Some test cases failed. Review your logic.")


if __name__ == "__main__":
    run_tests()