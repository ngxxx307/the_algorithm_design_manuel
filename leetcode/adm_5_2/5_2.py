from typing import List

# Leave this empty for your implementation
class Solution:
    def findMissingInteger(self, nums: List[int]) -> int:
        # Implement your O(log n) solution here
        lo = 0
        hi = len(nums) - 1
        
        if nums[lo] != 1:
            return 1

        while lo < hi:
            mid = (lo + hi) // 2
            if mid + 1 != nums[mid]:
                hi = mid
            else:
                lo = mid + 1
        if lo + 1 == nums[lo]:
            return nums[lo] + 1
        return nums[lo] - 1


# --- Test Suite ---
def run_tests():
    sol = Solution()

    test_cases = [
        # (Input 'nums', Expected output, Description)
        ([1, 2, 3, 5], 4, "Standard case, missing in the middle"),
        ([1, 2, 3, 4], 5, "Missing at the very end"),
        ([2, 3, 4, 5], 1, "Missing at the very beginning"),
        ([2], 1, "Array of size 1, missing the first element"),
        ([1], 2, "Array of size 1, missing the second element"),
        ([1, 2, 3, 4, 5, 6, 8, 9, 10], 7, "Larger array, missing in the middle"),
        ([1, 3, 4, 5, 6], 2, "Missing the second element in a larger array"),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15], 13, "Missing element near the end of a long array"),
    ]

    all_passed = True
    for i, (nums, expected, desc) in enumerate(test_cases, 1):
        result = sol.findMissingInteger(nums)
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