class Solution:
    def naiveSolution(self, nums: List[int]) -> bool:
        for i in range (0, len(nums)):
            for j in range (0, len(nums)):
                if i != j and nums[i] == nums[j]:
                    return True
        return False

    def hasDuplicate(self, nums: List[int]) -> bool:
        return self.naiveSolution(nums)