class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ls = []

        for ch in s:
            if ch.isalnum():
                ls.append(ch.lower())

        l=0
        r=len(ls)-1


        while l < r:
            if ls[l] != ls[r]:
                return False
            else:
                l+=1
                r-=1
        
        return True

