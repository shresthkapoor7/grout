class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range (0, len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                temp = nums[i] + nums[j] + nums[k]
                t = [nums[i], nums[j], nums[k]]
                if temp == 0:
                    res.add(tuple(t))
                    j += 1
                    k -= 1
                elif temp > 0:
                    k -= 1
                else:
                    j += 1

        return [list(i) for i in res]