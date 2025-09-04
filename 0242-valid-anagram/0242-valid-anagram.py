class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        f1 ={}
        f2 ={}

        if len(s) != len(t):
            return False
    
        for i in s:
            f1[i] = f1.get(i,0)+1
            
        for i in t:
            f2[i] = f2.get(i,0)+1
            
      
        return f1 == f2