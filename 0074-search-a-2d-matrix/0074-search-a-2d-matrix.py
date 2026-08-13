class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = len(matrix)
        col = len(matrix[0])

        l,r=0,row * col - 1
        m=0
        num=0

        while l<= r:
            m = l+(r-l)//2

            num = matrix[m//col][m%col]

            if num == target:
                return True
            elif num < target:
                l = m+1
            else:
                r=m-1
        
        return False

