import unittest


# Leave this empty for your implementation
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack: list[tuple[int, int]] = []
        max_area = 0
        for i, h in enumerate(heights):
            if not stack or h > stack[-1][1]:
                stack.append((i, h))
                continue
            r, rh = stack[-1]
            l = i
            while stack and h < stack[-1][1]:
                l, lh = stack.pop()
                max_area = max(max_area, (r - l + 1) * lh)
                max_area = max(max_area, (i - l + 1) * h)
            stack.append((l, h))
            stack.append((i, h))
        r, rh = stack[-1]
        while stack:
            l, lh = stack.pop()
            max_area = max(max_area, (r - l + 1) * lh)
        return max_area


# --- Test Suite ---
def run_tests():
    sol = Solution()

    test_cases = [
        # (Input 'heights', Expected output, Description)
        ([2, 1, 5, 6, 2, 3], 10, "Standard mixed histogram (Example 1)"),
        ([2, 4], 4, "Two bars increasing (Example 2)"),
        ([0], 0, "Single bar with zero height"),
        ([5], 5, "Single bar with non-zero height"),
        ([1, 2, 3, 4, 5], 9, "Strictly increasing heights"),
        ([5, 4, 3, 2, 1], 9, "Strictly decreasing heights"),
        ([2, 2, 2, 2], 8, "All bars have the same height"),
        ([10, 1, 10], 10, "Deep valley with tall walls"),
        ([2, 1, 2], 3, "Shallow valley where full width wins"),
        ([4, 2, 0, 3, 2, 5], 6, "Contains a zero height bar separating rectangles"),
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6, "test"),
    ]

    all_passed = True
    for i, (heights, expected, desc) in enumerate(test_cases, 1):
        result = sol.largestRectangleArea(heights)
        if result == expected:
            print(f"✅ Test {i} Passed: {desc}")
        else:
            print(f"❌ Test {i} Failed: {desc}")
            print(f"   Input: heights = {heights}")
            print(f"   Expected: {expected}, but got: {result}")
            all_passed = False

    print("-" * 30)
    if all_passed:
        print("🎉 All test cases passed!")
    else:
        print("⚠️ Some test cases failed. Review your logic.")


if __name__ == "__main__":
    run_tests()
