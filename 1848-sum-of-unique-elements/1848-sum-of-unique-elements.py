class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=0
        f={}

        for i in nums:
            f[i] = f.get(i,0)+1
        
        for i in f:
            if f[i] == 1:
                s+=i

        return s