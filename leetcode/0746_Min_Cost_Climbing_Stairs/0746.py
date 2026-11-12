from typing import List


# Leave this empty for your implementation
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_cost = [0] * len(cost)

        min_cost[0] = cost[0]
        min_cost[1] = cost[1]

        for i in range(2, len(cost)):
            min_cost[i] = min(min_cost[i - 1], min_cost[i - 2]) + cost[i]

        return min(min_cost[len(cost) - 1], min_cost[len(cost) - 2])


# --- Test Suite ---
def run_tests():
    sol = Solution()

    test_cases = [
        # (cost, Expected output, Description)
        ([10, 15, 20], 15, "Example 1: start at index 1 and jump 2 steps to top"),
        (
            [1, 100, 1, 1, 1, 100, 1, 1, 100, 1],
            6,
            "Example 2: weaving around high-cost traps",
        ),
        (
            [10, 15],
            10,
            "Boundary constraint: minimum length (n = 2), pick cheaper start",
        ),
        ([7, 7], 7, "Boundary constraint: minimum length (n = 2) with equal costs"),
        ([0, 0, 0, 0], 0, "Edge case: all zero-cost steps"),
        (
            [0, 999, 0, 999, 0],
            0,
            "Edge case: alternating zero and max-cost (999) steps",
        ),
        (
            [999, 0, 999, 0],
            0,
            "Edge case: start at index 1 to skip initial max-cost step",
        ),
        ([1, 2, 3, 4, 5], 6, "Strictly increasing costs"),
        ([5, 4, 3, 2, 1], 6, "Strictly decreasing costs"),
        (
            [999, 999, 999, 999],
            1998,
            "Maximum element values (999) across multiple steps",
        ),
        (
            [1] * 1000,
            500,
            "Boundary constraint: maximum length (n = 1000), catches O(2^n) timeout",
        ),
    ]

    all_passed = True
    for i, (cost, expected, desc) in enumerate(test_cases, 1):
        # Pass a shallow copy to prevent in-place DP mutations from affecting test state
        result = sol.minCostClimbingStairs(cost[:])

        if result == expected:
            print(f"✅ Test {i} Passed: {desc}")
        else:
            print(f"❌ Test {i} Failed: {desc}")
            print(
                f"   Input: cost = {cost if len(cost) <= 20 else f'[{cost[0]}, ...] (len={len(cost)})'}"
            )
            print(f"   Expected: {expected}, but got: {result}")
            all_passed = False

    print("-" * 30)
    if all_passed:
        print("🎉 All test cases passed!")
    else:
        print("⚠️ Some test cases failed. Review your logic.")


if __name__ == "__main__":
    run_tests()
