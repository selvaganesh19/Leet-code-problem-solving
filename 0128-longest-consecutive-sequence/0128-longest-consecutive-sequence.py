class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set(nums)

        c=0

        for nums in s:
            if nums -1 not in s:
                st = nums
                 
                while st + 1 in s:
                    st+=1
            
                c = max(c,st-nums+1)

        
        return c 
         