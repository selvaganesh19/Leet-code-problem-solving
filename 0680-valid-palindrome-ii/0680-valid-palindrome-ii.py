class Solution:
    def ispal(self,s: str) -> bool:
        return s == s[::-1]
    
    def validPalindrome(self, s: str) -> bool:
        i , j = 0, len(s)-1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return self.ispal(s[i+1:j+1]) or self.ispal(s[i:j])
        return True
        