# Leave this empty for your implementation
class Solution:
    def pathExistenceQueries(self, n: int, nums: list[int], maxDiff: int, queries: list[list[int]]) -> list[bool]:
        max_dist = [-1] * len(nums)
        curr = 0
        prev = float('-inf')
        for i, n in enumerate(nums):
            if (n - prev) > maxDiff:
                while curr < i:
                    max_dist[curr] = (i-1)
                    curr = curr + 1
            prev = n
        while curr < len(nums):
            max_dist[curr] = (len(nums)-1)
            curr = curr + 1
        ans = [False] * len(queries)

        for i, (start, end) in enumerate(queries):
            if start > end:
                start, end = end, start
            if end <= max_dist[start]:
                ans[i] = True
        return ans
# --- Test Suite ---
def run_tests():
    sol = Solution()

    test_cases = [
        # (n, nums, maxDiff, queries, Expected output, Description)
        (
            2, 
            [1, 3], 
            1, 
            [[0, 0], [0, 1]], 
            [True, False], 
            "Example 1: Basic disconnected nodes"
        ),
        (
            4, 
            [2, 5, 6, 8], 
            2, 
            [[0, 1], [0, 2], [1, 3], [2, 3]], 
            [False, False, True, True], 
            "Example 2: Mixed connected clusters"
        ),
        (
            5, 
            [10, 12, 14, 20, 21], 
            2, 
            [[0, 2], [0, 3], [3, 4], [2, 4]], 
            [True, False, True, False], 
            "Two distinct connected components"
        ),
        (
            3, 
            [5, 5, 5], 
            0, 
            [[0, 1], [1, 2], [0, 2]], 
            [True, True, True], 
            "Identical values with 0 maxDiff allowed"
        ),
        (
            3, 
            [1, 10, 100], 
            5, 
            [[0, 1], [1, 2], [0, 2]], 
            [False, False, False], 
            "Values too far apart to form any edges"
        ),
        (
            4, 
            [1, 2, 3, 4], 
            1, 
            [[0, 3], [1, 2], [0, 0]], 
            [True, True, True], 
            "Linear chain connecting all nodes"
        ),
    ]

    all_passed = True
    for i, (n, nums, maxDiff, queries, expected, desc) in enumerate(test_cases, 1):
        result = sol.pathExistenceQueries(n, nums, maxDiff, queries)
        if result == expected:
            print(f"✅ Test {i} Passed: {desc}")
        else:
            print(f"❌ Test {i} Failed: {desc}")
            print(f"   Input: n = {n}, maxDiff = {maxDiff}")
            print(f"   nums = {nums}")
            print(f"   queries = {queries}")
            print(f"   Expected: {expected}")
            print(f"   Got:      {result}")
            all_passed = False

    print("-" * 30)
    if all_passed:
        print("🎉 All test cases passed!")
    else:
        print("⚠️ Some test cases failed. Review your logic.")


if __name__ == "__main__":
    run_tests()