class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(grid: List[List[str]], i: int, j: int, n: int, m: int) -> None: 
            if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] == "0":
                return
            print(grid)
            if grid[i][j] == "1":
                grid[i][j] = "0"
                dfs(grid, i-1, j, n, m) 
                dfs(grid, i+1, j, n, m) 
                dfs(grid, i, j-1, n, m) 
                dfs(grid, i, j+1, n, m)
                return

        n = len(grid)
        m = len(grid[0])
        total = 0
        for i in range (0, n):
            for j in range (0, m):
                if grid[i][j] == "1":
                    print("i")
                    dfs(grid, i, j, n, m)
                    print("j")
                    total += 1
        return total


        