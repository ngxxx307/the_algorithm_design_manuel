class Solution:
    def isValid(self, s: str) -> bool:
        Dict = {
            "(": ")",
            "{": "}",
            "[": "]",
        }
        stack = []

        for c in s:
            if c in Dict:
                stack.append(c)
            else:
                if not stack or c != stack.pop():
                    return False

        return True if not stack else False


# --- Test Suite ---
def run_tests():
    sol = Solution()

    test_cases = [
        # (Input string 's', Expected output, Description)
        ("[]", True, "Simple matching square brackets (Example 1)"),
        ("([{}])", True, "Perfectly nested valid brackets (Example 2)"),
        ("[(])", False, "Interleaved brackets / incorrect order (Example 3)"),
        ("()[]{}", True, "Multiple consecutive valid pairs"),
        ("(", False, "Single open bracket"),
        (")", False, "Single close bracket"),
        ("((", False, "Unclosed open brackets"),
        ("))", False, "Closing brackets without preceding open brackets"),
        ("({[)]})", False, "Complex mismatched nesting"),
        ("{[]}", True, "Valid symmetry"),
        ("(((((((())))))))", True, "Deeply nested valid brackets"),
        ("()()()()()()())(", False, "Valid sequence followed by trailing error"),
    ]

    all_passed = True
    for i, (s, expected, desc) in enumerate(test_cases, 1):
        result = sol.isValid(s)
        if result == expected:
            print(f"✅ Test {i} Passed: {desc}")
        else:
            print(f"❌ Test {i} Failed: {desc}")
            print(f"   Input: s = '{s}'")
            print(f"   Expected: {expected}, but got: {result}")
            all_passed = False

    print("-" * 30)
    if all_passed:
        print("🎉 All test cases passed!")
    else:
        print("⚠️ Some test cases failed. Review your logic.")


if __name__ == "__main__":
    run_tests()
