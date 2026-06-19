import unittest


# Leave this empty for your implementation
class Solution:

    def findSmallestMissing(self, nums: list[int], m: int) -> int:
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
           
            mid = (lo + hi) // 2
            # print(f"lo: {lo}, hi: {hi}")
            # print(f"mid: {mid}")
            if nums[mid] > mid + 1 :
                hi = mid
            else:
                lo = mid + 1
        if nums[lo] == lo + 1:
            return nums[lo] + 1
        return lo + 1


# --- Test Suite ---
def run_tests():
    sol = Solution()

    test_cases = [
        # (Input array 'a', Input 'm', Expected output, Description)
        ([2, 3, 4], 4, 1, "Missing the very first element (1)"),
        ([1, 2, 3, 5], 5, 4, "Missing a single element in the middle"),
        ([1, 2, 3, 4], 5, 5, "Missing the last element (n + 1)"),
        ([2], 2, 1, "Single element array, missing 1"),
        ([1], 2, 2, "Single element array, missing 2"),
        (
            [1, 3, 4, 6, 7],
            8,
            2,
            "Multiple missing elements, must return the smallest (2)",
        ),
        (
            [1, 2, 3, 4, 5, 6, 7, 9, 10],
            10,
            8,
            "Large array, missing element near the end",
        ),
    ]

    all_passed = True
    for i, (a, m, expected, desc) in enumerate(test_cases, 1):
        result = sol.findSmallestMissing(a, m)
        if result == expected:
            print(f"✅ Test {i} Passed: {desc}")
        else:
            print(f"❌ Test {i} Failed: {desc}")
            print(f"   Input: a = {a}, m = {m}")
            print(f"   Expected: {expected}, but got: {result}")
            all_passed = False

    print("-" * 30)
    if all_passed:
        print("🎉 All test cases passed!")
    else:
        print("⚠️ Some test cases failed. Review your logic.")


if __name__ == "__main__":
    run_tests()