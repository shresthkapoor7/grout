class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # two pointer approach

        maxArea = 0
        i, j = 0, len(heights)-1

        while i < j:
            area = (j - i) * min(heights[i], heights[j])
            maxArea = max(maxArea, area)
            if heights[j] < heights[i]:
                j -= 1
            else:
                i += 1
        return maxArea
        