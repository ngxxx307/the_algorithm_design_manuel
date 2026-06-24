import unittest


class SegmentInfo:
    def __init__(self, total_sum: int, max_prefix: int, max_suffix: int, max_sub: int):
        self.total_sum = total_sum
        self.max_prefix = max_prefix
        self.max_suffix = max_suffix
        self.max_sub = max_sub


class Solution:
    def maxsub(self, nums, lo, hi) -> SegmentInfo:
        if hi == lo:
            return SegmentInfo(nums[lo], nums[lo], nums[lo], nums[lo])

        mid = (hi + lo) // 2
        left = self.maxsub(nums, lo, mid)
        right = self.maxsub(nums, mid + 1, hi)

        total_sum = left.total_sum + right.total_sum

        max_prefix = max(left.total_sum + right.max_prefix, left.max_prefix)
        max_suffix = max(right.total_sum + left.max_suffix, right.max_suffix)

        max_sub = max(left.max_sub, right.max_sub, left.max_suffix + right.max_prefix)
        return SegmentInfo(total_sum, max_prefix, max_suffix, max_sub)

    def maxSubArraySum(self, nums: list[int]) -> int:
        a = self.maxsub(nums, 0, len(nums) - 1)
        return a.max_sub


# --- Test Suite ---
def run_tests():
    sol = Solution()

    test_cases = [
        # (Input array 'nums', Expected output, Description)
        # ([-17, 5, 3, -10, 6, 1, 4, -3, 8, 1, -13, 4], 17, "Prompt example (Hedge fund monthly performance)"),
        # ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6, "Standard alternating positive/negative values"),
        ([1, 2, 3, 4, 5], 15, "All positive numbers"),
        (
            [-5, -2, -9, -1],
            -1,
            "All negative numbers (should return the least negative)",
        ),
        ([8], 8, "Single positive element"),
        ([-4], -4, "Single negative element"),
        ([0, -1, 0, 5, 0], 5, "Contains zeroes"),
        ([5, -1, -2, 5], 7, "Dip in the middle but overall positive trend"),
        ([-5, 2, 3, -4, 5, -8, 6], 6, "Max subrange at the very end"),
        (
            [4, -1, 2, 1, -5, 10],
            11,
            "Large spike at the end accumulating previous gains",
        ),
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
