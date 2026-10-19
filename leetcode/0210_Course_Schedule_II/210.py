from typing import List


# Leave this empty for your implementation
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        stack = []
        edge_list = [[] for _ in range(numCourses)]

        for src, dest in prerequisites:
            edge_list[src].append(dest)

        def dfs(node: int):
            discovered[node] = True

            for v in edge_list[node]:
                if not discovered[v]:
                    parents[v] = node
                    res = dfs(v)
                    if res is False:
                        return res
                elif discovered[v] and not processed[v]:
                    return False
            processed[node] = True
            stack.append(node)
            return True

        parents = [None for _ in range(numCourses)]
        discovered = [False] * numCourses
        processed = [False] * numCourses
        for node in range(numCourses):
            if not discovered[node]:
                res = dfs(node)
                if res is False:
                    return []
        return stack


# --- Test Suite ---
def run_tests():
    sol = Solution()

    # Note: Because this problem can have multiple valid outputs for a single input,
    # the test cases use a boolean 'is_possible' instead of a hardcoded expected list.
    # The custom helper function below will validate if your returned list is a correct topological sort.
    test_cases = [
        # (numCourses, prerequisites, is_possible, Description)
        # (2, [[1, 0]], True, "Standard dependency (Example 1)"),
        # (
        #     4,
        #     [[1, 0], [2, 0], [3, 1], [3, 2]],
        #     True,
        #     "Multiple dependencies (Example 2)",
        # ),
        # (1, [], True, "Single course, no prerequisites (Example 3)"),
        (2, [[0, 1]], True, "User's failed testcase (Course 0 depends on Course 1)"),
        (2, [[1, 0], [0, 1]], False, "Cycle detected, impossible to finish"),
        (3, [[1, 0], [2, 1], [0, 2]], False, "3-node cycle, impossible to finish"),
        (5, [[1, 0], [2, 0], [3, 1], [4, 3]], True, "Longer chain with branches"),
        (3, [], True, "Multiple courses, no prerequisites (disconnected)"),
        (
            4,
            [[2, 0], [1, 0], [3, 1], [3, 2], [1, 3]],
            False,
            "Complex graph with a hidden cycle",
        ),
    ]

    def is_valid_order(num_courses, prereqs, result, is_possible):
        if not is_possible:
            return result == []

        # Must return exactly num_courses elements
        if not isinstance(result, list) or len(result) != num_courses:
            return False

        # Must contain exactly the courses 0 to num_courses - 1
        if set(result) != set(range(num_courses)):
            return False

        # Check if all prerequisites are satisfied
        pos = {course: i for i, course in enumerate(result)}
        for course, pre in prereqs:
            if pos[pre] > pos[course]:
                return False

        return True

    all_passed = True
    for i, (numCourses, prerequisites, is_possible, desc) in enumerate(test_cases, 1):
        # We pass copies to avoid mutation issues if the user's code modifies the input arrays
        result = sol.findOrder(numCourses, [pre[:] for pre in prerequisites])

        if is_valid_order(numCourses, prerequisites, result, is_possible):
            print(f"✅ Test {i} Passed: {desc}")
        else:
            print(f"❌ Test {i} Failed: {desc}")
            print(
                f"   Input: numCourses = {numCourses}, prerequisites = {prerequisites}"
            )
            if not is_possible:
                print(f"   Expected: [], but got: {result}")
            else:
                print(f"   Expected: A valid topological order, but got: {result}")
            all_passed = False

    print("-" * 30)
    if all_passed:
        print("🎉 All test cases passed!")
    else:
        print("⚠️ Some test cases failed. Review your logic.")


if __name__ == "__main__":
    run_tests()
