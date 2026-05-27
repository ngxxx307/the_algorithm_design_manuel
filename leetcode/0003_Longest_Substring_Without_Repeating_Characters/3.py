import unittest


class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        l = 0
        r = 1
        Set = set(s[l])
        Max = 1
        while r < len(s):
            if s[r] not in Set:
                Set.add(s[r])
            else:
                Max = max(Max, len(Set))
                while s[r] in Set:
                    Set.remove(s[l])
                    l += 1
                Set.add(s[r])
            r += 1
        Max = max(Max, len(Set))
        return Max


# --- Test Suite ---
def run_tests():
    sol = Solution()

    test_cases = [
        # (Input string 's', Expected output, Description)
        ("abcabcbb", 3, "Standard alternating characters (Example 1)"),
        ("bbbbb", 1, "All identical characters (Example 2)"),
        ("pwwkew", 3, "Substring in the middle/end (Example 3)"),
        ("", 0, "Empty string edge case"),
        (" ", 1, "Single space character"),
        ("abcdef", 6, "All unique characters"),
        ("dvdf", 3, "Requires basic sliding window left-pointer reset"),
        ("abba", 2, "Tricky map update where duplicate is before current window"),
        ("tmmzuxt", 5, "Longer complex string with mixed duplicates"),
        ("ohvhjdml", 6, ""),
    ]

    all_passed = True
    for i, (s, expected, desc) in enumerate(test_cases, 1):
        result = sol.lengthOfLongestSubstring(s)
        if result == expected:
            print(f"✅ Test {i} Passed: {desc}")
        else:
            print(f"❌ Test {i} Failed: {desc}")
            print(f"   Input: s = '{s}'")
            print(f"   Expected: {expected}, but got: {result}")
            all_passed = False

    print("-" * 40)
    if all_passed:
        print("🎉 All test cases passed successfully!")
    else:
        print("⚠️ Some test cases failed. Check your sliding window logic.")


if __name__ == "__main__":
    run_tests()
