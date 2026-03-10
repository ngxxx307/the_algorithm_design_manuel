from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        leftmost = height[left]
        rightmost = height[right]

        print(height)
        water = 0
        while left != right:
            if leftmost < rightmost:
                left = left + 1
                leftmost = max(leftmost, height[left])
                water = water + (leftmost - height[left])
            else:
                right = right - 1
                rightmost = max(rightmost, height[right])
                water = water + (rightmost - height[right])

        return water


# --- Test Framework ---
def run_tests():
    sol = Solution()

    test_cases = [
        # Standard LeetCode example 1
        {
            "name": "Standard Basin",
            "height": [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],
            "expected": 6,
        },
        # Standard LeetCode example 2
        {"name": "Large Single Basin", "height": [4, 2, 0, 3, 2, 5], "expected": 9},
        # Edge Case: Empty or too small to hold water
        {"name": "Too Short", "height": [1, 2], "expected": 0},
        # # Edge Case: All same height (no gaps for water)
        {"name": "Flat Plateau", "height": [3, 3, 3, 3], "expected": 0},
        # Edge Case: Ascending (water spills off the left)
        {"name": "Staircase Up", "height": [1, 2, 3, 4, 5], "expected": 0},
        # Edge Case: Descending (water spills off the right)
        {"name": "Staircase Down", "height": [5, 4, 3, 2, 1], "expected": 0},
        # Edge Case: Mountain shape (no internal basins)
        {"name": "Mountain Peak", "height": [1, 2, 3, 2, 1], "expected": 0},
        # Tricky: Multiple disparate basins
        {"name": "Twin Valleys", "height": [3, 0, 2, 0, 4], "expected": 7},
    ]

    passed = 0
    for i, tc in enumerate(test_cases):
        result = sol.trap(tc["height"])
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
