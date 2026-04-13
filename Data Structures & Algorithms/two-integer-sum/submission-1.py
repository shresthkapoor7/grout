class Solution:
    def easySoln(self, nums: List[int], target: int):
        for i in range (len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    return [i, j]
    
    def betterApproach(self, nums: List[int], target: int):
        # Can't sort, because indexes are important
        my_dict = {}
        for i in range (len(nums)):
            if target - nums[i] in my_dict:
                j = my_dict[target-nums[i]]
                return [min(i, j), max(i, j)]
            my_dict[nums[i]] = i

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return self.betterApproach(nums, target)