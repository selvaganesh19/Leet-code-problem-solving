class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """

        a = list(s)

        i=0

        for j in range(len(s)):
            if i > 0 and a[i-1] == a[j]:
                i-=1
            else:
                a[i]=a[j]
                i+=1
        
        return "".join(a[:i])

