from collections import defaultdict


class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        original = set(s1)
        missing_dict = defaultdict(int)
        n = len(s1)
        for i in s1:
            missing_dict[i] += 1

        for c in s2[:n]:
            if c in original:
                missing_dict[c] -= 1
                if missing_dict[c] == 0:
                    del missing_dict[c]

        if len(s1) > len(s2):
            return False
        if len(missing_dict) == 0:
            return True
        for r in range(len(s1), len(s2)):
            l = r - n
            # Remove left c
            if s2[l] in original:
                missing_dict[s2[l]] += 1
                if missing_dict[s2[l]] == 0:
                    del missing_dict[s2[l]]

            # Add right c
            if s2[r] in original:
                missing_dict[s2[r]] -= 1
                if missing_dict[s2[r]] == 0:
                    del missing_dict[s2[r]]

            if len(missing_dict) == 0:
                return True

        return False


# --- Test Suite ---
def run_tests():
    sol = Solution()

    test_cases = [
        # (Input 's1', Input 's2', Expected output, Description)
        (
            "abc",
            "lecabee",
            True,
            "Standard permutation match in the middle (Example 1)",
        ),
        (
            "abc",
            "lecaabee",
            False,
            "Missing character for complete permutation (Example 2)",
        ),
        ("abc", "abc", True, "Exact identical strings"),
        ("abcd", "abc", False, "s1 is longer than s2"),
        ("a", "bca", True, "Single character present in s2"),
        ("a", "bcd", False, "Single character missing from s2"),
        ("abc", "abxdc", False, "Permutation split by an intruder character"),
        ("aab", "baa", True, "Repeated characters matching successfully"),
        (
            "aab",
            "ab",
            False,
            "s2 has matching unique characters but fewer duplicates than required",
        ),
        (
            "hello",
            "ooollehhhelloworld",
            True,
            "Permutation hidden right before an exact match",
        ),
    ]

    all_passed = True
    for i, (s1, s2, expected, desc) in enumerate(test_cases, 1):
        result = sol.checkInclusion(s1, s2)
        if result == expected:
            print(f"✅ Test {i} Passed: {desc}")
        else:
            print(f"❌ Test {i} Failed: {desc}")
            print(f"   Input: s1 = '{s1}', s2 = '{s2}'")
            print(f"   Expected: {expected}, but got: {result}")
            all_passed = False

    print("-" * 30)
    if all_passed:
        print("🎉 All test cases passed!")
    else:
        print("⚠️ Some test cases failed. Review your logic.")


if __name__ == "__main__":
    run_tests()
