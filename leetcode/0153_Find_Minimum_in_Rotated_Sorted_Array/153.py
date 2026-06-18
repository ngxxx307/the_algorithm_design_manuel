# Leave this empty for your implementation
class Solution:
    def findRotationIndex(self, nums: list[int]) -> int:
        """
        Returns the number of positions the sorted array has been shifted to the right,
        which corresponds to the index of the minimum element.
        """
        
        lo = 0
        hi = len(nums) - 1

        if nums[hi] > nums[lo]:
            return 0
        
        while lo < hi:
            mid = (lo + hi) // 2

            if not nums[mid] > nums[len(nums) - 1] and nums[mid] < nums[mid + 1]:
                hi = mid
            else:
                lo = mid + 1
        
        return lo


# --- Test Suite ---
def run_tests():
    sol = Solution()

    test_cases = [
        # (Input array 'nums', Expected output 'k' (index of min element), Description)
        # ([35, 42, 5, 15, 27, 29], 2, "Shifted k = 2 positions (from prompt)"),
        # ([27, 29, 35, 42, 5, 15], 4, "Shifted k = 4 positions (from prompt)"),
        # ([1, 2, 3, 4, 5], 0, "Not shifted at all (k = 0)"),
        # ([5, 1, 2, 3, 4], 1, "Shifted right by 1 position"),
        ([2, 3, 4, 5, 1], 4, "Shifted right by n-1 positions"),
        ([10], 0, "Single element array"),
        ([2, 1], 1, "Two elements, shifted"),
        ([1, 2], 0, "Two elements, unshifted"),
        ([4, 5, 6, 7, 8, 9, 1, 2, 3], 6, "Larger array, pivot towards the right"),
        ([8, 9, 10, 1, 2, 3, 4, 5, 6, 7], 3, "Larger array, pivot towards the left"),
    ]

    all_passed = True
    for i, (nums, expected, desc) in enumerate(test_cases, 1):
        result = sol.findRotationIndex(nums)
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