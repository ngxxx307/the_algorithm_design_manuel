import unittest


class Solution:

    def evalRPN(self, tokens: list[str]) -> int:
        # --- Place your implementation here ---
        stack = []

        for t in tokens:
            match t:
                case "+":
                    r = stack.pop()
                    l = stack.pop()
                    stack.append(l + r)
                case "-":
                    r = stack.pop()
                    l = stack.pop()
                    stack.append(l - r)
                case "*":
                    r = stack.pop()
                    l = stack.pop()
                    stack.append(l * r)
                case "/":
                    r = stack.pop()
                    l = stack.pop()
                    stack.append(int(l / r))
                case _:
                    stack.append(int(t))
        return stack.pop()


# --- Test Suite ---
def run_tests():
    sol = Solution()

    test_cases = [
        # (Input tokens, Expected output, Description)
        # (
        #     ["2", "1", "+", "3", "*"],
        #     9,
        #     "Standard addition and multiplication (Example 1)",
        # ),
        # (
        #     ["4", "13", "5", "/", "+"],
        #     6,
        #     "Division truncates toward zero - positive result (Example 2)",
        # ),
        (
            [
                "10",
                "6",
                "9",
                "3",
                "+",
                "-11",
                "*",
                "/",
                "*",
                "17",
                "+",
                "5",
                "+",
            ],
            22,
            "Complex nested expression with negatives (Example 3)",
        ),
        (["18"], 18, "Single operand string (no operators)"),
        (
            ["1", "-2", "/"],
            0,
            "Truncation toward zero producing 0 (-0.5 -> 0)",
        ),
        (
            ["-4", "3", "/"],
            -1,
            "Truncation toward zero with negative result (-1.333 -> -1)",
        ),
        (
            ["2", "3", "-"],
            -1,
            "Subtraction order verification (2 - 3 instead of 3 - 2)",
        ),
        (
            ["4", "2", "/"],
            2,
            "Division order verification (4 / 2 instead of 2 / 4)",
        ),
        (
            ["3", "-2", "*", "5", "+"],
            -1,
            "Negative intermediate results from multiplication",
        ),
    ]

    all_passed = True
    for i, (tokens, expected, desc) in enumerate(test_cases, 1):
        try:
            result = sol.evalRPN(tokens)
            if result == expected:
                print(f"✅ Test {i} Passed: {desc}")
            else:
                print(f"❌ Test {i} Failed: {desc}")
                print(f"   Input: tokens = {tokens}")
                print(f"   Expected: {expected}, but got: {result}")
                all_passed = False
        except Exception as e:
            print(f"💥 Test {i} Crashed: {desc}")
            print(f"   Error: {e}")
            all_passed = False

    print("-" * 40)
    if all_passed:
        print("🎉 All test cases passed!")
    else:
        print("⚠️ Some test cases failed. Review your logic.")


if __name__ == "__main__":
    run_tests()
