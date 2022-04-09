# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr=[]
        temp=head
        while temp:
            arr.append(temp.val)
            temp=temp.next
        arr[k-1],arr[-k]=arr[-k],arr[k-1]
        x=curr=ListNode(0)
        for i in arr:
                x.next=ListNode(i)
                x=x.next
        return curr.next
        