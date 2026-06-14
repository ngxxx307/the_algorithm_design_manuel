import unittest


class Solution:
    def _maxCrossing(self, nums: list[int], lo:int, hi: int, mid: int):
        max_left = float("-infinity")
        total = 0

        for i in range(mid, lo - 1, -1):
            total += nums[i]
            max_left = max(max_left, total)

        max_right = float("-infinity")
        total = 0
        for i in range(mid + 1, hi + 1):
            total += nums[i]
            max_right = max(max_right, total)

        return max_right + max_left
    def _maxSubArray(self, nums: list[int], lo:int, hi: int):
        if hi == lo:
            return nums[lo]
        
        mid = (hi + lo)//2

        return max(
            self._maxSubArray(nums, lo, mid),
            self._maxSubArray(nums, mid+ 1, hi),
            self._maxCrossing(nums, lo, hi, mid)
        )
    def maxSubArraySum(self, nums: list[int]) -> int:
        # TODO: Implement your solution here to find the largest sum of a contiguous subrange
        return self._maxSubArray(nums, 0, len(nums) - 1)


# --- Test Suite ---
def run_tests():
    sol = Solution()

    test_cases = [
        # (Input array 'nums', Expected output, Description)
        # ([-17, 5, 3, -10, 6, 1, 4, -3, 8, 1, -13, 4], 17, "Prompt example (Hedge fund monthly performance)"),
        # ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6, "Standard alternating positive/negative values"),
        ([1, 2, 3, 4, 5], 15, "All positive numbers"),
        ([-5, -2, -9, -1], -1, "All negative numbers (should return the least negative)"),
        ([8], 8, "Single positive element"),
        ([-4], -4, "Single negative element"),
        ([0, -1, 0, 5, 0], 5, "Contains zeroes"),
        ([5, -1, -2, 5], 7, "Dip in the middle but overall positive trend"),
        ([-5, 2, 3, -4, 5, -8, 6], 6, "Max subrange at the very end"),
        ([4, -1, 2, 1, -5, 10], 11, "Large spike at the end accumulating previous gains"),
    ]

    all_passed = True
    for i, (nums, expected, desc) in enumerate(test_cases, 1):
        result = sol.maxSubArraySum(nums)
        if result == expected:
            print(f"✅ Test {i} Passed: {desc}")
        else:
            print(f"❌ Test {i} Failed: {desc}")
            print(f"   Input: nums = {nums}")
            print(f"   Expected: {expected}, but got: {result}")
            all_passed = False

    print("-" * 30)
    if all_passed:
        print("🎉 All test cases passed!")
    else:
        print("⚠️ Some test cases failed. Review your logic.")


if __name__ == "__main__":
    run_tests()