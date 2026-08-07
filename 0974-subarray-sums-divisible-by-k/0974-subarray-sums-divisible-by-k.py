class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        s = {0: 1}
        p = c = 0
        for x in nums:
            p  = (p + x) % k
            c += s.get(p, 0)
            s[p] = s.get(p, 0) + 1
        
        return c