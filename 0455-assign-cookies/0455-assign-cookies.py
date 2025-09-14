class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """

        s.sort()
        g.sort()

        i,j,c=0,0,0

        while i<len(g) and j<len(s):
            if s[j] >= g[i]:
                c+=1
                i+=1
            j+=1

        return c


