class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # brute force
        maxArea = 0
        for i in range(0, len(heights)):
            for j in range(0, len(heights)):
                if i != j:
                    area = (j-i) * min(heights[j], heights[i])
                    maxArea = max(maxArea, area)
        return maxArea
        