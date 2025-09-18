class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        f={}

        for i in s:
            f[i] = f.get(i,0)+1

        
        for i,c in enumerate(s):
            if f[c] ==1:
                return i
        
        return -1