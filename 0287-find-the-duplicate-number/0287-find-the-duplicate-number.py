class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        sl = 0

        while True:
            slow = nums[slow]
            sl = nums[sl]

            if sl == slow:
                return slow
        


        

