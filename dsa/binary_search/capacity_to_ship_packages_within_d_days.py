"""
LeetCode 1011: Capacity To Ship Packages Within D Days

Why this one:
- It is a standard binary-search-on-answer problem.
- It complements rotated search and boundary search with a different pattern.
- Amazon-oriented binary search prep lists continue to include it.

Problem summary:
You are given an array `weights` where `weights[i]` is the weight of the
ith package on a conveyor belt. Packages must be shipped in the given order.

Each day, you load packages onto the ship in order until adding the next
package would exceed the ship's capacity. Return the least ship capacity
needed to ship all packages within `days` days.

Examples:
- weights = [1,2,3,4,5,6,7,8,9,10], days = 5 -> 15
- weights = [3,2,2,4,1,4], days = 3 -> 6
- weights = [1,2,3,1,1], days = 4 -> 3

Suggested constraints:
- Runtime target: O(n log S), where S is the answer range

References:
- https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
- https://leetcode.com/discuss/post/7483322/ultimate-binary-search-master-list-for-a-yes1/
- https://www.greenlearnific.com/post/common-binary-search-questions-asked-in-amazon-interview
- https://leetcode.com/discuss/study-guide/3444552/binary-search-on-answer-template-generic-template/
"""


class Solution:
    def check(self, weights: list[int], days: int, capacity: int) -> bool:
        currWeight = 0
        currDays = 1
        for weight in weights:
            if currWeight + weight <= capacity:
                currWeight += weight
            else:
                currDays += 1
                currWeight = weight
        return currDays <= days

    def shipWithinDays(self, weights: list[int], days: int) -> int:
        """
        Implement binary search on the minimum valid ship capacity.
        """
        minWeight = max(weights)
        maxWeight = sum(weights)
        answer = 0
        while minWeight <= maxWeight:
            mid = (minWeight + maxWeight) // 2

            if self.check(weights, days, mid):
                answer = mid
                maxWeight = mid - 1
            else:
                minWeight = mid + 1

        return answer
        



def run_tests() -> None:
    solution = Solution()

    test_cases = [
        {"weights": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "days": 5, "expected": 15},
        {"weights": [3, 2, 2, 4, 1, 4], "days": 3, "expected": 6},
        {"weights": [1, 2, 3, 1, 1], "days": 4, "expected": 3},
        {"weights": [5], "days": 1, "expected": 5},
        {"weights": [5, 5, 5, 5], "days": 2, "expected": 10},
        {"weights": [7, 2, 5, 10, 8], "days": 2, "expected": 18},
        {"weights": [7, 2, 5, 10, 8], "days": 5, "expected": 10},
        {"weights": [9, 8, 7, 6, 5], "days": 5, "expected": 9},
        {"weights": [9, 8, 7, 6, 5], "days": 1, "expected": 35},
        {"weights": [2, 2, 2, 2, 2, 2], "days": 3, "expected": 4},
    ]

    for i, case in enumerate(test_cases, start=1):
        actual = solution.shipWithinDays(case["weights"], case["days"])
        assert actual == case["expected"], (
            f"Test {i} failed: weights={case['weights']}, days={case['days']}, "
            f"expected={case['expected']}, got={actual}"
        )

    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
