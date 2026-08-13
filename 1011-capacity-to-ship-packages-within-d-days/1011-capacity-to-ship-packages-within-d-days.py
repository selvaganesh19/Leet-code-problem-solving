class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """

        l,r=max(weights),sum(weights)

        res = r

        def canShip(cap):
            ships =1 
            currCap = cap

            for w in weights:
                if currCap - w < 0:
                    ships+=1
                    currCap = cap
                currCap-=w
            
            return ships <= days


        while l <= r:
            m = l+ (r-l) //2

            if canShip(m):
                res = min(res,m)

                r = m -1
            else:
                l = m +1
        
        return res
