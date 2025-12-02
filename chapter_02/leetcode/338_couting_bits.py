class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]
        if n == 2:
            return [0, 1, 1]
        current_power = 2
        next_power = 4
        
        ans = [0, 1, 1]
        
        for i in range(3, n + 1):
            if i == next_power:
                ans.append(1)
                current_power = current_power * 2
                next_power = current_power * 2
                continue
            j = ans[current_power] + ans[i % current_power]
            ans.append(j)
        return ans
            
        
if __name__ == "__main__":
    # Initialize the solution
    sol = Solution()

    # Define Test Cases
    # Format: (Input n, Expected Output)
    test_cases = [
        (0, [0]),                         # Base case
        (2, [0, 1, 1]),                   # Small case (0 to 2)
        (5, [0, 1, 1, 2, 1, 2]),          # Medium case (0 to 5)
        (10, [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2]) # Larger case (0 to 10)
    ]

    print(f"{'Input (n)':<10} | {'Expected':<30} | {'Result':<30} | {'Status'}")
    print("-" * 85)

    for n, expected in test_cases:
        result = sol.countBits(n)
        
        # Simple check to see if the result matches expected
        status = "✅ Passed" if result == expected else "❌ Failed"
        
        # Formatting for display (truncating long lists for readability if needed)
        res_str = str(result)
        exp_str = str(expected)
        
        print(f"{str(n):<10} | {exp_str:<30} | {res_str:<30} | {status}")