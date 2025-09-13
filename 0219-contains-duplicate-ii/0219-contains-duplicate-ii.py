class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        st = {}
        for i in range(len(nums)):
            if nums[i] in st and abs(i-st[nums[i]]) <= k:
                return True
            st[nums[i]] = i
        return False