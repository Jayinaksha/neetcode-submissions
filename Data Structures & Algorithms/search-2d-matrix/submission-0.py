class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) #length of colums
        n = len(matrix[0]) #length of rows
        left = 0
        right = (m*n)-1
        while left <= right:
            mid = (left+right)//2
            if target == matrix[mid//n][mid%n]:
                return True
            elif target > matrix[mid//n][mid%n]:
                left = mid+1
            else:
                right = mid-1
        return False