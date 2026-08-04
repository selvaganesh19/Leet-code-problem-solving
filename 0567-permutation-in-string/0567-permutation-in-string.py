class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        if len(s1) > len(s2): return False
        
        w1 = {}
        w2 ={}

        
        for i in range(len(s1)):
            w1[s1[i]] = w1.get(s1[i],0)+1
            w2[s2[i]] = w2.get(s2[i],0)+1
        
        if w1 == w2 : return True

        for r in range(len(s1),len(s2)):
            w2[s2[r]] = w2.get(s2[r],0)+1

            l = s2[r-len(s1)]

            w2[l] -=1

            if w2[l] == 0:
                del w2[l]
            
            if w1 == w2:
                return True
        
        return False

        