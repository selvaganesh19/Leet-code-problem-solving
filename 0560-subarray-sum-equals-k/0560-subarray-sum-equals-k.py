class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        s = {0: 1}
        p = c = 0
        for x in nums:
            p += x
            c += s.get(p - k, 0)
            s[p] = s.get(p, 0) + 1
        
        return c