class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        low=0

        high=num

        while low <= high:
            mid = (low + high) //2
            sq = mid*mid

            if sq == num:
                return True
            elif sq > num:
                high = mid-1
            else:
                low = mid +1
        
        return False