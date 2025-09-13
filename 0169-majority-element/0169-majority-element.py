class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        f={}

        for i in nums:
            f[i] =  f.get(i,0)+1
        
    
        return max(f,key=f.get)