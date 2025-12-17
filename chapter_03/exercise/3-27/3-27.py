import functools


# ==========================================
# 1. The Simulated Black Box
# ==========================================
def subset_sum_oracle(sequence, k) -> bool:
    """
    This is the 'Black Box' described in the problem.
    It returns True if a subset exists that sums to k, False otherwise.

    Note: In a real scenario, this is O(1) as per the problem statement.
    Here, we simulate it using standard recursion/memoization.
    """
    # Convert list to tuple for caching
    seq_tuple = tuple(sequence)

    @functools.lru_cache(None)
    def _solve(idx, current_target):
        if current_target == 0:
            return True
        if idx < 0 or current_target < 0:
            return False

        # Include current number or exclude it
        val = seq_tuple[idx]
        return _solve(idx - 1, current_target - val) or _solve(idx - 1, current_target)

    return _solve(len(sequence) - 1, k)


# ==========================================
# 2. Your Solution Placeholder
# ==========================================
def find_subset(S: list[int], k: int, oracle: callable):
    """
    Args:
        S (list): The input list of integers.
        k (int): The target sum.
        oracle (func): A function `oracle(sequence, target)` returning boolean.

    Returns:
        list: A subset of S that sums to k. Return [] or None if impossible.
    """
    # TODO: Implement your O(n) logic here using the oracle.
    # Remember: You can call oracle(some_sequence, some_target)
    if not oracle(S, k):
        return None
    arr = []

    for i in range(0, len(S)):
        temp = S[i]
        S[i] = 0
        if not oracle(S, k):
            arr.append(temp)
            S[i] = temp
    return arr  # Placeholder


# ==========================================
# 3. Test Case Generator & Runner
# ==========================================
def run_tests():
    test_cases = [
        # (Input Set S, Target k, Description)
        ([1, 2, 3, 4, 5], 10, "Standard case"),
        ([2, 4, 6, 8], 5, "Impossible case (Evens summing to Odd)"),
        ([10, 20, 30], 0, "Target is 0 (Empty subset)"),
        ([5], 5, "Single element match"),
        ([5], 6, "Single element mismatch"),
        ([1, 1, 1, 1], 3, "Duplicate numbers"),
        ([-5, 10, 5, 2], 7, "Includes negative numbers"),
        ([100, 200, 300], 600, "All elements needed"),
        ([], 0, "Empty input, 0 target"),
        ([], 5, "Empty input, non-zero target"),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 55, "Large sum (all items)"),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1, "First item only"),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, "Last item only"),
    ]

    passed = 0
    failed = 0

    print(f"{'STATUS':<10} | {'TARGET':<6} | {'INPUT (Truncated)':<20} | {'RESULT'}")
    print("-" * 60)

    for S, k, desc in test_cases:
        # 1. Check if a solution is actually possible using the oracle
        is_possible = subset_sum_oracle(S, k)

        # 2. Run the user's solution
        # We pass a copy of S to ensure the solution doesn't mutate the test case for verification
        try:
            result = find_subset(S[:], k, subset_sum_oracle)
        except Exception as e:
            print(f"ERROR      | {k:<6} | {str(S):<20} | Exception: {e}")
            failed += 1
            continue

        # 3. Verify the result
        if not is_possible:
            if result == [] or result is None:
                print(
                    f"PASS       | {k:<6} | {str(S)[:20]:<20} | Correctly returned no solution"
                )
                passed += 1
            else:
                print(
                    f"FAIL       | {k:<6} | {str(S)[:20]:<20} | Expected None/[], got {result}"
                )
                failed += 1
        else:
            if result is None:
                print(
                    f"FAIL       | {k:<6} | {str(S)[:20]:<20} | Solution exists, but got None"
                )
                failed += 1
                continue

            # Check sum
            actual_sum = sum(result)

            # Check if result is actually a subset (accounting for duplicates)
            is_subset = True
            temp_S = list(S)
            for item in result:
                if item in temp_S:
                    temp_S.remove(item)
                else:
                    is_subset = False
                    break

            if actual_sum == k and is_subset:
                print(
                    f"PASS       | {k:<6} | {str(S)[:20]:<20} | Sum: {actual_sum}, Subset: {result}"
                )
                passed += 1
            else:
                print(
                    f"FAIL       | {k:<6} | {str(S)[:20]:<20} | Target: {k}, Got Sum: {actual_sum}, Valid Subset: {is_subset}"
                )
                failed += 1

    print("-" * 60)
    print(f"Tests Completed: {passed} Passed, {failed} Failed")


if __name__ == "__main__":
    run_tests()
