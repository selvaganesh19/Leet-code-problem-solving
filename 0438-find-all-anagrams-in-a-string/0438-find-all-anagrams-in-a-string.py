class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
        if len(p) > len(s): return []
        
        w1 = {}
        w2 ={}

        
        for i in range(len(p)):
             w1[p[i]] = w1.get(p[i],0)+1
             w2[s[i]] = w2.get(s[i],0)+1
           
        
        res = [0] if w1 == w2 else []

        for r in range(len(p),len(s)):
            w2[s[r]] = w2.get(s[r],0)+1

            l = s[r-len(p)]

            w2[l] -=1

            if w2[l] == 0:
                del w2[l]
            
            if w1 == w2:
                res.append(r-len(p)+1)
        
        return res 