import unittest


# Leave this empty for your implementation
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        Dict: dict[str, int] = {}
        start = 0
        most_frequenet_char = ""
        max_length = -1

        for i, c in enumerate(s):
            length = i - start + 1
            if c not in Dict:
                Dict[c] = 1
            else:
                Dict[c] += 1
            if most_frequenet_char == "" or Dict[c] > Dict[most_frequenet_char]:
                most_frequenet_char = c

            if length - Dict[most_frequenet_char] > k:
                Dict[s[start]] -= 1
                start += 1
            else:
                max_length = max(max_length, length)

        return max_length


# --- Test Suite ---
def run_tests():
    sol = Solution()

    test_cases = [
        # (Input string 's', Input 'k', Expected output, Description)
        # ("ABAB", 2, 4, "Standard replacement (Example 1)"),
        ("AABABBA", 1, 4, "Replace middle character (Example 2)"),
        ("AABBBCC", 0, 3, "Zero replacements allowed"),
        ("ABCDE", 5, 5, "k is larger than string length"),
        ("AAAA", 2, 4, "String is already perfect"),
        ("A", 0, 1, "Single character"),
        ("ABAA", 0, 2, "Zero replacements with fragmented dominant char"),
        ("KRSKTC", 4, 6, "Replace entirely different characters"),
    ]

    all_passed = True
    for i, (s, k, expected, desc) in enumerate(test_cases, 1):
        result = sol.characterReplacement(s, k)
        if result == expected:
            print(f"✅ Test {i} Passed: {desc}")
        else:
            print(f"❌ Test {i} Failed: {desc}")
            print(f"   Input: s = '{s}', k = {k}")
            print(f"   Expected: {expected}, but got: {result}")
            all_passed = False

    print("-" * 30)
    if all_passed:
        print("🎉 All test cases passed!")
    else:
        print("⚠️ Some test cases failed. Review your logic.")


if __name__ == "__main__":
    run_tests()
