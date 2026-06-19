"""
LeetCode 39: Combination Sum

Why this one:
- It is one of the cleanest medium backtracking problems.
- It trains the core pattern: choose -> recurse -> undo.
- It forces you to think about when you can reuse a choice and when to move on.
- It is common interview practice for recursion and backtracking.

Problem summary:
You are given a list of distinct positive integers called `candidates` and a
target integer `target`.

Return all unique combinations of `candidates` where the chosen numbers sum to
`target`.

You may use the same number from `candidates` multiple times.
Two combinations are unique if they differ in at least one chosen value count.

Examples:
- candidates = [2, 3, 6, 7], target = 7 -> [[2, 2, 3], [7]]
- candidates = [2, 3, 5], target = 8 -> [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
- candidates = [2], target = 1 -> []

Suggested constraints:
- 1 <= len(candidates) <= 30
- 1 <= candidates[i] <= 200
- All values in `candidates` are distinct
- 1 <= target <= 500
- Runtime target: exponential backtracking with pruning

Practice protocol before coding:
- Pattern:
- Data structure:
- Brute force:
- Optimized idea:
- Invariant:
- Time complexity:
- Space complexity:

References:
- https://leetcode.com/problems/combination-sum/
"""


class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        """
        Implement backtracking here.

        Backtracking reminders:
        - Keep a `path` list for the current combination.
        - Decide what the recursive state means.
        - Reuse the same candidate only when that matches your recursion design.
        - Use `path.copy()` when saving an answer.
        - Always undo with `pop()` after the recursive call.
        """
        raise NotImplementedError("Write the backtracking solution here.")


def normalize(result: list[list[int]]) -> list[list[int]]:
    return sorted(sorted(combination) for combination in result)


def run_tests() -> None:
    solution = Solution()

    test_cases = [
        {
            "candidates": [2, 3, 6, 7],
            "target": 7,
            "expected": [[2, 2, 3], [7]],
        },
        {
            "candidates": [2, 3, 5],
            "target": 8,
            "expected": [[2, 2, 2, 2], [2, 3, 3], [3, 5]],
        },
        {
            "candidates": [2],
            "target": 1,
            "expected": [],
        },
        {
            "candidates": [1],
            "target": 1,
            "expected": [[1]],
        },
        {
            "candidates": [1],
            "target": 2,
            "expected": [[1, 1]],
        },
        {
            "candidates": [8, 7, 4, 3],
            "target": 11,
            "expected": [[3, 4, 4], [3, 8], [4, 7]],
        },
    ]

    try:
        for i, case in enumerate(test_cases, start=1):
            actual = solution.combinationSum(case["candidates"], case["target"])
            assert normalize(actual) == normalize(case["expected"]), (
                f"Test {i} failed: candidates={case['candidates']}, "
                f"target={case['target']}, expected={case['expected']}, got={actual}"
            )
    except NotImplementedError as exc:
        print(exc)
        print("Implement Solution.combinationSum() and run this file again.")
        return

    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
