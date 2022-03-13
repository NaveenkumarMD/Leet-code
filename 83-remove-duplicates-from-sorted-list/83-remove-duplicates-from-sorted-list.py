# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        prev=head
        curr=prev.next
        while curr is not None:
            if curr.val==prev.val:
                while curr.val==prev.val:
                    curr=curr.next
                    if curr is None:
                        break
                prev.next=curr
            else:
                curr=curr.next
                prev=prev.next
        return head