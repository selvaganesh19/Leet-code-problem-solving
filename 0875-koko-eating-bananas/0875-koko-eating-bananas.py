class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        l = 1
        r = max(piles)
        res = r

        while l <= r:
            m = l + (r - l) // 2

            hrs = 0

            for p in piles:
                hrs += math.ceil(p / float(m))

            if hrs <= h:
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1

        return res

    