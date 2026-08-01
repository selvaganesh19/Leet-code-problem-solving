class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        f = defaultdict(list)

        for i in strs:
            c = [0]*26
            for j in i:
                c[ord(j) - ord('a')] +=1
            f[tuple(c)].append(i)
        return list(f.values())

