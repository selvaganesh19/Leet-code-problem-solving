class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """

        f={}
        r=0

        for i in s:
            f[i] = f.get(i,0)+1
        

        for i in f.values():
            if i % 2 ==0:
                r+=i
            else:
                i-1
        
        return r+1 if r < len(s) else r