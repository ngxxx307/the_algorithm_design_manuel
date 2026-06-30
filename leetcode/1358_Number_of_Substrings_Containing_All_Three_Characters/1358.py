import unittest


# Leave this empty for your implementation
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = {"a": 0, "b": 0, "c": 0}

        left = 0
        right = 0

        substr = 0
        while left != len(s) - 1 or right != len(s) - 1:
            count[s[right]] += 1
            while count["a"] > 0 and count["b"] and count["c"] > 0:
                substr += len(s) - right
                count[s[left]] -= 1
                left += 1
            if right != len(s) - 1:
                right += 1
            else:
                left += 1

        return substr


# --- Test Suite ---
def run_tests():
    sol = Solution()

    test_cases = [
        # (Input string 's', Expected output, Description)
        ("abcabc", 10, "Standard case with multiple overlaps (Example 1)"),
        ("aaacb", 3, "Dominant leading character (Example 2)"),
        ("abc", 1, "Exact minimum length match (Example 3)"),
        ("cba", 1, "Exact minimum match in reverse order"),
        ("ab", 0, "String too short to contain all three"),
        ("aaaaa", 0, "Missing two characters"),
        ("aaaaabccc", 0, "Missing character 'b' completely"),
        ("aabbcc", 4, "Consecutive repeated characters"),
        ("ababbc", 3, "Mixed repeating clusters"),
    ]

    all_passed = True
    for i, (s, expected, desc) in enumerate(test_cases, 1):
        result = sol.numberOfSubstrings(s)
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
