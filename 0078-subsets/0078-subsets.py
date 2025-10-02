class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        n= len(nums)

        subset=[]

        for i in range(1 << n):
            curr_set = []
            for j in range(n):
                if(i >> j) & 1:
                    curr_set.append(nums[j])
            subset.append(curr_set)
        
        return subset