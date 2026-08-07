class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        st =[]
        m = {}

        for i in nums2:
            while st and st[-1] < i:
                m[st.pop()] = i

            st.append(i)            


        
        return [m.get(i,-1) for i in nums1]
            