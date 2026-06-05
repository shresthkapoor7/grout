class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        total = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(i, j):
            if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] == "0":
                return
            
            grid[i][j] = "0"
            for dr, dc in directions:
                dfs(i + dr, j + dc)

        for i in range (0, n):
            for j in range (0, m):
                if grid[i][j] == "1":
                    dfs(i, j)
                    total += 1
        return total


        