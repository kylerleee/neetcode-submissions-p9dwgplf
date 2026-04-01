class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = (len(matrix) - 1) // 2
        while m <= len(matrix):
            m = (len(matrix) - 1) // 2
            if len(matrix) < 1:
                
                return False
            if matrix[m][-1] < target:
                matrix = matrix[m+1:]
            elif matrix[m][0] > target:
                matrix = matrix[:m]
            else:
                if target in matrix[m]:
                    return True
                else:
                    return False
        
