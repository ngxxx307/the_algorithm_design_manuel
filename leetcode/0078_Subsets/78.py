from typing import List


# Leave this empty for your implementation
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def Backtrack(p: List[int], level: int):
            nonlocal res
            if level == len(nums):
                res.append(p)
                return

            Backtrack(p, level + 1)
            Backtrack(p + [nums[level]], level + 1)

        Backtrack([], 0)
        return res


# --- Test Suite ---
def normalize_subsets(subsets: List[List[int]]) -> set:
    """Helper to convert subsets into a set of frozensets for order-independent comparison."""
    if subsets is None:
        return set()
    return {frozenset(s) for s in subsets}


def run_tests():
    sol = Solution()

    # Test cases: (nums, expected_subsets, description)
    test_cases = [
        (
            [1, 2, 3],
            [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]],
            "Standard case (Example 1): 3 distinct positive integers",
        ),
        (
            [7],
            [[], [7]],
            "Boundary constraint (Example 2): Single element array",
        ),
        (
            [-10],
            [[], [-10]],
            "Boundary constraint: Single minimum negative integer (-10)",
        ),
        (
            [0],
            [[], [0]],
            "Boundary constraint: Single zero element",
        ),
        (
            [-1, 1],
            [[], [-1], [1], [-1, 1]],
            "Small mixed sign: 2 elements with negative and positive values",
        ),
        (
            [-2, 0, 2],
            [[], [-2], [0], [2], [-2, 0], [-2, 2], [0, 2], [-2, 0, 2]],
            "Mixed values with zero: 3 elements",
        ),
        (
            [4, 1],
            [[], [4], [1], [4, 1]],
            "Unsorted input array: 2 elements",
        ),
        (
            [9, -3, 5, 0],
            [
                [],
                [9],
                [-3],
                [5],
                [0],
                [9, -3],
                [9, 5],
                [9, 0],
                [-3, 5],
                [-3, 0],
                [5, 0],
                [9, -3, 5],
                [9, -3, 0],
                [9, 5, 0],
                [-3, 5, 0],
                [9, -3, 5, 0],
            ],
            "Unsorted 4-element mixed array (16 subsets)",
        ),
        (
            [-5, -4, -3, -2, -1],
            [
                [],
                [-5],
                [-4],
                [-3],
                [-2],
                [-1],
                [-5, -4],
                [-5, -3],
                [-5, -2],
                [-5, -1],
                [-4, -3],
                [-4, -2],
                [-4, -1],
                [-3, -2],
                [-3, -1],
                [-2, -1],
                [-5, -4, -3],
                [-5, -4, -2],
                [-5, -4, -1],
                [-5, -3, -2],
                [-5, -3, -1],
                [-5, -2, -1],
                [-4, -3, -2],
                [-4, -3, -1],
                [-4, -2, -1],
                [-3, -2, -1],
                [-5, -4, -3, -2],
                [-5, -4, -3, -1],
                [-5, -4, -2, -1],
                [-5, -3, -2, -1],
                [-4, -3, -2, -1],
                [-5, -4, -3, -2, -1],
            ],
            "All negative integers: 5 elements (32 subsets)",
        ),
        (
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            None,  # Verified by size (2^10 = 1024) and unique subsets of nums
            "Maximum constraint: Length 10 array (1024 unique subsets)",
        ),
    ]

    all_passed = True
    for i, (nums, expected, desc) in enumerate(test_cases, 1):
        input_copy = nums[:]
        result = sol.subsets(input_copy)

        # Max constraint verification (check length and distinctness)
        if expected is None:
            passed = (
                isinstance(result, list)
                and len(result) == 1024
                and len({frozenset(s) for s in result}) == 1024
                and all(set(s).issubset(set(nums)) for s in result)
            )
        else:
            passed = (
                isinstance(result, list)
                and len(result) == len(expected)
                and normalize_subsets(result) == normalize_subsets(expected)
            )

        if passed:
            print(f"Test {i} Passed: {desc}")
        else:
            print(f"Test {i} Failed: {desc}")
            print(f"   Input nums: {nums}")
            if expected is not None:
                print(
                    f"   Expected count: {len(expected)}, Got count: {len(result) if isinstance(result, list) else result}"
                )
            else:
                print(
                    f"   Expected 1024 unique valid subsets, Got: {len(result) if isinstance(result, list) else result}"
                )
            all_passed = False

    print("-" * 35)
    if all_passed:
        print("All test cases passed!")
    else:
        print("Some test cases failed. Review your logic.")


if __name__ == "__main__":
    run_tests()
