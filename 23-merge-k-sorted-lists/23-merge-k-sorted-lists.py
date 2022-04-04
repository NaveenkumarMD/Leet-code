# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergelist(lists):
            x=ListNode(0)
            curr=x
            for li in lists:
                temp=li
                while temp is not None:
                    x.next=ListNode(temp.val)
                    x=x.next
                    temp=temp.next
            return curr.next
        def sorting(head):
            p=head
            temp=head
            index=None
            if head is None:
                return None
            else:
                while temp is not None:
                    index=temp.next
                    while index is not None:
                        if temp.val>index.val:
                            x=temp.val
                            temp.val=index.val
                            index.val=x
                        index=index.next
                    temp=temp.next
            return p
        return sorting(mergelist(lists))
        