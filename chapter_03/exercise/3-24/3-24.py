import random


def solve_naive(arr, k) -> bool:
    """
    A slow, O(N*K) reference implementation to generate the 'correct' answer.
    It checks every element against the previous k elements.
    """
    n = len(arr)
    for i in range(n):
        # Check backwards up to k steps
        limit = max(0, i - k)
        for j in range(i - 1, limit - 1, -1):
            if arr[i] == arr[j]:
                return False  # Found duplicate within k distance
    return True


def get_test_cases():
    """
    Generates a list of test cases.
    Each case is a dict: {'arr': [...], 'k': int, 'expected': bool, 'desc': str}
    """
    tests = []

    # --- CATEGORY 1: Basic Logic ---
    tests.append(
        {
            "arr": [1, 2, 3, 4, 1],
            "k": 3,
            "expected": True,
            "desc": "Basic True: Duplicate exists (1), but distance is 4 (which is > k=3)",
        }
    )
    tests.append(
        {
            "arr": [1, 2, 3, 1],
            "k": 3,
            "expected": False,
            "desc": "Basic False: Duplicate (1) at distance 3 (which is <= k=3)",
        }
    )
    tests.append(
        {
            "arr": [1, 2, 3, 4, 5],
            "k": 2,
            "expected": True,
            "desc": "All Unique: No duplicates at all",
        }
    )

    # --- CATEGORY 2: The Boundary (Exactly K vs K+1) ---
    tests.append(
        {
            "arr": [10, 20, 30, 10],
            "k": 2,
            "expected": True,
            "desc": "Boundary: Duplicate distance is 3. 3 > 2. Should be True.",
        }
    )
    tests.append(
        {
            "arr": [10, 20, 30, 10],
            "k": 3,
            "expected": False,
            "desc": "Boundary: Duplicate distance is 3. 3 <= 3. Should be False.",
        }
    )

    # --- CATEGORY 3: Edge Cases ---
    tests.append(
        {"arr": [], "k": 5, "expected": True, "desc": "Empty Array: Vacuously true"}
    )
    tests.append({"arr": [1], "k": 0, "expected": True, "desc": "Single Element"})
    tests.append(
        {
            "arr": [1, 1],
            "k": 1,
            "expected": False,
            "desc": "Immediate neighbors duplicate",
        }
    )
    tests.append(
        {
            "arr": [1, 2, 3, 4, 5, 6],
            "k": 100,
            "expected": True,
            "desc": "K larger than N (Unique array)",
        }
    )
    tests.append(
        {
            "arr": [1, 2, 3, 4, 1, 6],
            "k": 100,
            "expected": False,
            "desc": "K larger than N (Duplicate exists)",
        }
    )

    # --- CATEGORY 4: Stress / Tricky Patterns ---
    tests.append(
        {
            "arr": [5, 5, 5, 5, 5],
            "k": 1,
            "expected": False,
            "desc": "All elements identical",
        }
    )
    tests.append(
        {
            "arr": [1, 2, 3, 1, 2, 3],
            "k": 2,
            "expected": True,
            "desc": "Repeating pattern 1,2,3 with k=2 (Dist is 3)",
        }
    )
    tests.append(
        {
            "arr": [1, 2, 3, 1, 2, 3],
            "k": 3,
            "expected": False,
            "desc": "Repeating pattern 1,2,3 with k=3 (Dist is 3)",
        }
    )

    # --- CATEGORY 5: Randomized Tests ---
    # We generate random arrays and use the Naive solver to determine the expected truth
    for _ in range(5):
        # Generate random array length 20, values 0-10
        rand_arr = [random.randint(0, 15) for _ in range(20)]
        rand_k = random.randint(1, 10)
        expected = solve_naive(rand_arr, rand_k)

        tests.append(
            {
                "arr": rand_arr,
                "k": rand_k,
                "expected": expected,
                "desc": f"Random: N=20, K={rand_k}, Arr={rand_arr}",
            }
        )

    return tests


# ==========================================
# PUT YOUR SOLUTION HERE
# ==========================================
def is_k_unique_solution(arr, k) -> bool:
    """
    TODO: Implement your O(N log K) solution here.
    Current return is a placeholder.
    """
    Set = set()
    for i, c in enumerate(arr):
        if c in Set:
            return False
        Set.add(c)
        if i >= k:
            Set.remove(arr[i - k])

    # Your logic goes here...
    return True


# ==========================================
# TEST RUNNER
# ==========================================
def run_tests():
    cases = get_test_cases()
    passed = 0
    failed = 0

    print(f"{'STATUS':<10} | {'K':<3} | {'EXPECTED':<8} | {'DESC'}")
    print("-" * 80)

    for case in cases:
        # Run user solution
        # Note: We copy the array to ensure your solution doesn't modify the test input in place
        result = is_k_unique_solution(case["arr"].copy(), case["k"])

        if result == case["expected"]:
            passed += 1
            print(
                f"✅ PASS    | {case['k']:<3} | {str(case['expected']):<8} | {case['desc']}"
            )
        else:
            failed += 1
            print(
                f"❌ FAIL    | {case['k']:<3} | {str(case['expected']):<8} | {case['desc']}"
            )
            print(f"   -> Input Array: {case['arr']}")
            print(f"   -> Your Output: {result}")

    print("-" * 80)
    print(f"Total: {len(cases)} | Passed: {passed} | Failed: {failed}")


if __name__ == "__main__":
    run_tests()
