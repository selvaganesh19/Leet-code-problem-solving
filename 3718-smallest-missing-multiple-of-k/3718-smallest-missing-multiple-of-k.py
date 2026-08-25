class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        s = set(nums)

        mul = k

        while mul in s:
            mul+=k
        
        return mul