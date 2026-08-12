class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        w = defaultdict(int)

        l=m=0

        for r in range(len(nums)):
            w[nums[r]]+=1

            while w[nums[r]] > k:
                w[nums[l]] -=1
                l+=1
            
            m = max(m,r-l+1)
        
        return m

