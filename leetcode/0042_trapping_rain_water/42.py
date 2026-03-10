from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        stack: list[tuple[int, int]] = []
        highest = -1
        water = 0
        print(height)
        for i, h in enumerate(height):
            if h > highest:  # If highest, create new stack
                lowest = -1
                for left_i, item_h in stack[::-1]:
                    print("highest:", left_i, i)
                    water = water + (i - left_i - 1) * (item_h - lowest)
                    print("water:", water)
                    lowest = max(lowest, item_h)
                stack = [(i, h)]
                highest = h
                continue
            if h < stack[-1][1]:
                stack.append((i, h))
            else:
                lowest = -1
                while stack and h >= stack[-1][1]:
                    left_i, left_h = stack.pop()
                    print("low:", left_i, i)
                    water = water + (i - left_i - 1) * (left_h - lowest)
                    print("water:", water)
                    lowest = max(lowest, left_h)
                    print(lowest)
                if h > lowest:
                    water = water + (i - stack[-1][0] - 1) * (h - lowest)
                stack.append((i, h))

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
