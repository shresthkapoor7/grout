"""
LeetCode 34: Find First and Last Position of Element in Sorted Array

Why this one:
- It is a core binary search variant for duplicates.
- It complements rotated-array search without repeating the same idea.
- Amazon-focused prep lists still include it as a standard binary-search pattern.

Problem summary:
Given a sorted array of integers `nums` in non-decreasing order, find the
starting and ending position of a given `target`.

Return:
- [first_index, last_index] if target exists
- [-1, -1] otherwise

Examples:
- nums = [5, 7, 7, 8, 8, 10], target = 8 -> [3, 4]
- nums = [5, 7, 7, 8, 8, 10], target = 6 -> [-1, -1]
- nums = [], target = 0 -> [-1, -1]

Suggested constraints:
- Runtime target: O(log n)

References:
- https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
- https://leetcode.com/discuss/post/7483322/ultimate-binary-search-master-list-for-a-yes1/
- https://leetcode.com/discuss/post/7441588/binary-search-patterns-that-solve-80-of-qu83f/
- https://leetcode.com/discuss/post/7474246/top-120-most-frequently-asked-amazon-sde-imwy/
"""


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def find_bound(find_first: bool) -> int:
            left, right = 0, len(nums) - 1
            ans = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    ans = mid
                    if find_first:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return ans

        return [find_bound(True), find_bound(False)]



def run_tests() -> None:
    solution = Solution()

    test_cases = [
        {"nums": [5, 7, 7, 8, 8, 10], "target": 8, "expected": [3, 4]},
        {"nums": [5, 7, 7, 8, 8, 10], "target": 6, "expected": [-1, -1]},
        {"nums": [], "target": 0, "expected": [-1, -1]},
        {"nums": [1], "target": 1, "expected": [0, 0]},
        {"nums": [1], "target": 0, "expected": [-1, -1]},
        {"nums": [2, 2], "target": 2, "expected": [0, 1]},
        {"nums": [1, 2, 2, 2, 3], "target": 2, "expected": [1, 3]},
        {"nums": [1, 2, 3, 4, 5], "target": 4, "expected": [3, 3]},
        {"nums": [1, 3, 3, 3, 5, 7], "target": 3, "expected": [1, 3]},
        {"nums": [1, 1, 1, 1, 1], "target": 1, "expected": [0, 4]},
    ]

    for i, case in enumerate(test_cases, start=1):
        actual = solution.searchRange(case["nums"], case["target"])
        assert actual == case["expected"], (
            f"Test {i} failed: nums={case['nums']}, target={case['target']}, "
            f"expected={case['expected']}, got={actual}"
        )

    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
