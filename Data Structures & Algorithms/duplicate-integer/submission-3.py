class Solution:
    def naiveSolution(self, nums: List[int]) -> bool:
        for i in range (0, len(nums)):
            for j in range (0, len(nums)):
                if i != j and nums[i] == nums[j]:
                    return True
        return False
    
    def betterApproach(self, nums: List[int]) -> bool:
        nums.sort()
        j = 1
        for i in range (0, len(nums)):
            if j < len(nums) and nums[i] == nums[j]:
                return True
            j += 1
        return False
    
    def bestApproach(self, nums: List[int]) -> bool:
        my_dict = {}
        for i in range (0, len(nums)):
            if nums[i] in my_dict:
                my_dict[nums[i]] += 1
            else:
                my_dict[nums[i]] = 1
        return len(my_dict) != len(nums)
    
    def hasDuplicate(self, nums: List[int]) -> bool:
        return self.bestApproach(nums)