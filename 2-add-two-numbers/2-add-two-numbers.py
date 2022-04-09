# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s,t=l1,l2
        new=ListNode(0)
        x=new
        carry=0
        while s or t:
            e=0 if s is None else s.val
            o=0 if t is None else t.val
            temp=e+o+carry
            if temp<10:
                carry=0
                f=temp
            else:
                f=temp%10
                carry=temp//10
            if s is not None:s=s.next
            if t is not None:t=t.next
            new.next=ListNode(f)
            new=new.next
       
        if carry>0:
            new.next=ListNode(carry)
            new=new.next
        return x.next