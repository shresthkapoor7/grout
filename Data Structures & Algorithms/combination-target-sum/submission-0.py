class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        def dfs(currSum: int, index: int, currList: list[int]) -> None:
            if currSum == target:
                combinations.append(currList.copy())
                return
            if currSum > target or index >= len(candidates):
                return

            currList.append(candidates[index]) # consider
            dfs(currSum + candidates[index], index, currList)

            currList.pop() # don't
            dfs(currSum, index + 1, currList)

            return
        
        combinations = []
        dfs(0, 0, [])
        return combinations