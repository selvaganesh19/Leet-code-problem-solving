class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        l = 1

        res = [1]*len(nums)

        for i in range(len(nums)):
            res[i] = l
            l*=nums[i]

        r = 1

        for i in range(len(nums)-1,-1,-1):
            res[i]*=r
            r*=nums[i]
        
        return res