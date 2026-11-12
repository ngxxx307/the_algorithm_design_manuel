from typing import List


# Leave this empty for your implementation
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[1], nums[0])

        max_rob = [0] * len(nums)

        max_rob[0] = nums[0]
        max_rob[1] = nums[1]
        max_rob[2] = nums[0] + nums[2]

        for i in range(3, len(nums)):
            max_rob[i] = max(max_rob[i - 2], max_rob[i - 3]) + nums[i]
        return max(max_rob[len(max_rob) - 1], max_rob[len(max_rob) - 2])


# --- Test Suite ---
def run_tests():
    sol = Solution()

    test_cases = [
        # (nums, Expected output, Description)
        ([1, 2, 3, 1], 4, "Example 1: standard small street (1 + 3 = 4)"),
        ([2, 7, 9, 3, 1], 12, "Example 2: standard medium street (2 + 9 + 1 = 12)"),
        ([5], 5, "Boundary constraint: single house (n = 1)"),
        ([0], 0, "Boundary constraint: single empty house (n = 1, val = 0)"),
        ([10, 20], 20, "Boundary constraint: two houses (n = 2), pick larger"),
        ([2, 1, 1, 2], 4, "Edge case: skipping two adjacent houses (2 + 2 = 4)"),
        ([0, 0, 0, 0, 0], 0, "Edge case: all zero-value houses"),
        (
            [400, 0, 400, 0, 400],
            1200,
            "Edge case: alternating max value (400) and zero",
        ),
        ([1, 2, 3, 4, 5, 6], 12, "Strictly increasing values (2 + 4 + 6 = 12)"),
        ([6, 5, 4, 3, 2, 1], 12, "Strictly decreasing values (6 + 4 + 2 = 12)"),
        ([100, 1, 1, 100, 1, 1, 100], 300, "Edge case: multiple two-house skips"),
        (
            [400] * 100,
            20000,
            "Boundary constraint: max length (n = 100) and max values (400)",
        ),
    ]

    all_passed = True
    for i, (nums, expected, desc) in enumerate(test_cases, 1):
        # Pass a shallow copy to prevent in-place DP mutations from affecting test state
        result = sol.rob(nums[:])

        if result == expected:
            print(f"✅ Test {i} Passed: {desc}")
        else:
            print(f"❌ Test {i} Failed: {desc}")
            print(
                f"   Input: nums = {nums if len(nums) <= 20 else f'[{nums[0]}, ...] (len={len(nums)})'}"
            )
            print(f"   Expected: {expected}, but got: {result}")
            all_passed = False

    print("-" * 30)
    if all_passed:
        print("🎉 All test cases passed!")
    else:
        print("⚠️ Some test cases failed. Review your logic.")


if __name__ == "__main__":
    run_tests()
