from typing import List


# Leave this empty for your implementation
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        solution = []

        def backtrack(level: int, subsum: int):
            if subsum == target:
                res.append(solution.copy())
            while (target - subsum) < candidates[level] and level >= 0:
                level -= 1
            if level < 0:
                return
            backtrack(level - 1, subsum)
            solution.append(candidates[level])
            backtrack(level, subsum + candidates[level])
            solution.pop()

        backtrack(len(candidates) - 1, 0)
        return res


# --- Helper for Order-Independent Comparison ---
def canonicalize(combinations: List[List[int]]) -> List[List[int]]:
    """Sorts inner combinations and the outer list for order-independent comparison."""
    if combinations is None:
        return []
    return sorted([sorted(combo) for combo in combinations])


# --- Test Suite ---
def run_tests():
    sol = Solution()

    test_cases = [
        (
            [2, 3, 6, 7],
            7,
            [[2, 2, 3], [7]],
            "Example 1: Multiple combinations with repeated elements",
        ),
        (
            [2, 3, 5],
            8,
            [[2, 2, 2, 2], [2, 3, 3], [3, 5]],
            "Example 2: Multiple valid combinations",
        ),
        (
            [2],
            1,
            [],
            "Example 3: Target smaller than minimum candidate (no solution)",
        ),
        (
            [5],
            5,
            [[5]],
            "Boundary: Single candidate matching target directly",
        ),
        (
            [2],
            40,
            [[2] * 20],
            "Boundary: Max target (40) composed entirely of smallest candidate (2)",
        ),
        (
            [40],
            40,
            [[40]],
            "Boundary: Max candidate equals max target",
        ),
        (
            [3, 5],
            7,
            [],
            "Unreachable target with coprime candidates (no exact sum)",
        ),
        (
            [2, 4, 6],
            7,
            [],
            "Parity mismatch: All even candidates with odd target",
        ),
        (
            [2, 3, 5, 7],
            10,
            [
                [2, 2, 2, 2, 2],
                [2, 2, 3, 3],
                [2, 3, 5],
                [3, 7],
                [5, 5],
            ],
            "Multi-branching: Target with multiple distinct prime combinations",
        ),
        (
            [8, 7, 4, 3],
            11,
            [
                [3, 4, 4],
                [3, 8],
                [4, 7],
            ],
            "Unsorted input candidates",
        ),
    ]

    all_passed = True
    for i, (candidates, target, expected, desc) in enumerate(test_cases, 1):
        # Pass shallow copy to prevent in-place mutation side-effects
        raw_result = sol.combinationSum(candidates[:], target)

        result_canonical = canonicalize(raw_result)
        expected_canonical = canonicalize(expected)

        if result_canonical == expected_canonical:
            print(f"Test {i} Passed: {desc}")
        else:
            print(f"Test {i} Failed: {desc}")
            print(f"   Input: candidates = {candidates}, target = {target}")
            print(f"   Expected: {expected_canonical}")
            print(f"   Got:      {result_canonical}")
            all_passed = False

    print("-" * 35)
    if all_passed:
        print("All test cases passed!")
    else:
        print("Some test cases failed. Review your logic.")


if __name__ == "__main__":
    run_tests()
