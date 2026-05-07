class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        m, n = len(matrix), len(matrix[0])
        for line in matrix:
            l, r = 0, n - 1
            if target > line[-1]:
                continue
            if target < line[0]:
                return False
            while l <= r:
                mid = l + ((r-l)//2)
                if line[mid] < target:
                    l = mid + 1
                elif line[mid] > target:
                    r = mid - 1
                else:
                    return True
        
        return False