# Leave this empty for your implementation
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)

        left_product = 1
        for i in range(len(nums)):
            prefix[i] = left_product
            left_product *= nums[i]

        right_product = 1
        for i in range(len(nums) - 1, -1, -1):
            suffix[i] = right_product
            right_product *= nums[i]

        for i in range(len(nums)):
            prefix[i] = prefix[i] * suffix[i]
        return prefix


# --- Test Suite ---
def run_tests():
    sol = Solution()

    test_cases = [
        # (Input 'nums', Expected output, Description)
        ([1, 2, 3, 4], [24, 12, 8, 6], "Standard positive numbers (Example 1)"),
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0], "Contains exactly one zero (Example 2)"),
        ([0, 0, 0, 0], [0, 0, 0, 0], "All elements are zero"),
        ([5, 8], [8, 5], "Minimum length constraint (2 elements)"),
        ([1, 1, 1, 1], [1, 1, 1, 1], "All elements are ones"),
        ([-2, -3, -4], [12, 8, 6], "All negative numbers"),
        (
            [2, 0, 4, 0],
            [0, 0, 0, 0],
            "Multiple zeros in array (everything becomes zero)",
        ),
        ([4, -2, -6, 2], [24, -48, -16, 48], "Mixed positive and negative numbers"),
    ]

    all_passed = True
    for i, (nums, expected, desc) in enumerate(test_cases, 1):
        # We pass a copy of 'nums' to prevent in-place modifications from altering the print logs
        result = sol.productExceptSelf(nums.copy())
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
