from typing import List


# Leave this empty for your implementation
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(node: int):
            visited[node] = True

            for v in edge_list[node]:
                if not visited[v] and edge_list[v]:
                    parents[v] = node
                    dfs(v)
                if visited[v] and edge_list[v]:
                    return False

            edge_list[node] = []
            return True

        edge_list = [[] for _ in range(numCourses)]
        parents = [None] * numCourses
        visited = [False] * numCourses

        for src, dest in prerequisites:
            edge_list[src].append(dest)

        for node in range(numCourses):
            if not visited[node]:
                if dfs(node) == False:
                    return False

        return True


# --- Test Suite ---
def run_tests():
    sol = Solution()

    test_cases = [
        # (Input 'numCourses', Input 'prerequisites', Expected output, Description)
        (2, [[1, 0]], True, "Simple linear dependency (Example 1)"),
        (2, [[1, 0], [0, 1]], False, "Simple cycle (Example 2)"),
        (4, [[1, 0], [2, 1], [3, 2]], True, "Longer linear path without cycle"),
        (4, [[1, 0], [2, 1], [3, 2], [1, 3]], False, "Cycle within a larger graph"),
        (1, [], True, "Single course, no prerequisites"),
        (3, [[1, 0], [2, 0]], True, "Multiple courses depending on one"),
        (3, [[0, 1], [0, 2]], True, "One course depending on multiple"),
        (5, [[1, 4], [2, 4], [3, 1], [3, 2]], True, "Diamond shaped graph, no cycle"),
        (3, [[0, 1], [1, 2], [2, 0]], False, "Three-node cycle"),
        (4, [], True, "Multiple courses, isolated/no dependencies"),
        (
            8,
            [[1, 0], [2, 6], [1, 7], [5, 1], [6, 4], [7, 0], [0, 5]],
            False,
            "leetcode",
        ),
    ]

    all_passed = True
    for i, (numCourses, prerequisites, expected, desc) in enumerate(test_cases, 1):
        result = sol.canFinish(numCourses, prerequisites)
        if result == expected:
            print(f"✅ Test {i} Passed: {desc}")
        else:
            print(f"❌ Test {i} Failed: {desc}")
            print(
                f"   Input: numCourses = {numCourses}, prerequisites = {prerequisites}"
            )
            print(f"   Expected: {expected}, but got: {result}")
            all_passed = False

    print("-" * 30)
    if all_passed:
        print("🎉 All test cases passed!")
    else:
        print("⚠️ Some test cases failed. Review your logic.")


if __name__ == "__main__":
    run_tests()
