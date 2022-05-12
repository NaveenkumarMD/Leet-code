class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """


        if not head:
            return None

        cur, prev = head, None
        while m > 1:
            prev = cur
            cur = cur.next
            m, n = m - 1, n - 1


        tail, con = cur, prev


        while n:
            third = cur.next
            cur.next = prev
            prev = cur
            cur = third
            n -= 1
            
        if con:
            con.next=prev
        else:
            head=prev
        tail.next=cur
        return head
        