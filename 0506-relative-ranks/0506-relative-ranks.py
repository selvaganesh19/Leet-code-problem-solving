class Solution(object):
    def findRelativeRanks(self, s):
        """
        :type score: List[int]
        :rtype: List[str]
        """

        n = len(s)
        rankmap ={}

        for rank , val in enumerate(sorted(s, reverse=True), 1):
            if rank == 1:
                rankmap[val] = "Gold Medal"
            elif rank == 2:
                rankmap[val] = "Silver Medal"
            elif rank == 3:
                rankmap[val] = "Bronze Medal"
            else:
                rankmap[val] = str(rank)
        
        return [rankmap[i] for i in s]




