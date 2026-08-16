# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """


        curr = head

        for _ in range(k):
            if not curr: return head
            curr =  curr.next
        
        pre = None
        curr = head

        for _ in range(k):
            nxt = curr.next
            curr.next = pre
            pre = curr
            curr = nxt
        

        head.next = self.reverseKGroup(curr, k)
        return pre