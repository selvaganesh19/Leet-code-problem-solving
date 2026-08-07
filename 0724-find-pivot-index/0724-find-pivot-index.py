class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tots = sum(nums)
        l = r = 0
        
        for i in range(len(nums)):
            r = tots - l - nums[i]

            if l == r :
                return i 
            else:
                l+=nums[i]
        
        return -1

