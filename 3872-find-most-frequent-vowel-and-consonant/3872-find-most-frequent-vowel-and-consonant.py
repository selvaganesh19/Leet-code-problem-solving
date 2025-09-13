class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        f1={}
        f2={}

        for i in s:
            if i in "aeiouAEIOU":
                f1[i] = f1.get(i,0)+1
            else:
                f2[i] = f2.get(i,0)+1
        
        r1 = max(f1.values()) if f1 else 0
        r2 = max(f2.values()) if f2 else 0

        return r1+r2