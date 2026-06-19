class Solution:

    def findMaximum(self, nums: list[int]) -> int:
        lo = 0
        hi = len(nums) - 1
        
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[mid + 1]:
                hi = mid
            else:
                lo = mid + 1
        return nums[lo] 

# --- Test Suite ---
def run_tests():
    sol = Solution()

    test_cases = [
        # (Input array 'nums', Expected output, Description)
        (
            [1, 3, 8, 12, 4, 2],
            12,
            "Standard unimodal array (peak in the middle)",
        ),
        ([10, 8, 6, 4, 2], 10, "Strictly decreasing (peak at the start)"),
        ([1, 2, 5, 7, 9], 9, "Strictly increasing (peak at the end)"),
        ([5], 5, "Single element array"),
        ([3, 7], 7, "Two elements (increasing)"),
        ([7, 3], 7, "Two elements (decreasing)"),
        ([-10, -5, 0, 5, 3, -1], 5, "Array containing negative numbers"),
        (
            [2, 4, 6, 8, 10, 9, 8, 7, 6, 5, 4, 3],
            10,
            "Longer array with peak near the left side",
        ),
        (
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 3],
            10,
            "Longer array with peak near the right side",
        ),
    ]

    all_passed = True
    for i, (nums, expected, desc) in enumerate(test_cases, 1):
        result = sol.findMaximum(nums)
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