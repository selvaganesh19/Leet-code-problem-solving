class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        v = []

        l = list(s)

        for i in l:
            if i in "AEIOUaieou":
                v.append(i)
        
        if v == []:
            return s
        v.sort()

        count = 0
        for i in range(len(s)):
            if l[i] in "AIEOUaeiou":
                l[i] = v[count]
                count+=1
        
        return "".join(l)
