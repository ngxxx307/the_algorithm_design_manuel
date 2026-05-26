import heapq
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count_dict = defaultdict(int)

        for n in nums:
            count_dict[n] = count_dict[n] + 1
        heap = []

        for key in count_dict:
            heapq.heappush(heap, (count_dict[key], key))

            if len(heap) > k:
                heapq.heappop(heap)
        return [num for count, num in heap]


# --- Test Suite ---
def run_tests():
    sol = Solution()

    test_cases = [
        # (Input 'nums', Input 'k', Expected output, Description)
        ([1, 1, 1, 2, 2, 3], 2, [1, 2], "Standard case (Example 1)"),
        ([1], 1, [1], "Single element (Example 2)"),
        ([4, 4, 4, 4], 1, [4], "All identical elements"),
        ([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5], "All unique elements, k equals length"),
        ([-1, -1], 1, [-1], "Negative numbers"),
        ([1, 2, 2, 3, 3, 3, 4, 4, 4, 4], 2, [3, 4], "Varying frequencies"),
        (
            [7, 7, 7, 7, 2, 2, 2, 9, 9, 9, 9, 9],
            1,
            [9],
            "Highest frequency at the end of the array",
        ),
        (
            [
                3,
                2,
                3,
                1,
                2,
                4,
                5,
                5,
                6,
                7,
                7,
                8,
                2,
                3,
                1,
                1,
                1,
                10,
                11,
                5,
                6,
                2,
                4,
                7,
                8,
                5,
                6,
            ],
            10,
            [1, 2, 5, 3, 6, 7, 4, 8, 9, 10],
            "Large array with many elements (Expected represents top 10, adjusted for valid test logic)",
        ),
    ]

    # Correcting the expected output for the last test case to match actual top 10 frequencies
    test_cases[-1] = (
        [
            3,
            2,
            3,
            1,
            2,
            4,
            5,
            5,
            6,
            7,
            7,
            8,
            2,
            3,
            1,
            1,
            1,
            10,
            11,
            5,
            6,
            2,
            4,
            7,
            8,
            5,
            6,
        ],
        4,
        [1, 2, 5, 3],
        "Large array returning top 4",
    )

    all_passed = True
    for i, (nums, k, expected, desc) in enumerate(test_cases, 1):
        # We pass a copy of nums in case your implementation mutates the input array
        result = sol.topKFrequent(nums.copy(), k)

        # LeetCode accepts the answer in any order, so we sort them before comparing
        if result is not None and sorted(result) == sorted(expected):
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
