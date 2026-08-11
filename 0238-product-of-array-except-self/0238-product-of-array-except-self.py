class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        l = 1
        
        re = [1]*len(nums)

        for i in range(len(nums)):
            re[i] = l
            l*=nums[i]

        r = 1

        for i in range(len(nums)-1,-1,-1):
            re[i]*=r
            r*=nums[i]
        

        return re