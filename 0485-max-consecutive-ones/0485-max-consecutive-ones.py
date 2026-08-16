class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=0

        m = defaultdict(int)
        res=0

        for r in range(len(nums)):
            m[nums[r]]+=1

            c=0
            if nums[r] == 1:
                c+=1
                res = max(res,r-l+1)
            else:
                l = r+1
        
        return res