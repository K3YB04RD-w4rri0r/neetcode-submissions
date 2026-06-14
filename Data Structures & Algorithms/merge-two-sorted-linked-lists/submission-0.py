class Solution:
    def mergeTwoLists(self, list1, list2):
        t1 = list1
        t2 = list2
        out = None


        while t1 and t2:
            h1 = t1.val
            h2 = t2.val

            if h1 <= h2:
                out = ListNode(h1, out)
                t1 = t1.next
            else:
                out = ListNode(h2, out)
                t2 = t2.next


        while t1:
            out = ListNode(t1.val, out)
            t1 = t1.next

        while t2:
            out = ListNode(t2.val, out)
            t2 = t2.next


        rev = None
        t = out

        while t:
            rev = ListNode(t.val, rev)
            t = t.next

        return rev