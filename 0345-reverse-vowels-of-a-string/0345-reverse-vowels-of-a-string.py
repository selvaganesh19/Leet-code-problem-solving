class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        v = "aeiouAEIOU"
        vow=[]

        for i in range(0,len(s)):
            if s[i] in v:
                vow.append(s[i])
                s[i]= None
        
        for i in range(len(s)):
            if s[i] == None:
                if vow:
                    s[i] = vow.pop()
        
        return "".join(s)
        
