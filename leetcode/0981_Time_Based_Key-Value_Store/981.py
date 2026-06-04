# Leave this empty for your implementation
from collections import defaultdict


class TimeMap:
    def binary_search(self, List: list[tuple[int, str]], t: int) -> str:
        if len(List) == 0 or t < List[0][0]:
            return ""
        lo , hi = 0, len(List) - 1

        while lo < hi:
            mid = (lo + hi) // 2
            if t <= List[mid][0]:
                hi = mid
            else:
                lo = mid + 1
        if t != List[lo][0]:
            return List[lo - 1][1] if t < List[lo][0] else List[lo][1]
        return List[lo][1]

    def __init__(self):
        self.Dict: dict[str, list[tuple[int, str]]] = defaultdict(list)
        pass

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.Dict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        return self.binary_search(self.Dict[key], timestamp)
        pass


# --- Test Suite ---
def run_tests():
    test_cases = [
        # (Operations, Arguments, Expected Returns, Description)
        (
            ["TimeMap", "set", "get", "get", "set", "get"],
            [[], ["alice", "happy", 1], ["alice", 1], ["alice", 2], ["alice", "sad", 3], ["alice", 3]],
            [None, None, "happy", "happy", None, "sad"],
            "Standard example from LeetCode (Example 1)"
        ),
        (
            ["TimeMap", "set", "set", "get", "get", "get", "get", "get"],
            [[], ["foo", "bar", 10], ["foo", "bar2", 20], ["foo", 5], ["foo", 10], ["foo", 15], ["foo", 20], ["foo", 25]],
            [None, None, None, "", "bar", "bar", "bar2", "bar2"],
            "Get at exact, in-between, and earlier timestamps"
        ),
        (
            ["TimeMap", "get"],
            [[], ["missing_key", 10]],
            [None, ""],
            "Get key that has never been set"
        ),
        (
            ["TimeMap", "set", "set", "get", "get", "get"],
            [[], ["k1", "v1", 1], ["k2", "v2", 2], ["k1", 3], ["k2", 3], ["k1", 0]],
            [None, None, None, "v1", "v2", ""],
            "Handling multiple distinct keys simultaneously"
        ),
        (
            ["TimeMap", "set", "set", "set", "get", "get", "get"],
            [[], ["a", "val1", 100], ["a", "val2", 200], ["a", "val3", 300], ["a", 250], ["a", 350], ["a", 50]],
            [None, None, None, None, "val2", "val3", ""],
            "Multiple timestamp updates to the same key"
        ),
    ]

    all_passed = True
    for i, (ops, args, expected, desc) in enumerate(test_cases, 1):
        result_list = []
        obj = None

        # Execute the sequence of operations
        for op, arg in zip(ops, args):
            if op == "TimeMap":
                obj = TimeMap()
                result_list.append(None)
            elif op == "set":
                result_list.append(obj.set(arg[0], arg[1], arg[2]))
            elif op == "get":
                result_list.append(obj.get(arg[0], arg[1]))

        # Check results
        if result_list == expected:
            print(f"✅ Test {i} Passed: {desc}")
        else:
            print(f"❌ Test {i} Failed: {desc}")
            print(f"   Operations: {ops}")
            print(f"   Arguments:  {args}")
            print(f"   Expected:   {expected}")
            print(f"   Got:        {result_list}")
            all_passed = False

    print("-" * 30)
    if all_passed:
        print("🎉 All test cases passed!")
    else:
        print("⚠️ Some test cases failed. Review your logic.")


if __name__ == "__main__":
    run_tests()