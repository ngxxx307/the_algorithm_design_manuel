from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        ans = [0] * n
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                j = stack.pop()
                ans[j] = i - j
            stack.append(i)
            
        return ans
        
def run_tests():
    solver = Solution()
    
    test_cases = [
        # --- Standard Examples ---
        {
            "name": "Example 1: Mixed temperatures",
            "input": [73, 74, 75, 71, 69, 72, 76, 73],
            "expected": [1, 1, 4, 2, 1, 1, 0, 0]
        },
        {
            "name": "Example 2: Strictly increasing",
            "input": [30, 40, 50, 60],
            "expected": [1, 1, 1, 0]
        },
        {
            "name": "Example 3: Gap in temperatures",
            "input": [30, 60, 90],
            "expected": [1, 1, 0]
        },

        # --- Edge Cases ---
        {
            "name": "Strictly decreasing (No warmer days)",
            "input": [90, 80, 70, 60, 50],
            "expected": [0, 0, 0, 0, 0]
        },
        {
            "name": "All temperatures equal",
            "input": [65, 65, 65, 65],
            "expected": [0, 0, 0, 0]
        },
        {
            "name": "Single day",
            "input": [50],
            "expected": [0]
        },
        {
            "name": "Yo-Yo pattern (Up and Down)",
            "input": [40, 60, 40, 60, 30],
            "expected": [1, 0, 1, 0, 0]
        },
        
        # --- Tricky Scenarios ---
        {
            "name": "Long wait for warmer day",
            "input": [50, 40, 30, 60],
            "expected": [3, 2, 1, 0]
        },
        {
            "name": "Warmer day is distant but not last",
            "input": [70, 60, 50, 40, 75, 30],
            "expected": [4, 3, 2, 1, 0, 0]
        },
        {
            "name": "Repeated warmer value",
            "input": [30, 60, 90, 60],
            "expected": [1, 1, 0, 0] 
            # Note: The last 60 is 0 because there are no future days warmer than 60
        }
    ]

    print(f"{'Test Name':<40} | {'Status':<10} | {'Result'}")
    print("-" * 75)

    for case in test_cases:
        temps = case["input"]
        expected = case["expected"]
        
        # Create a copy of inputs to ensure the solution doesn't modify the original array
        result = solver.dailyTemperatures(temps[:])
        
        status = "PASS" if result == expected else "FAIL"
        print(f"{case['name']:<40} | {status:<10} | {result if status == 'FAIL' else 'Correct'}")
        
        if status == "FAIL":
            print(f"   Expected: {expected}")
            print(f"   Got:      {result}")
            print("-" * 75)

if __name__ == "__main__":
    run_tests()