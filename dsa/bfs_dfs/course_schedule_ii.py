"""
LeetCode 210: Course Schedule II

Why this one:
- It is the natural follow-up to Course Schedule.
- It reuses the same adjacency-list setup, but now you must return an order.
- It trains topological sort, which is a core directed-graph interview pattern.
- Amazon-focused graph prep lists continue to include it.

Problem summary:
There are `numCourses` total courses labeled from `0` to `numCourses - 1`.
You are given `prerequisites` where `prerequisites[i] = [a, b]` means you
must take course `b` before course `a`.

Return any valid order in which you can finish all courses. If it is
impossible, return an empty list.

Examples:
- numCourses = 2, prerequisites = [[1, 0]] -> [0, 1]
- numCourses = 4, prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]] -> [0, 1, 2, 3] or [0, 2, 1, 3]
- numCourses = 1, prerequisites = [] -> [0]

Suggested constraints:
- Runtime target: O(V + E)

References:
- https://leetcode.com/problems/course-schedule-ii/
- https://leetcode.com/discuss/post/7454010/graph-problems-for-amazon-sde-1-intervie-96rq/
- https://leetcode.com/discuss/post/7474246/top-120-most-frequently-asked-amazon-sde-imwy/
- https://leetcode.com/discuss/study-guide/6125954/PatternandTemplate-Topological-Sorting-Pattern-in-Graph-Problems/
"""


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        """
        Implement graph traversal / topological sort to return a valid course order.
        """
        adjList = [[] for i in range (0, numCourses)]
        for course, prereq in prerequisites:
            adjList[course].append(prereq)
        
        visiting = set()
        visited = set()
        order = []
        
        def dfs(course: int) -> bool:
            if course in visiting:
                return False
            if course in visited:
                return True
            
            visiting.add(course)

            for preq in adjList[course]:
                if not dfs(preq):
                    return False
            
            visiting.remove(course)
            visited.add(course)
            order.append(course)
            return True

        
        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return order


def is_valid_order(order: list[int], numCourses: int, prerequisites: list[list[int]]) -> bool:
    if len(order) != numCourses:
        return False

    position = {}
    for i, course in enumerate(order):
        if course in position or not (0 <= course < numCourses):
            return False
        position[course] = i

    for course, prereq in prerequisites:
        if position[prereq] > position[course]:
            return False

    return True


def run_tests() -> None:
    solution = Solution()

    test_cases = [
        {"numCourses": 2, "prerequisites": [[1, 0]], "possible": True},
        {"numCourses": 2, "prerequisites": [[1, 0], [0, 1]], "possible": False},
        {"numCourses": 4, "prerequisites": [[1, 0], [2, 0], [3, 1], [3, 2]], "possible": True},
        {"numCourses": 1, "prerequisites": [], "possible": True},
        {"numCourses": 3, "prerequisites": [[1, 0], [2, 1]], "possible": True},
        {"numCourses": 3, "prerequisites": [[1, 0], [0, 2], [2, 1]], "possible": False},
        {"numCourses": 5, "prerequisites": [], "possible": True},
        {"numCourses": 5, "prerequisites": [[1, 0], [2, 0], [3, 1], [4, 3]], "possible": True},
        {"numCourses": 4, "prerequisites": [[1, 0], [2, 1], [3, 2], [1, 3]], "possible": False},
        {"numCourses": 6, "prerequisites": [[1, 0], [2, 0], [3, 1], [4, 2], [5, 3], [5, 4]], "possible": True},
    ]

    for i, case in enumerate(test_cases, start=1):
        actual = solution.findOrder(case["numCourses"], case["prerequisites"])

        if case["possible"]:
            assert is_valid_order(actual, case["numCourses"], case["prerequisites"]), (
                f"Test {i} failed: numCourses={case['numCourses']}, "
                f"prerequisites={case['prerequisites']}, got invalid order={actual}"
            )
        else:
            assert actual == [], (
                f"Test {i} failed: numCourses={case['numCourses']}, "
                f"prerequisites={case['prerequisites']}, expected=[], got={actual}"
            )

    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
