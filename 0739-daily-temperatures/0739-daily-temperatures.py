class Solution(object):
    def dailyTemperatures(self, nums):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        res =  [0]*len(nums)

        s = []

        for i in range(len(nums)):
            while s and nums[s[-1]] < nums[i]:
                ind = s.pop()
                res[ind] = i - ind
            
            s.append(i)  

        return res