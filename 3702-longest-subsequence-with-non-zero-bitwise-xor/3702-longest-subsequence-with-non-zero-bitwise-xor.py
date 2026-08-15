class Solution(object):
    def longestSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        s = 0
        f=False

        for i in nums:
            if i>0:
                f = True
            s=s^i

        if f==False: return 0

        if s>0: return len(nums)

        return len(nums)-1





