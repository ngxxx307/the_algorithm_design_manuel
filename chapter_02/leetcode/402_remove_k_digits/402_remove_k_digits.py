import random
import string
from typing import List, Tuple, Callable, Optional

# -------------------------------
# Test case generators
# -------------------------------


def gen_case(num: str, k: int) -> Tuple[str, int]:
    return num, k


def gen_edge_cases() -> List[Tuple[str, int]]:
    cases = []
    # Smallest n
    cases.append(gen_case("0", 0))
    cases.append(gen_case("0", 1))  # if k>len(num) your runner can clamp or expect ""
    # Single digit variations
    for d in "0123456789":
        cases.append(gen_case(d, 0))
        cases.append(gen_case(d, 1 if d != "0" else 0))
    # All zeros
    cases.append(gen_case("0000", 0))
    cases.append(gen_case("0000", 1))
    cases.append(gen_case("0000", 3))
    # All same digit (non-zero)
    cases.append(gen_case("77777", 0))
    cases.append(gen_case("77777", 2))
    cases.append(gen_case("77777", 5))
    # Increasing sequence
    cases.append(gen_case("123456789", 0))
    cases.append(gen_case("123456789", 1))
    cases.append(gen_case("123456789", 5))
    # Decreasing sequence
    cases.append(gen_case("987654321", 0))
    cases.append(gen_case("987654321", 1))
    cases.append(gen_case("987654321", 5))
    # With leading zeros already present
    cases.append(gen_case("00123", 0))
    cases.append(gen_case("00123", 1))
    cases.append(gen_case("00123", 3))
    # k = 0 and k = len(num)
    cases.append(gen_case("10", 0))
    cases.append(gen_case("10", 2))
    # k bigger than len(num) (some callers clamp to len(num))
    cases.append(gen_case("9", 10))
    return cases


def gen_random_num(length: int, allow_leading_zero: bool = True) -> str:
    if length <= 0:
        return "0"
    digits = "0123456789"
    if allow_leading_zero:
        return "".join(random.choice(digits) for _ in range(length))
    first = random.choice("123456789")
    rest = "".join(random.choice(digits) for _ in range(length - 1))
    return first + rest


def gen_random_cases(
    count: int, min_len: int = 1, max_len: int = 20, allow_leading_zero: bool = True
) -> List[Tuple[str, int]]:
    cases = []
    for _ in range(count):
        n = random.randint(min_len, max_len)
        num = gen_random_num(n, allow_leading_zero=allow_leading_zero)
        k = random.randint(0, n + 3)  # sometimes larger than len(num)
        cases.append(gen_case(num, k))
    return cases


def gen_structured_cases() -> List[Tuple[str, int]]:
    cases = []
    # Alternating highs and lows
    cases.append(gen_case("9090909090", 1))
    cases.append(gen_case("9090909090", 5))
    cases.append(gen_case("9090909090", 9))
    # Blocks
    cases.append(gen_case("1111222233334444", 4))
    cases.append(gen_case("555500001111", 6))
    cases.append(gen_case("100200300400500", 7))
    # Long with many zeros inside
    cases.append(gen_case("1200000345000067000089", 10))
    # Borderline near powers of 10
    cases.append(gen_case("1000000", 1))
    cases.append(gen_case("1000000", 6))
    cases.append(gen_case("1000001", 1))
    # Mixed leading zeros plus large k
    cases.append(gen_case("00010203", 3))
    cases.append(gen_case("00010203", 7))
    cases.append(gen_case("9", 1))
    cases.append(gen_case("33526221184202197273", 19))
    return cases


def generate_all_tests(
    random_count: int = 50,
    min_len: int = 1,
    max_len: int = 30,
    allow_leading_zero: bool = True,
) -> List[Tuple[str, int]]:
    tests = []
    tests += gen_random_cases(random_count, min_len, max_len, allow_leading_zero)
    tests += gen_edge_cases()
    tests += gen_structured_cases()

    return tests


# -------------------------------
# Simple test harness
# -------------------------------


def run_tests(
    solution_fn: Callable[[str, int], str],
    tests: List[Tuple[str, int]],
    clamp_k: bool = True,
    verbose: bool = True,
    max_show: Optional[int] = 100,
) -> None:
    """
    Runs the provided Solution.removeKdigits on generated tests.
    This harness does not assert correctness; it just executes and prints.
    - clamp_k: if True, k is clamped to [0, len(num)], which many solutions assume.
    """
    passed = 0
    shown = 0
    for i, (num, k) in enumerate(tests, 1):
        k_eff = max(0, min(k, len(num))) if clamp_k else k
        try:
            out = solution_fn(num, k_eff)
            passed += 1
            if verbose and (max_show is None or shown < max_show):
                print(f"[{i}] num={num!r}, k={k} -> k_eff={k_eff}, out={out!r}")
                shown += 1
        except Exception as e:
            print(f"[{i}] ERROR for num={num!r}, k={k} (k_eff={k_eff}): {e}")

    print(f"\nExecuted {len(tests)} tests, {passed} completed without exceptions.")


# -------------------------------
# Example usage
# -------------------------------


# Dummy placeholder to demonstrate wiring. Replace with your actual Solution.
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        n = len(num)
        for i in range(n):
            while k > 0 and stack and stack[-1] > num[i]:
                print(f"stack: {stack}, num: {num[i]}")
                stack.pop()
                k = k - 1
            stack.append(num[i])
        print((f"stack: {stack}, k: {k}"))
        if k:
            stack = stack[:-k]
        res = "".join(stack).lstrip("0")
        if not stack or not res:
            return "0"
        return res


if __name__ == "__main__":
    random.seed(42)
    tests = generate_all_tests(
        random_count=50,  # increase for more random coverage
        min_len=1,
        max_len=30,
        allow_leading_zero=True,
    )

    sol = Solution()

    # If you already implemented removeKdigits, uncomment:
    # run_tests(sol.removeKdigits, tests, clamp_k=True, verbose=True, max_show=50)

    # Otherwise, just preview the generated test cases:
    for i, (num, k) in enumerate(tests, 1):
        print(f"[preview {i}] num={num!r}, k={k}, Solution:{sol.removeKdigits(num, k)}")
