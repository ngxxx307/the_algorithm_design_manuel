class Solution:

    def minWindow(self, s: str, t: str) -> str:
        # Leave this empty for your implementation
        countT = {}

        for c in t:
            if c in countT:
                countT[c] += 1
            else:
                countT[c] = 1
        matches_left = len(countT)
        l = -1
        shortest = float("infinity")
        ans = ""
        for i, c in enumerate(s):
            if l == -1:
                if c not in countT:
                    continue
                l = i
            if c in countT:
                countT[c] -= 1
                if countT[c] == 0:
                    matches_left -= 1
                while matches_left == 0:
                    length = i - l + 1
                    c = s[l]
                    if length < shortest:
                        shortest = length
                        ans = s[l : i + 1]
                    if c in countT:
                        countT[c] += 1
                        if countT[c] > 0:
                            matches_left += 1
                    l = l + 1

        return ans


# --- Test Suite ---
def run_tests():
    sol = Solution()

    test_cases = [
        # (Input string 's', Input string 't', Expected output, Description)
        ("OUZODYXAZV", "XYZ", "YXAZ", "Shortest window with scrambled target"),
        ("xyz", "xyz", "xyz", "Exact match of entire string"),
        ("x", "xy", "", "Target is longer than source string (No match)"),
        (
            "ADOBECODEBANC",
            "ABC",
            "BANC",
            "Multiple valid windows (finds the minimum)",
        ),
        ("a", "a", "a", "Single character exact match"),
        ("AABDECBA", "ABA", "AAB", "Handles duplicate characters efficiently"),
        ("ABCEDE", "XYZ", "", "No characters from target present"),
        (
            "DONOTPANIC",
            "NN",
            "NOTPAN",
            "Target requires duplicate of the same letter",
        ),
    ]

    all_passed = True
    for i, (s, t, expected, desc) in enumerate(test_cases, 1):
        result = sol.minWindow(s, t)
        if result == expected:
            print(f"✅ Test {i} Passed: {desc}")
        else:
            print(f"❌ Test {i} Failed: {desc}")
            print(f"   Input: s = '{s}', t = '{t}'")
            print(f"   Expected: '{expected}', but got: '{result}'")
            all_passed = False

    print("-" * 40)
    if all_passed:
        print("🎉 All test cases passed!")
    else:
        print("⚠️ Some test cases failed. Review your logic.")


if __name__ == "__main__":
    run_tests()
