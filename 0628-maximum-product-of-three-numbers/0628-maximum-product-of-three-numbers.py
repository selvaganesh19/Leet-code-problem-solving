class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()


        op1 = nums[-1] * nums[-2] * nums[-3]
        op2 = nums[0] * nums[1] * nums[-1]

        return max(op1,op2)