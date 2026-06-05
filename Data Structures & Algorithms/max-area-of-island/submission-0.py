class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]

        def dfs(i, j) -> int:
            if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == 0:
                return 0
            
            grid[i][j] = 0
            total = 1
            for dr, dc in directions:
                total += dfs(i + dr, j + dc)
            
            return total
        
        total = 0
        for i in range(0, rows):
            for j in range(0, cols):
                if grid[i][j] == 1:
                    total = max(dfs(i, j), total)

        return total