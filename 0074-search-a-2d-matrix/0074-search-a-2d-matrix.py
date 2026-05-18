class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l=0
        h=len(matrix)-1
        n=len(matrix[0])-1
        while l<=h:
            mid=(l+h)//2
            if target>=matrix[mid][0] and target<=matrix[mid][n]:
                midd=mid
                break
            if matrix[mid][n]<target:
                l=mid+1
            elif matrix[mid][0]>target:
                h=mid-1
        if l>h: return False
        l=0
        h=n
        while l<=h:
            mid=(l+h)//2
            if target==matrix[midd][mid]:
                return True
            elif target<matrix[midd][mid]:
                h=mid-1
            elif target>matrix[midd][mid]:
                l=mid+1
        return False
        