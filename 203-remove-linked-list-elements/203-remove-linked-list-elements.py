class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val==val:
            head=head.next
        if head==None:
            return None
        else:
            prev=head
            curr=prev.next
            while curr:
                if curr.val==val:
                    curr=curr.next
                    prev.next=curr
                else:
                    curr=curr.next
                    prev=prev.next
            return head