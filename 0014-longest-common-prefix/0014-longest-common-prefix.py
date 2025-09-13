class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        first = strs[0]

        for i in strs:
            while not i.startswith(first):
                first = first[:-1]
            
        return first