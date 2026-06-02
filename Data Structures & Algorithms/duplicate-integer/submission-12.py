import random
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        def bruteforce(nums: List[int]) -> bool:
            # time = O(n*n), space = O(1)
            for i in range (0, len(nums)):
                for j in range (0, len(nums)):
                    if i != j and nums[i] == nums[j]:
                        return True
            return False

        def sortnums(nums: List[int]) -> bool:
            # time = O(nlogn), space = O(n)
            nums.sort()
            for i in range(0, len(nums)-1):
                if nums[i] == nums[i+1]:
                    return True
            return False

        def hashsets(nums: List[int]) -> bool:
            # time = O(n), space = O(n)
            seen = set()
            for num in nums:
                if num in seen:
                    return True
                seen.add(num)
            return False
        
        def cleanest(nums: List[int]) -> bool:
            # time = O(n), space = O(n)
            return len(set(nums)) < len(nums)
        
        # use of freewill
        possibleSolutions = [sortnums, hashsets, cleanest]
        return random.choice(possibleSolutions)(nums)

        