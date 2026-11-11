from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        # Leave this empty for your implementation
        letters: list[list[str]] = [
            [],
            [],
            ["a", "b", "c"],
            ["d", "e", "f"],
            ["g", "h", "i"],
            ["j", "k", "l"],
            ["m", "n", "o"],
            ["p", "r", "q", "s"],
            ["t", "u", "v"],
            ["w", "x", "y", "z"],
        ]
        res = []
        solution: str = ""

        def backtrack(i: int):
            nonlocal solution
            if i == len(digits):
                res.append(solution)
                return
            for c in letters[int(digits[i])]:
                solution += c
                backtrack(i + 1)
                solution = solution[:-1]
            return

        backtrack(0)
        return res


# --- Test Suite ---
def run_tests():
    sol = Solution()

    test_cases = [
        # (digits, Expected combinations, Description)
        # (
        #     "34",
        #     ["dg", "dh", "di", "eg", "eh", "ei", "fg", "fh", "fi"],
        #     "Example 1: standard 2-digit combination",
        # ),
        # (
        #     "",
        #     [],
        #     "Boundary constraint: minimum length (empty string)",
        # ),
        # (
        #     "2",
        #     ["a", "b", "c"],
        #     "Single digit with 3-letter mapping",
        # ),
        # (
        #     "7",
        #     ["p", "q", "r", "s"],
        #     "Single digit with 4-letter mapping ('7' -> pqrs)",
        # ),
        # (
        #     "23",
        #     ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"],
        #     "Standard 2-digit combination ('23')",
        # ),
        # (
        #     "22",
        #     ["aa", "ab", "ac", "ba", "bb", "bc", "ca", "cb", "cc"],
        #     "Duplicate digits with identical character mappings",
        # ),
        ("6", ["m", "n", "o"], "test"),
        (
            "89",
            [
                "tw",
                "tx",
                "ty",
                "tz",
                "uw",
                "ux",
                "uy",
                "uz",
                "vw",
                "vx",
                "vy",
                "vz",
            ],
            "Mixed 3-letter and 4-letter mappings ('8' -> tuv, '9' -> wxyz)",
        ),
        (
            "79",
            [
                "pw",
                "px",
                "py",
                "pz",
                "qw",
                "qx",
                "qy",
                "qz",
                "rw",
                "rx",
                "ry",
                "rz",
                "sw",
                "sx",
                "sy",
                "sz",
            ],
            "Two 4-letter mapping digits (4 x 4 = 16 combinations)",
        ),
        (
            "234",
            [
                "adg",
                "adh",
                "adi",
                "aeg",
                "aeh",
                "aei",
                "afg",
                "afh",
                "afi",
                "bdg",
                "bdh",
                "bdi",
                "beg",
                "beh",
                "bei",
                "bfg",
                "bfh",
                "bfi",
                "cdg",
                "cdh",
                "cdi",
                "ceg",
                "ceh",
                "cei",
                "cfg",
                "cfh",
                "cfi",
            ],
            "Three-digit combination (3 x 3 x 3 = 27 combinations)",
        ),
        (
            "2222",
            [
                "aaaa",
                "aaab",
                "aaac",
                "aaba",
                "aabb",
                "aabc",
                "aaca",
                "aacb",
                "aacc",
                "abaa",
                "abab",
                "abac",
                "abba",
                "abbb",
                "abbc",
                "abca",
                "abcb",
                "abcc",
                "acaa",
                "acab",
                "acac",
                "acba",
                "acbb",
                "acbc",
                "acca",
                "accb",
                "accc",
                "baaa",
                "baab",
                "baac",
                "baba",
                "babb",
                "babc",
                "baca",
                "bacb",
                "bacc",
                "bbaa",
                "bbab",
                "bbac",
                "bbba",
                "bbbb",
                "bbbc",
                "bbca",
                "bbcb",
                "bbcc",
                "bcaa",
                "bcab",
                "bcac",
                "bcba",
                "bcbb",
                "bcbc",
                "bcca",
                "bccb",
                "bccc",
                "caaa",
                "caab",
                "caac",
                "caba",
                "cabb",
                "cabc",
                "caca",
                "cacb",
                "cacc",
                "cbaa",
                "cbab",
                "cbac",
                "cbba",
                "cbbb",
                "cbbc",
                "cbca",
                "cbcb",
                "cbcc",
                "ccaa",
                "ccab",
                "ccac",
                "ccba",
                "ccbb",
                "ccbc",
                "ccca",
                "cccb",
                "cccc",
            ],
            "Boundary constraint: maximum length 4 (3^4 = 81 combinations)",
        ),
    ]

    all_passed = True
    for i, (digits, expected, desc) in enumerate(test_cases, 1):
        # Defensive copy of input
        input_digits = str(digits)
        result = sol.letterCombinations(input_digits)

        # Output may be returned in any order; sort before comparison
        result_sorted = sorted(result) if isinstance(result, list) else result
        expected_sorted = sorted(expected)

        if result_sorted == expected_sorted:
            print(f"✅ Test {i} Passed: {desc}")
        else:
            print(f"❌ Test {i} Failed: {desc}")
            print(f'   Input: digits = "{input_digits}"')
            print(f"   Expected: {expected_sorted}")
            print(f"   Actual:   {result}")
            all_passed = False

    print("-" * 40)
    if all_passed:
        print("🎉 All test cases passed!")
    else:
        print("⚠️ Some test cases failed. Review your logic.")


if __name__ == "__main__":
    run_tests()
