class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        n, m = len(grid), len(grid[0])
        total = 0

        def bfs(r, c):
            q = deque()
            grid[r][c] = "0"
            q.append((r, c))

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    i, j = dr + row, dc + col

                    if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] == "0":
                        continue
                    q.append((i, j))
                    grid[i][j] = "0"
            
        for r in range(n):
            for c in range(m):
                if grid[r][c] == "1":
                    bfs(r, c)
                    total += 1
        return total
