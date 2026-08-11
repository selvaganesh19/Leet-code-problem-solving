class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        st = []

        max_len = 0

        for i, he in enumerate(heights):
            start=i

            while st and he < st[-1][0]:
                h,j =  st.pop()
                w = i - j 
                max_len = max(max_len,h*w)
                start = j
            
            st.append((he, start))

        while st:
            h,j = st.pop()
            w = len(heights) - j

            max_len = max(max_len,h*w)
        
        return max_len