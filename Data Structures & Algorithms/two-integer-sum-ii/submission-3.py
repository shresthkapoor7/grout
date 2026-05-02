class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # binary search

        for i in range(len(numbers)): #need to check for each
            l, r = i + 1, len(numbers) - 1
            temp = target - numbers[i]

            while l <= r:
                mid = l + (r-l) // 2
                if numbers[mid] == temp:
                    return [i + 1, mid + 1]
                elif numbers[mid] < temp:
                    l = mid + 1
                else:
                    r = mid - 1
        return []