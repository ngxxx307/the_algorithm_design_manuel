import math


# Leave this empty for your implementation
class Solution:
    def probabilityOfHeads(self, prob: list[float], target: int) -> float:
        if not prob:
            return 1
        prob_matrix = [[0] * (target + 1) for _ in range(len(prob))]

        for i, p in enumerate(prob):
            for j in range(target + 1):
                if j > (i + 1):
                    break
                prev_minus_one_p = prob_matrix[i - 1][j - 1] if i > 0 and j > 0 else 0
                prev_p = prob_matrix[i - 1][j] if i > 0 else 0

                if i == 0:
                    prob_matrix[0][0] = 1 - p
                    if target:
                        prob_matrix[0][1] = p
                    continue
                prob_matrix[i][j] = prev_minus_one_p * p + prev_p * (1 - p)
        return prob_matrix[-1][-1]


# --- Test Suite ---
def run_tests():
    sol = Solution()

    test_cases = [
        # (Input 'prob', Input 'target', Expected output, Description)
        ([0.5, 0.5, 0.5], 0, 0.125, "All fair coins, target 0 heads"),
        ([0.5, 0.5, 0.5], 3, 0.125, "All fair coins, target 3 heads"),
        ([0.4, 0.5, 0.6], 2, 0.380, "Biased coins, target 2 heads"),
        ([1.0, 1.0, 1.0], 3, 1.000, "Guaranteed heads, target matches coins"),
        ([1.0, 1.0, 1.0], 2, 0.000, "Guaranteed heads, target is impossible"),
        ([0.0, 0.0, 0.0], 0, 1.000, "Guaranteed tails, target 0 heads"),
        ([0.1, 0.2, 0.3], 0, 0.504, "Biased coins, target 0 heads"),
        ([0.5], 1, 0.500, "Single coin, target 1"),
        ([0.5], 0, 0.500, "Single coin, target 0"),
        ([], 0, 1.000, "Edge case: Zero coins, target 0"),
    ]

    all_passed = True
    for i, (prob, target, expected, desc) in enumerate(test_cases, 1):
        result = sol.probabilityOfHeads(prob, target)

        # Handle None returns if the function isn't implemented yet
        if result is None:
            print(f"❌ Test {i} Failed: {desc}")
            print(f"   Function returned None. Implement the solution.")
            all_passed = False
            continue

        # Use math.isclose for floating-point comparison
        if math.isclose(result, expected, rel_tol=1e-5, abs_tol=1e-8):
            print(f"✅ Test {i} Passed: {desc}")
        else:
            print(f"❌ Test {i} Failed: {desc}")
            print(f"   Input: prob = {prob}, target = {target}")
            print(f"   Expected: {expected:.5f}, but got: {result:.5f}")
            all_passed = False

    print("-" * 30)
    if all_passed:
        print("🎉 All test cases passed!")
    else:
        print("⚠️ Some test cases failed. Review your logic.")


if __name__ == "__main__":
    run_tests()
