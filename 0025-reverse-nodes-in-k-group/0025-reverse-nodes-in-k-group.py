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

        dummy = jump = ListNode(0)

        dummy.next = l = r = head

        while True:
            c = 0
            while r and c < k:
                r = r.next
                c+=1
            
            if c == k:
                pre = r
                curr = l

                for _ in range(k):
                    nxt = curr.next
                    curr.next = pre
                    pre = curr
                    curr = nxt
                
                jump.next = pre
                jump = l
                l = r
            else:
                return dummy.next

