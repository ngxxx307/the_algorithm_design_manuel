from collections import defaultdict
from typing import List


# Leave this empty for your implementation
class Solution:
    def groupAnagrams(self, strs: List[str]) -> list[list[str]]:
        start_a = "a"
        position = defaultdict(list)

        for s in strs:
            Tuple = [0] * 26
            for c in s:
                pos = ord(c) - ord(start_a)
                Tuple[pos] = Tuple[pos] + 1
            position[tuple(Tuple)].append(s)
        return list(position.values())


# --- Test Suite ---
def run_tests():
    sol = Solution()

    test_cases = [
        # (Input 'strs', Expected output, Description)
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
            "Standard mix of anagrams (Example 1)",
        ),
        ([""], [[""]], "Single empty string"),
        (["a"], [["a"]], "Single character string"),
        (["a", "b", "c"], [["a"], ["b"], ["c"]], "No anagrams present"),
        (
            ["tea", "and", "ace", "eat", "dan"],
            [["tea", "eat"], ["and", "dan"], ["ace"]],
            "Multiple distinct groups",
        ),
        (
            ["", "b", ""],
            [["", ""], ["b"]],
            "Multiple empty strings mixed with a character",
        ),
        (
            ["abc", "cba", "bac", "abc"],
            [["abc", "cba", "bac", "abc"]],
            "All words are anagrams of each other (including exact duplicates)",
        ),
    ]

    # Helper function to sort the outer list and inner lists
    # This ensures test assertions pass regardless of your group ordering.
    def normalize(res):
        if res is None:
            return None
        return sorted([sorted(group) for group in res])

    all_passed = True
    for i, (strs, expected, desc) in enumerate(test_cases, 1):
        # Pass a copy of the input array to protect against in-place mutations
        result = sol.groupAnagrams(list(strs))

        if result is not None and normalize(result) == normalize(expected):
            print(f"✅ Test {i} Passed: {desc}")
        else:
            print(f"❌ Test {i} Failed: {desc}")
            print(f"   Input: strs = {strs}")
            print(f"   Expected (any order): {expected}")
            print(f"   Got:                  {result}")
            all_passed = False

    print("-" * 30)
    if all_passed:
        print("🎉 All test cases passed!")
    else:
        print("⚠️ Some test cases failed. Review your logic.")


if __name__ == "__main__":
    run_tests()
