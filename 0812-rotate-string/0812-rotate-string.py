class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        
        if goal in (s+s) and len(goal)==len(s):
            return True
        return False