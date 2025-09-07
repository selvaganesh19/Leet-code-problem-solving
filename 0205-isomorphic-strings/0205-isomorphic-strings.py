class Solution(object):
    def isIsomorphic(self, s1, s2):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        m1 ={}
        m2 ={}

        for i in range(len(s1)):
            if s1[i] not in m1:
                m1[s1[i]] = i
            if s2[i] not in m2:
                m2[s2[i]] = i

            if m1[s1[i]] != m2[s2[i]]:
                return False

        return True