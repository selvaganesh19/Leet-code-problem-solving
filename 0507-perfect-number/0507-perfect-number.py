class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """

        res = {6, 28, 496, 8128, 33550336}

        return num in res