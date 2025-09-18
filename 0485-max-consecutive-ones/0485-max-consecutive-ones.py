class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        res = 0

        for i in nums:
            if i ==1:
                count+=1
                res = max(count,res)
            else:
                count = 0
        
        return res
