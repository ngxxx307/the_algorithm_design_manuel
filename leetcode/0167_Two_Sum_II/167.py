import unittest


class Solution:

    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        start = 0
        end = len(numbers) - 1

        while start != end:
            Sum = numbers[start] + numbers[end]
            if Sum == target:
                return [start + 1, end + 1]
            if Sum < target:
                start = start + 1
            if Sum > target:
                end = end - 1
        return []


# --- Test Suite ---
def run_tests():
    sol = Solution()

    test_cases = [
        # (Input 'numbers', Input 'target', Expected output, Description)
        ([1, 2, 3, 4], 3, [1, 2], "Standard small array (Example 1)"),
        ([2, 7, 11, 15], 9, [1, 2], "Target at the beginning of the array"),
        ([2, 3, 4, 4], 8, [3, 4], "Target formed by duplicate elements"),
        ([-1, 0], -1, [1, 2], "Array with negative numbers and zero"),
        (
            [-10, -5, 0, 3, 7],
            -3,
            [1, 5],
            "Negative and positive numbers combined (-10 + 7)",
        ),
        (
            [1, 3, 5, 7, 9, 11],
            12,
            [1, 6],
            "Target formed by first and last elements",
        ),
        ([0, 0], 0, [1, 2], "Minimum array size (2 elements) with zeros"),
    ]

    all_passed = True
    for i, (numbers, target, expected, desc) in enumerate(test_cases, 1):
        result = sol.twoSum(numbers, target)
        if result == expected:
            print(f"✅ Test {i} Passed: {desc}")
        else:
            print(f"❌ Test {i} Failed: {desc}")
            print(f"   Input: numbers = {numbers}, target = {target}")
            print(f"   Expected: {expected}, but got: {result}")
            all_passed = False

    print("-" * 30)
    if all_passed:
        print("🎉 All test cases passed!")
    else:
        print("⚠️ Some test cases failed. Review your logic.")


if __name__ == "__main__":
    run_tests()
