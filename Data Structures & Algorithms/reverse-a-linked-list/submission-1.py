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
            out = ListNode(t.val, out)
            t = t.next
            

        return out
