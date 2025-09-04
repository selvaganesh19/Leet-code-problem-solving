class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        p = 0
        if len(nums) == 1:
            return nums
        for i in range(0, len(nums)):
            if nums[i] != 0:
                nums[p] = nums[i]
                p += 1
            
        for k in range(p, len(nums)):
            nums[k] = 0
            
        return nums