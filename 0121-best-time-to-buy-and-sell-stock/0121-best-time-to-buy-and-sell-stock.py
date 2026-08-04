class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        mi=prices[0]
        b=0

        for i in prices:
            mi = min(mi,i)

            b = max(b,i-mi)

        return b

