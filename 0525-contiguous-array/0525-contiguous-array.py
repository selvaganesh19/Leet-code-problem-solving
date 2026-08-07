class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = l = 0

        map = {0:-1}

        for i in range(len(nums)):
            if nums[i] == 0:
                count-=1
            else:
                count+=1
            
            if count in map:
                l = max(l,i-map[count])
            else:
                map[count] = i
        
        return l
