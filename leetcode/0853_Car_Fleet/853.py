import unittest


class Solution:

    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        if len(position) == 0:
            return 0
        fleet = 1

        sorted_indices = sorted(range(len(position)), key=lambda i: position[i])
        top = sorted_indices.pop()
        time_remained = (target - position[top]) / speed[top]

        while sorted_indices:
            i = sorted_indices.pop()
            distance = time_remained * speed[i] + position[i]
            if distance < target:
                fleet += 1
                time_remained = (target - position[i]) / speed[i]
        return fleet


# --- Test Suite ---
def run_tests():
    sol = Solution()

    test_cases = [
        # (target, position, speed, expected_output, description)
        (10, [1, 4], [3, 2], 1, "Example 1: Meet exactly at destination"),
        (
            10,
            [4, 1, 0, 7],
            [2, 2, 1, 1],
            3,
            "Example 2: Fragmented fleets and independent cars",
        ),
        (10, [5], [2], 1, "Single car on the road"),
        (10, [3, 5, 7], [1, 1, 1], 3, "All cars traveling at identical speeds"),
        (
            100,
            [0, 50, 90],
            [100, 10, 1],
            1,
            "Cascade effect: Fast trailing cars join the slowest lead car",
        ),
        (
            10,
            [0, 8],
            [2, 1],
            2,
            "Trailing car is faster but cannot catch up before target",
        ),
        (
            20,
            [10, 15, 18],
            [10, 5, 2],
            1,
            "Simultaneous arrival: All cars hit target at the exact same moment",
        ),
    ]

    all_passed = True
    for i, (target, position, speed, expected, desc) in enumerate(test_cases, 1):
        result = sol.carFleet(target, position, speed)
        if result == expected:
            print(f"✅ Test {i} Passed: {desc}")
        else:
            print(f"❌ Test {i} Failed: {desc}")
            print(
                f"   Input: target = {target}, position = {position}, speed = {speed}"
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
