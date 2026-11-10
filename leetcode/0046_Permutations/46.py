from typing import List


# Leave this empty for your implementation
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        included = [False] * len(nums)
        solution = []
        res = []

        def backtrack(included: list[bool]):
            if len(solution) == len(nums):
                res.append(solution.copy())
                return
            for i in range(len(nums)):
                if included[i]:
                    continue
                included[i] = True
                solution.append(nums[i])
                backtrack(included)
                included[i] = False
                solution.pop()
            return

        backtrack(included)
        return res


# --- Test Suite ---
def run_tests():
    sol = Solution()

    test_cases = [
        # (nums, Expected output, Description)
        (
            [1, 2, 3],
            [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]],
            "Example 1: Standard 3-element array",
        ),
        ([7], [[7]], "Example 2: Minimum length array (single element)"),
        ([0, 1], [[0, 1], [1, 0]], "Boundary constraint: 2-element array"),
        (
            [-1, 0, 1],
            [[-1, 0, 1], [-1, 1, 0], [0, -1, 1], [0, 1, -1], [1, -1, 0], [1, 0, -1]],
            "Edge case: Negative numbers and zero",
        ),
        ([-5, 5], [[-5, 5], [5, -5]], "Edge case: Two opposite signs"),
        (
            [9, -3, 2],
            [[9, -3, 2], [9, 2, -3], [-3, 9, 2], [-3, 2, 9], [2, 9, -3], [2, -3, 9]],
            "Edge case: Unsorted with negatives",
        ),
        (
            [1, 2, 3, 4],
            [
                [1, 2, 3, 4],
                [1, 2, 4, 3],
                [1, 3, 2, 4],
                [1, 3, 4, 2],
                [1, 4, 2, 3],
                [1, 4, 3, 2],
                [2, 1, 3, 4],
                [2, 1, 4, 3],
                [2, 3, 1, 4],
                [2, 3, 4, 1],
                [2, 4, 1, 3],
                [2, 4, 3, 1],
                [3, 1, 2, 4],
                [3, 1, 4, 2],
                [3, 2, 1, 4],
                [3, 2, 4, 1],
                [3, 4, 1, 2],
                [3, 4, 2, 1],
                [4, 1, 2, 3],
                [4, 1, 3, 2],
                [4, 2, 1, 3],
                [4, 2, 3, 1],
                [4, 3, 1, 2],
                [4, 3, 2, 1],
            ],
            "Moderate size: 4-element array (24 permutations)",
        ),
        ([0], [[0]], "Boundary constraint: Single element zero"),
    ]

    all_passed = True
    for i, (nums_input, expected, desc) in enumerate(test_cases, 1):
        original_input = nums_input[:]
        result = sol.permute(nums_input[:])

        try:
            result_set = set(tuple(p) for p in result) if result is not None else set()
            expected_set = set(tuple(p) for p in expected)
        except TypeError:
            result_set = set()

        if result_set == expected_set:
            print(f"✅ Test {i} Passed: {desc}")
        else:
            print(f"❌ Test {i} Failed: {desc}")
            print(f"   Input: nums = {original_input}")
            print(
                f"   Expected count: {len(expected)}, Got: {len(result) if result is not None else 'None'}"
            )
            print(f"   Expected: {expected}")
            print(f"   Got: {result}")
            all_passed = False

    print("-" * 40)
    if all_passed:
        print("🎉 All test cases passed!")
    else:
        print("⚠️ Some test cases failed. Review your logic.")


if __name__ == "__main__":
    run_tests()
