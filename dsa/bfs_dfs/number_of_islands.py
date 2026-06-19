"""
LeetCode 200: Number of Islands

Why this one:
- It is the standard grid BFS/DFS traversal problem.
- It matches the graph prep focus on grid traversal and 4-direction movement.
- Amazon-focused prep lists continue to include it frequently.

Problem summary:
Given an `m x n` 2D grid of `"1"`s (land) and `"0"`s (water), return the
number of islands.

An island is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are surrounded by water.

Examples:
- grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ] -> 1
- grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
  ] -> 3

Suggested constraints:
- Runtime target: O(m * n)

References:
- https://leetcode.com/problems/number-of-islands/
- https://leetcode.com/discuss/post/7454010/graph-problems-for-amazon-sde-1-intervie-96rq/
- https://leetcode.com/discuss/post/5039797/bfs-and-dfs-graph-problems-easy-to-mediu-8mz5/
- https://leetcode.com/discuss/post/7474246/top-120-most-frequently-asked-amazon-sde-imwy/
"""


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        """
        Implement DFS or BFS to count connected components in a grid.
        """
        n, m = len(grid), len(grid[0])
        total = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(i, j):
            if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] == "0":
                return

            grid[i][j] = "0"

            for dr, dc in directions:
                dfs(i + dr, j + dc)
        
        for i in range (0, n):
            for j in range (0, m):
                if grid[i][j] == "1":
                    dfs(i, j)
                    total += 1
        return total


def run_tests() -> None:
    solution = Solution()

    test_cases = [
        {
            "grid": [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ],
            "expected": 1,
        },
        {
            "grid": [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ],
            "expected": 3,
        },
        {"grid": [["1"]], "expected": 1},
        {"grid": [["0"]], "expected": 0},
        {
            "grid": [
                ["1", "0", "1", "0"],
                ["0", "1", "0", "1"],
                ["1", "0", "1", "0"],
            ],
            "expected": 6,
        },
        {
            "grid": [
                ["1", "1", "0"],
                ["0", "1", "0"],
                ["0", "0", "1"],
            ],
            "expected": 2,
        },
        {
            "grid": [
                ["0", "0", "0"],
                ["0", "0", "0"],
            ],
            "expected": 0,
        },
        {
            "grid": [
                ["1", "1", "1"],
                ["1", "0", "1"],
                ["1", "1", "1"],
            ],
            "expected": 1,
        },
    ]

    for i, case in enumerate(test_cases, start=1):
        grid_copy = [row[:] for row in case["grid"]]
        actual = solution.numIslands(grid_copy)
        assert actual == case["expected"], (
            f"Test {i} failed: grid={case['grid']}, "
            f"expected={case['expected']}, got={actual}"
        )

    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
