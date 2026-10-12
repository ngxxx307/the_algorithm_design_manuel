from typing import Optional


# Definition for a Node.
class Node:

    def __init__(self, val: int = 0, neighbors: Optional[list["Node"]] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def dfs():
    return


# Leave this empty for your implementation
class Solution:

    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        visited: dict[Node, Node] = {}

        def dfs(node: Node | None):
            if not node:
                return None
            nonlocal visited
            node_clone = Node(val=node.val)
            visited[node] = node_clone
            for v in node.neighbors:
                if v not in visited:
                    v_clone = dfs(v)
                else:
                    v_clone = visited[v]
                if v_clone:
                    node_clone.neighbors.append(v_clone)
            return node_clone

        return dfs(node)


# --- Helper Functions for Graph Conversion & Verification ---
def build_graph(adj_list: list[list[int]]) -> Optional[Node]:
    if not adj_list:
        return None

    nodes = {i + 1: Node(i + 1) for i in range(len(adj_list))}
    for i, neighbors in enumerate(adj_list):
        nodes[i + 1].neighbors = [nodes[n] for n in neighbors]

    return nodes[1]


def graph_to_adj_list(node: Optional[Node]) -> list[list[int]]:
    if not node:
        return []

    visited = {}

    def dfs(curr: Node):
        if curr.val in visited:
            return
        visited[curr.val] = curr
        for neighbor in curr.neighbors:
            dfs(neighbor)

    dfs(node)

    result = [[] for _ in range(len(visited))]
    for val in sorted(visited.keys()):
        result[val - 1] = [neighbor.val for neighbor in visited[val].neighbors]

    return result


def is_distinct_deep_copy(original: Optional[Node], clone: Optional[Node]) -> bool:
    if not original and not clone:
        return True
    if not original or not clone:
        return False

    visited_orig = {}
    visited_clone = {}

    def dfs(o: Node, c: Node) -> bool:
        if o is c:  # Direct reference check - fails if original node is reused
            return False
        if o.val != c.val or len(o.neighbors) != len(c.neighbors):
            return False

        visited_orig[o.val] = o
        visited_clone[c.val] = c

        for no, nc in zip(o.neighbors, c.neighbors):
            if no.val != nc.val:
                return False
            if no.val not in visited_orig:
                if not dfs(no, nc):
                    return False
            else:
                if visited_clone.get(no.val) is not nc:
                    return False
        return True

    return dfs(original, clone)


# --- Test Suite ---
def run_tests():
    sol = Solution()

    test_cases = [
        # (adjList, Description)
        (
            [[2, 4], [1, 3], [2, 4], [1, 3]],
            "Standard 4-node connected graph (Example 1)",
        ),
        ([[]], "Single node with no neighbors (Example 2)"),
        ([], "Empty graph (Example 3)"),
        ([[2], [1]], "Two connected nodes"),
        ([[2, 3], [1, 3], [1, 2]], "Complete graph of 3 nodes (Triangle)"),
        ([[2], [1, 3], [2, 4], [3]], "Linear path graph of 4 nodes"),
        (
            [[2, 3, 4], [1], [1], [1]],
            "Star graph (Hub node connected to leaves)",
        ),
        ([[3, 4], [3, 4], [1, 2], [1, 2]], "Complete bipartite graph"),
    ]

    all_passed = True
    for i, (adj_list, desc) in enumerate(test_cases, 1):
        original = build_graph(adj_list)
        clone = sol.cloneGraph(original)

        cloned_adj = graph_to_adj_list(clone)
        is_deep = is_distinct_deep_copy(original, clone)

        if cloned_adj == adj_list and is_deep:
            print(f"✅ Test {i} Passed: {desc}")
        else:
            print(f"❌ Test {i} Failed: {desc}")
            print(f"   Input: adjList = {adj_list}")
            print(f"   Expected adjList: {adj_list}")
            print(f"   Got adjList:      {cloned_adj}")
            if not is_deep and cloned_adj == adj_list:
                print(
                    "   Reason: Graph structure matches, but node references were not deep copied."
                )
            all_passed = False

    print("-" * 40)
    if all_passed:
        print("🎉 All test cases passed!")
    else:
        print("⚠️ Some test cases failed. Review your logic.")


if __name__ == "__main__":
    run_tests()
