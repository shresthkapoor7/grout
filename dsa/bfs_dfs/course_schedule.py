"""
LeetCode 207: Course Schedule

Why this one:
- It directly matches the graph BFS/DFS focus from `amazon_oa_dsa.md`.
- It forces you to build an adjacency list from `prerequisites`.
- It trains cycle detection in a directed graph, which is a core interview pattern.
- Amazon-oriented graph prep lists continue to include it.

Problem summary:
There are `numCourses` total courses labeled from `0` to `numCourses - 1`.
You are given `prerequisites` where `prerequisites[i] = [a, b]` means you
must take course `b` before course `a`.

Return `True` if you can finish all courses, otherwise return `False`.

Examples:
- numCourses = 2, prerequisites = [[1, 0]] -> True
- numCourses = 2, prerequisites = [[1, 0], [0, 1]] -> False

Suggested constraints:
- Runtime target: O(V + E)

References:
- https://leetcode.com/problems/course-schedule/
- https://leetcode.com/discuss/post/7454010/graph-problems-for-amazon-sde-1-intervie-96rq/
- https://leetcode.com/discuss/post/5039797/bfs-and-dfs-graph-problems-easy-to-mediu-8mz5/
- https://leetcode.com/discuss/post/7474246/top-120-most-frequently-asked-amazon-sde-imwy/
"""


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        """
        Implement graph traversal to determine whether all courses can be finished.
        """
        adjList = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            adjList[course].append(prereq)
        
        visiting = set()
        visited = set()

        def dfs(course: int) -> bool:
            if course in visiting:
                return False
            if course in visited:
                return True

            visiting.add(course)

            for prereq in adjList[course]:
                if not dfs(prereq):
                    return False

            visiting.remove(course)
            visited.add(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True


def run_tests() -> None:
    solution = Solution()

    test_cases = [
        {"numCourses": 2, "prerequisites": [[1, 0]], "expected": True},
        {"numCourses": 2, "prerequisites": [[1, 0], [0, 1]], "expected": False},
        {"numCourses": 5, "prerequisites": [[1, 4], [2, 4], [3, 1], [3, 2]], "expected": True},
        {"numCourses": 3, "prerequisites": [[0, 1], [1, 2], [2, 0]], "expected": False},
        {"numCourses": 1, "prerequisites": [], "expected": True},
        {"numCourses": 4, "prerequisites": [[1, 0], [2, 1], [3, 2]], "expected": True},
        {"numCourses": 4, "prerequisites": [[1, 0], [2, 1], [0, 2]], "expected": False},
        {"numCourses": 6, "prerequisites": [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4]], "expected": True},
        {"numCourses": 3, "prerequisites": [[1, 0], [1, 2], [0, 1]], "expected": False},
        {"numCourses": 5, "prerequisites": [], "expected": True},
    ]

    for i, case in enumerate(test_cases, start=1):
        actual = solution.canFinish(case["numCourses"], case["prerequisites"])
        assert actual == case["expected"], (
            f"Test {i} failed: numCourses={case['numCourses']}, "
            f"prerequisites={case['prerequisites']}, "
            f"expected={case['expected']}, got={actual}"
        )

    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
