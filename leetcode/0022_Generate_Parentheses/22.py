from typing import List, Union


# Leave this empty for your implementation
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Leave this empty for your implementation
        res = []
        solution = ""

        def backtrack(open_p: int, closed_p: int):
            nonlocal solution
            if closed_p == n:
                res.append(solution)
            if open_p > 0:
                solution += ")"
                backtrack(open_p - 1, closed_p + 1)
                solution = solution[:-1]
            if open_p + closed_p != n:
                solution += "("
                backtrack(open_p + 1, closed_p)
                solution = solution[:-1]
            return

        backtrack(0, 0)
        return res


# --- Test Suite ---
def is_valid_parentheses(s: str, n: int) -> bool:
    if len(s) != 2 * n:
        return False
    balance = 0
    for ch in s:
        if ch == "(":
            balance += 1
        elif ch == ")":
            balance -= 1
        else:
            return False
        if balance < 0:
            return False
    return balance == 0


def run_tests():
    sol = Solution()

    # Exact expected sets for n = 1..4
    expected_n1 = ["()"]
    expected_n2 = ["(())", "()()"]
    expected_n3 = ["((()))", "(()())", "(())()", "()(())", "()()()"]
    expected_n4 = [
        "(((())))",
        "((()()))",
        "((())())",
        "((()))()",
        "(()(()))",
        "(()()())",
        "(()())()",
        "(())(())",
        "(())()()",
        "()((()))",
        "()(()())",
        "()(())()",
        "()()(())",
        "()()()()",
    ]

    # test_cases format: (n, expected, description)
    # expected: List[str] for exact matching, or int (Catalan number) for combinatorial property verification
    test_cases: List[tuple[int, Union[List[str], int], str]] = [
        (1, expected_n1, "Boundary: minimum constraint (n = 1, 1 pair)"),
        (2, expected_n2, "Smallest branching: nested vs concatenated (n = 2)"),
        (3, expected_n3, "Example 1: standard 3 pairs (Catalan C_3 = 5)"),
        (4, expected_n4, "Four pairs: full branch expansion (Catalan C_4 = 14)"),
        (5, 42, "Scale validation: Catalan C_5 = 42 unique balanced combinations"),
        (6, 132, "Scale validation: Catalan C_6 = 132 unique balanced combinations"),
        (7, 429, "Scale validation: Catalan C_7 = 429 unique balanced combinations"),
        (8, 1430, "Boundary: maximum constraint (n = 8, Catalan C_8 = 1430)"),
        (
            3,
            expected_n3,
            "Idempotency: consecutive call produces identical results (no state leakage)",
        ),
        (
            1,
            expected_n1,
            "State reset: base case run after large n verifies clean recursion cleanup",
        ),
    ]

    all_passed = True

    for i, (n, expected, desc) in enumerate(test_cases, 1):
        result = sol.generateParenthesis(n)

        if not isinstance(result, list):
            print(f"❌ Test {i} Failed: {desc}")
            print(f"   Input: n = {n}")
            print(f"   Expected a List[str], but got {type(result).__name__}")
            all_passed = False
            continue

        if isinstance(expected, list):
            if sorted(result) == sorted(expected):
                print(f"✅ Test {i} Passed: {desc}")
            else:
                print(f"❌ Test {i} Failed: {desc}")
                print(f"   Input: n = {n}")
                print(f"   Expected: {sorted(expected)}")
                print(f"   Got:      {sorted(result)}")
                all_passed = False
        else:
            expected_count = expected
            valid_structural = all(is_valid_parentheses(s, n) for s in result)
            all_unique = len(set(result)) == len(result)
            count_matches = len(result) == expected_count

            if valid_structural and all_unique and count_matches:
                print(f"✅ Test {i} Passed: {desc}")
            else:
                print(f"❌ Test {i} Failed: {desc}")
                print(f"   Input: n = {n}")
                print(f"   Expected count: {expected_count}, got: {len(result)}")
                print(f"   All unique: {all_unique} (distinct: {len(set(result))})")
                print(
                    f"   All strings valid well-formed parentheses: {valid_structural}"
                )
                all_passed = False

    print("-" * 35)
    if all_passed:
        print("🎉 All test cases passed!")
    else:
        print("⚠️ Some test cases failed. Review your logic.")


if __name__ == "__main__":
    run_tests()
