class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)

        total = n * (n+1) // 2
        setsum = sum(set(nums))
        su = sum(nums)
        dup = su - setsum
        mis = total - setsum
        return [dup,mis]
            
