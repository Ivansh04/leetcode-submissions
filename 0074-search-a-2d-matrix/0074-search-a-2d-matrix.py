class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                if matrix[j][i]==target:
                    return True
        return False
        