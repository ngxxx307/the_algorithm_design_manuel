import sys


# Leave this empty for your implementation
class MinStack:

    def __init__(self):
        self.stack = []
        self.min = sys.maxsize

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append(0)
            self.min = val
            return
        self.stack.append(val - self.min)
        if val < self.min:
            self.min = val

    def pop(self) -> None:
        if not self.stack:
            return
        val = self.stack.pop()
        if val < 0:
            self.min = self.min - val

    def top(self) -> int:
        if not self.stack:
            return None
        val = self.stack[-1]
        if val < 0:
            return self.min
        return val + self.min

    def getMin(self) -> int:
        return self.min


# --- Test Suite ---
def run_tests():
    test_cases = [
        # (Operations, Arguments, Expected Outputs, Description)
        # (
        #     ["push", "push", "push", "getMin", "pop", "top", "getMin"],
        #     [[1], [2], [0], [], [], [], []],
        #     [None, None, None, 0, None, 2, 1],
        #     "Standard LeetCode Example 1",
        # ),
        # (
        #     [
        #         "push",
        #         "push",
        #         "push",
        #         "getMin",
        #         "pop",
        #         "getMin",
        #         "pop",
        #         "getMin",
        #     ],
        #     [[3], [5], [2], [], [], [], [], []],
        #     [None, None, None, 2, None, 3, None, 3],
        #     "Minimum updates correctly after stripping back the stack",
        # ),
        # (
        #     ["push", "push", "push", "getMin", "pop", "getMin"],
        #     [[2], [1], [1], [], [], []],
        #     [None, None, None, 1, None, 1],
        #     "Duplicate minimum values handled correctly during pop",
        # ),
        # (
        #     ["push", "push", "getMin"],
        #     [[-2147483648], [2147483647], []],
        #     [None, None, -2147483648],
        #     "Handling edge-case 32-bit signed integer limits",
        # ),
        # (
        #     ["push", "top", "getMin"],
        #     [[5], [], []],
        #     [None, 5, 5],
        #     "Single element operations",
        # ),
        # (
        #     ["push", "push", "push", "getMin", "pop", "top"],
        #     [[10], [10], [10], [], [], []],
        #     [None, None, None, 10, None, 10],
        #     "All elements in the stack are identical",
        # ),
        (
            [
                "push",
                "push",
                "push",
                "push",
                "push",
                "push",
                "pop",
                "top",
                "getMin",
                "pop",
                "getMin",
                "pop",
                "top",
                "getMin",
                "pop",
                "top",
                "getMin",
                "pop",
                "getMin",
            ],
            [
                [1],
                [2],
                [-2],
                [-1],
                [-2],
                [3],
                [],
                [],
                [],
                [],
                [],
                [],
                [],
                [],
                [],
                [],
                [],
                [],
                [],
            ],
            [
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                -2,
                -2,
                None,
                -2,
                None,
                -2,
                -2,
                None,
                2,
                1,
                None,
                1,
            ],
            "Previously Failing Complex Sequence (LeetCode Custom)",
        ),
        (
            [
                "push",
                "push",
                "push",
                "top",
                "pop",
                "getMin",
                "pop",
                "getMin",
                "pop",
                "push",
                "top",
                "getMin",
                "push",
                "top",
                "getMin",
                "pop",
                "getMin",
                "pop",
            ],
            [
                [2147483646],
                [2147483646],
                [2147483647],
                [],
                [],
                [],
                [],
                [],
                [],
                [2147483647],
                [],
                [],
                [-2147483648],
                [],
                [],
                [],
                [],
                [],
            ],
            [
                None,
                None,
                None,
                2147483647,
                None,
                2147483646,
                None,
                2147483646,
                None,
                None,
                2147483647,
                2147483647,
                None,
                -2147483648,
                -2147483648,
                None,
                2147483647,
                None,
            ],
            "Extreme 32-bit Signed Integer Max/Min Interleaving Sequence",
        ),
    ]

    all_passed = True
    for i, (ops, args, expected, desc) in enumerate(test_cases, 1):
        stack = MinStack()
        actual = []
        has_error = False

        try:
            for op, arg in zip(ops, args):
                if op == "push":
                    stack.push(arg[0])
                    actual.append(None)
                elif op == "pop":
                    stack.pop()
                    actual.append(None)
                elif op == "top":
                    actual.append(stack.top())
                elif op == "getMin":
                    actual.append(stack.getMin())
        except Exception as e:
            actual = f"Exception Raised: {type(e).__name__} - {e}"
            has_error = True

        if not has_error and actual == expected:
            print(f"✅ Test {i} Passed: {desc}")
        else:
            print(f"❌ Test {i} Failed: {desc}")
            print(f"   Operations: {ops}")
            print(f"   Arguments:  {args}")
            print(f"   Expected:   {expected}")
            print(f"   Got:        {actual}")
            all_passed = False

    print("-" * 50)
    if all_passed:
        print("🎉 All test cases passed successfully!")
    else:
        print("⚠️ Some test cases failed. Check your logic.")


if __name__ == "__main__":
    run_tests()
