class Solution:
    def bfs(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        queue = deque([root])
        depth = 0

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1
        return depth

    def dfs(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return 1 + max(self.dfs(root.left), self.dfs(root.right))
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)