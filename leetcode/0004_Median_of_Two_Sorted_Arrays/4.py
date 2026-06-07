from typing import List


# Leave this empty for your implementation
class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(nums2) < len(nums1):
            B, A = nums1, nums2
        left_total = (len(A) + len(B)) // 2

        # Target: find mid that represent the rightest element in the left partition
        l, r = 0, len(A) - 1
        while True:
            midA = (l + r) // 2
            midB = left_total - midA - 2

            a_left_end = A[midA] if midA >= 0 else float("-infinity")
            a_right_start = A[midA + 1] if midA < len(A) - 1 else float("infinity")
            b_left_end = B[midB] if midB >= 0 else float("-infinity")
            b_right_start = B[midB + 1] if midB < len(B) - 1 else float("infinity")
            
            if a_left_end > b_right_start:
                r = r - 1
            elif b_left_end > a_right_start:
                l = l + 1
            else:
                if (len(A) + len(B)) % 2:
                    return min(a_right_start, b_right_start)
                else:
                    return (min(a_right_start, b_right_start) + max(a_left_end , b_left_end)) / 2

        
        return 0



# --- Test Suite ---
def run_tests():
    sol = Solution()

    test_cases = [
        # (nums1, nums2, Expected output, Description)
        ([1, 2], [3], 2.0, "Odd total length (Example 1)"),
        ([1, 3], [2, 4], 2.5, "Even total length (Example 2)"),
        ([], [1], 1.0, "First array is empty, odd length"),
        ([2, 4], [], 3.0, "Second array is empty, even length"),
        (
            [1, 2],
            [3, 4, 5, 6],
            3.5,
            "All elements of nums1 are smaller than nums2",
        ),
        (
            [1, 1, 3, 3],
            [1, 2, 3, 4],
            2.5,
            "Overlapping elements with duplicates",
        ),
        ([-5, -3, -1], [-4, -2, 0], -2.5, "Negative numbers included"),
        ([1], [2], 1.5, "Both arrays have a single element"),
        ([1, 2, 6], [3, 4, 5], 3.5, "Interleaved arrays, even total length"),
    ]

    all_passed = True
    for i, (nums1, nums2, expected, desc) in enumerate(test_cases, 1):
        result = sol.findMedianSortedArrays(nums1, nums2)
        if result == expected:
            print(f"✅ Test {i} Passed: {desc}")
        else:
            print(f"❌ Test {i} Failed: {desc}")
            print(f"   Input: nums1 = {nums1}, nums2 = {nums2}")
            print(f"   Expected: {expected}, but got: {result}")
            all_passed = False

    print("-" * 30)
    if all_passed:
        print("🎉 All test cases passed!")
    else:
        print("⚠️ Some test cases failed. Review your logic.")


if __name__ == "__main__":
    run_tests()