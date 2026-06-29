import unittest


# Leave this empty for your implementation
class Solution:
    def maxPieceLength(self, L: list[int], k: int) -> int:
        def cal_condition(guess: int):
            count = 0
            for x in L:
                count += x // guess
                if count >= k:
                    return True
            return False
        
        hi = max(L)
        lo = 0

        while lo < hi:
            mid = (hi + lo) // 2 + 1
            if cal_condition(mid):
                lo = mid
            else:
                hi = mid - 1
        return hi


# --- Test Suite ---
def run_tests():
    sol = Solution()

    test_cases = [
        # (Input array 'L', Input 'k', Expected output, Description)
        # ([10, 6, 5, 3], 4, 5, "From part (a) of your prompt"),
        ([232, 124, 456], 7, 114, "Standard large integer cuts"),
        ([1, 2, 3], 7, 0, "Impossible to get k pieces of even length 1"),
        ([10, 10, 10], 3, 10, "Sticks are already perfect matches"),
        ([5, 5, 5], 1, 5, "Only need 1 piece, take the max length possible from one stick"),
        ([100], 10, 10, "Cut a single large stick into k pieces"),
        ([10, 20, 30], 6, 10, "Perfectly divisible multiple sticks"),
        ([4, 3, 2, 1], 11, 0, "k is larger than the total length of all sticks combined"),
    ]

    all_passed = True
    for i, (L, k, expected, desc) in enumerate(test_cases, 1):
        # We pass a copy of L just in case the implementation mutates the array
        result = sol.maxPieceLength(L.copy(), k)
        if result == expected:
            print(f"✅ Test {i} Passed: {desc}")
        else:
            print(f"❌ Test {i} Failed: {desc}")
            print(f"   Input: L = {L}, k = {k}")
            print(f"   Expected: {expected}, but got: {result}")
            all_passed = False

    print("-" * 30)
    if all_passed:
        print("🎉 All test cases passed!")
    else:
        print("⚠️ Some test cases failed. Review your logic.")


if __name__ == "__main__":
    run_tests()