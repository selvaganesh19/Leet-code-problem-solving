class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set(nums)

        c=0

        for i in s:
            if i-1 not in s:
                st = i

                while st+1 in s:
                    st+=1

                c = max(c, st-i+1)
        
        return c
         