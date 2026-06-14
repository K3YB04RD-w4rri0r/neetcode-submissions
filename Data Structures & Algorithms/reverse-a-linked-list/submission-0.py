# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # for 3 , 1 , 2
        # means head = ListNode(3, ListNode(1, ListNode(2 ...)))
        out = None
        t = head
        while t:
            h = t.val
            t = t.next
            out = ListNode(h, out)
            

        return out
