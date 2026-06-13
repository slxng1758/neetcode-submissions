class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1
        row = len(matrix) - 1
        while l<=r:
            mid = l + ((r-l)//2)
            if matrix[mid][0]==target:
                return True
            if mid+1<len(matrix) and matrix[mid][0]<target and matrix[mid+1][0]>target:
                row = mid
                break
            elif matrix[mid][0]>target:
                r = mid-1
            else:
                l = mid + 1

        l, r = 0, len(matrix[0])-1
        while l<=r:
            mid = l + ((r-l)//2)
            if matrix[row][mid]==target:
                return True
            if matrix[row][mid]>target:
                r = mid -1
            else:
                l = mid+1
        return False
        