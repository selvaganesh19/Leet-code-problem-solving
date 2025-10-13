class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        f={}

        for i in arr:
            f[i] = f.get(i,0)+1
        
        frq = list(f.values())

        return len(frq) == len(set(frq))