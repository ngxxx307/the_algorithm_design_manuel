from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Dict: dict[str, list[str]] = {}
        
        for s in strs:
            sorted_s  = ''.join(sorted(s))
            if sorted_s not in Dict:
                Dict[sorted_s] = [s]
            else:
                Dict[sorted_s].append(s)
        return [value for _, value in Dict.items()]

# --- Test Framework ---
def run_tests():
    sol = Solution()
    
    test_cases = [
        {
            "name": "Example 1: Standard case",
            "input": ["eat","tea","tan","ate","nat","bat"],
            "expected": [["bat"],["nat","tan"],["ate","eat","tea"]]
        },
        {
            "name": "Example 2: Single empty string",
            "input": [""],
            "expected": [[""]]
        },
        {
            "name": "Example 3: Single character",
            "input": ["a"],
            "expected": [["a"]]
        },
        {
            "name": "Custom 1: No anagrams present",
            "input": ["cat", "dog", "bird"],
            "expected": [["cat"], ["dog"], ["bird"]]
        },
        {
            "name": "Custom 2: All identical strings",
            "input": ["abc", "abc", "abc"],
            "expected": [["abc", "abc", "abc"]]
        },
        {
            "name": "Custom 3: Multiple empty strings mixed",
            "input": ["", "b", ""],
            "expected": [["", ""], ["b"]]
        },
        {
            "name": "Custom 4: Anagrams with repeated letters",
            "input": ["aab", "aba", "baa", "abb"],
            "expected": [["aab", "aba", "baa"], ["abb"]]
        }
    ]

    passed = 0
    for i, tc in enumerate(test_cases):
        # Run the user's solution
        result = sol.groupAnagrams(tc["input"])
        
        # Helper to sort both inner lists and the outer list to ignore ordering
        def normalize(lst):
            if not lst: return []
            return sorted([sorted(sub) for sub in lst])
        
        # Compare normalized results
        if result is not None and normalize(result) == normalize(tc["expected"]):
            print(f"✅ Test {i+1} Passed: {tc['name']}")
            passed += 1
        else:
            print(f"❌ Test {i+1} Failed: {tc['name']}")
            print(f"   Input:    {tc['input']}")
            print(f"   Expected: {tc['expected']}")
            print(f"   Got:      {result}")
            
    print("-" * 30)
    print(f"Results: {passed}/{len(test_cases)} tests passed.")

if __name__ == "__main__":
    run_tests()