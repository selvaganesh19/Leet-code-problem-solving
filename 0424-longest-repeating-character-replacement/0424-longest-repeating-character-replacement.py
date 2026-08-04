class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        w = {}
        m=0
        b=l=0

        for r in range(len(s)):
            w[s[r]] = w.get(s[r],0)+1
            m = max(m,w[s[r]])

            while r- l+1 - m > k:
                w[s[l]] -=1
                l+=1

            b = max(b,r-l+1)
        
        return b