"""
LeetCode 994: Rotting Oranges

Why this one:
- It is a standard multi-source BFS problem.
- It shifts practice from DFS/cycle detection to queue-based level traversal.
- Amazon-focused graph prep lists continue to include it.

Problem summary:
You are given an `m x n` grid where each cell can have one of three values:
- `0` representing an empty cell
- `1` representing a fresh orange
- `2` representing a rotten orange

Every minute, any fresh orange that is 4-directionally adjacent to a rotten
orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a
fresh orange. If this is impossible, return `-1`.

Examples:
- grid = [[2,1,1],[1,1,0],[0,1,1]] -> 4
- grid = [[2,1,1],[0,1,1],[1,0,1]] -> -1
- grid = [[0,2]] -> 0

Suggested constraints:
- Runtime target: O(m * n)

References:
- https://leetcode.com/problems/rotting-oranges/
- https://leetcode.com/discuss/post/7454010/graph-problems-for-amazon-sde-1-intervie-96rq/
- https://leetcode.com/discuss/post/7474246/top-120-most-frequently-asked-amazon-sde-imwy/
- https://leetcode.com/discuss/interview-question/1760429/amazon-phone-off-campus-interview-questions-feb-2022-rotting-oranges/
"""


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        """
        Implement multi-source BFS to compute the minimum number of minutes.
        """
        raise NotImplementedError("Implement the BFS solution here.")


def run_tests() -> None:
    solution = Solution()

    test_cases = [
        {"grid": [[2, 1, 1], [1, 1, 0], [0, 1, 1]], "expected": 4},
        {"grid": [[2, 1, 1], [0, 1, 1], [1, 0, 1]], "expected": -1},
        {"grid": [[0, 2]], "expected": 0},
        {"grid": [[1]], "expected": -1},
        {"grid": [[2]], "expected": 0},
        {"grid": [[2, 2], [2, 2]], "expected": 0},
        {"grid": [[1, 2]], "expected": 1},
        {"grid": [[2, 1, 1], [1, 1, 1], [0, 1, 2]], "expected": 2},
        {"grid": [[0, 0, 0], [0, 0, 0]], "expected": 0},
        {"grid": [[2, 1, 0, 2], [1, 1, 1, 0], [0, 1, 1, 1]], "expected": 4},
    ]

    for i, case in enumerate(test_cases, start=1):
        grid_copy = [row[:] for row in case["grid"]]
        actual = solution.orangesRotting(grid_copy)
        assert actual == case["expected"], (
            f"Test {i} failed: grid={case['grid']}, "
            f"expected={case['expected']}, got={actual}"
        )

    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
