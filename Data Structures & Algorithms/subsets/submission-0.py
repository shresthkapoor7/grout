class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result = []
        def dfs(index: int, path: List[int]) -> None:
            if index == len(nums):
                result.append(path.copy())
                return
            
            path.append(nums[index])
            dfs(index + 1, path)

            path.pop()
            dfs(index + 1, path)
        
        dfs(0, [])
        return result