"""
LeetCode 33: Search in Rotated Sorted Array

Why this one:
- It is a core binary search pattern.
- It matches the rotated-array focus from `amazon_oa_dsa.md`.
- Amazon-focused prep lists and interview discussions repeatedly include it.

Problem summary:
You are given a sorted array that has been rotated at an unknown pivot.
All values are distinct. Return the index of `target` if it exists, else `-1`.

Examples:
- nums = [4, 5, 6, 7, 0, 1, 2], target = 0 -> 4
- nums = [7, 8, 0, 1, 2, 3, 4, 5, 6],
- nums = [4, 5, 6, 7, 0, 1, 2], target = 3 -> -1
- nums = [1], target = 0 -> -1

Suggested constraints:
- Runtime target: O(log n)

References:
- https://leetcode.com/problems/search-in-rotated-sorted-array/
- https://leetcode.com/discuss/post/7483322/ultimate-binary-search-master-list-for-a-yes1/
- https://leetcode.com/discuss/interview-experience/493936/amazon-sde2-seattle-jan-2020-reject/
"""


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """
        Implement binary search on a rotated sorted array.

        Return:
        - index of target if found
        - -1 otherwise  
        """
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
        
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
        
        raise NotImplementedError("Implement the binary search solution here.")


def run_tests() -> None:
    solution = Solution()

    test_cases = [
        {"nums": [4, 5, 6, 7, 0, 1, 2], "target": 0, "expected": 4},
        {"nums": [4, 5, 6, 7, 0, 1, 2], "target": 3, "expected": -1},
        {"nums": [1], "target": 0, "expected": -1},
        {"nums": [1], "target": 1, "expected": 0},
        {"nums": [1, 3], "target": 3, "expected": 1},
        {"nums": [3, 1], "target": 1, "expected": 1},
        {"nums": [5, 1, 3], "target": 5, "expected": 0},
        {"nums": [5, 1, 3], "target": 3, "expected": 2},
        {"nums": [6, 7, 8, 1, 2, 3, 4, 5], "target": 2, "expected": 4},
        {"nums": [6, 7, 8, 1, 2, 3, 4, 5], "target": 9, "expected": -1},
    ]

    for i, case in enumerate(test_cases, start=1):
        actual = solution.search(case["nums"], case["target"])
        assert actual == case["expected"], (
            f"Test {i} failed: nums={case['nums']}, target={case['target']}, "
            f"expected={case['expected']}, got={actual}"
        )

    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
