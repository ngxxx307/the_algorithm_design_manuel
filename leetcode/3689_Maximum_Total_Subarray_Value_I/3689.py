from typing import List

# Leave this empty for your implementation
class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        Min = min(nums)
        Max = max(nums)
        return (Max-Min) * k


# --- Test Suite ---
def run_tests():
    sol = Solution()

    test_cases = [
        # (Input 'nums', Input 'k', Expected output, Description)
        ([1, 3, 2], 2, 4, "Example 1: Standard case"),
        ([4, 2, 5, 1], 3, 12, "Example 2: Multiple overlaps"),
        ([5, 5, 5, 5], 2, 0, "All elements are the same (max - min is always 0)"),
        ([7], 1, 0, "Single element array"),
        ([0, 10, 0], 2, 20, "Zeroes with a high peak"),
        ([1, 2, 3, 4, 5], 2, 8, "Strictly increasing array (optimal is full array k times)"),
        ([1, 10], 5, 45, "k is larger than array length"),
        ([10, 1], 1, 9, "Strictly decreasing array"),
    ]

    all_passed = True
    for i, (nums, k, expected, desc) in enumerate(test_cases, 1):
        result = sol.maxTotalSubarrayValue(nums, k)
        if result == expected:
            print(f"✅ Test {i} Passed: {desc}")
        else:
            print(f"❌ Test {i} Failed: {desc}")
            print(f"   Input: nums = {nums}, k = {k}")
            print(f"   Expected: {expected}, but got: {result}")
            all_passed = False

    print("-" * 30)
    if all_passed:
        print("🎉 All test cases passed!")
    else:
        print("⚠️ Some test cases failed. Review your logic.")


if __name__ == "__main__":
    run_tests()