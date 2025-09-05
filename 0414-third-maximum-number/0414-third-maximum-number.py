class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = set(nums)

        if len(res) < 3:
            return max(res)
        
        res.remove(max(res))
        res.remove(max(res))

        return max(res)