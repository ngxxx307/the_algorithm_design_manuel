from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = -1

        while left != right:
            w = right - left
            if height[left] > height[right]:
                h = height[right]
                right = right - 1
            else:
                h = height[left]
                left = left + 1
            max_area = max(max_area, w * h)
        # Your implementation goes here
        return max_area


# --- Test Framework ---
def run_tests():
    sol = Solution()

    test_cases = [
        # Standard example
        {
            "name": "Standard Case",
            "height": [1, 8, 6, 2, 5, 4, 8, 3, 7],
            "expected": 49,
        },
        # Minimum constraints (only 2 lines)
        {"name": "Minimum Length", "height": [1, 1], "expected": 1},
        # Taller lines on the outside
        {"name": "Tall Outside", "height": [4, 3, 2, 1, 4], "expected": 16},
        # All lines the same height
        {"name": "Uniform Heights", "height": [5, 5, 5, 5], "expected": 15},
        # Zeroes included
        {"name": "Zeroes Included", "height": [0, 2], "expected": 0},
        # Tallest lines right next to each other in the middle
        {"name": "Tall Middle", "height": [2, 3, 4, 5, 18, 17, 6], "expected": 17},
        # Ascending order
        {"name": "Ascending Order", "height": [1, 2, 3, 4, 5], "expected": 6},
    ]

    passed = 0
    for i, tc in enumerate(test_cases):
        result = sol.maxArea(tc["height"])
        if result == tc["expected"]:
            print(f"✅ Test {i+1} ({tc['name']}) Passed!")
            passed += 1
        else:
            print(
                f"❌ Test {i+1} ({tc['name']}) Failed! Expected {tc['expected']}, got {result}"
            )

    print(f"\nScore: {passed}/{len(test_cases)} Passed")


if __name__ == "__main__":
    run_tests()
