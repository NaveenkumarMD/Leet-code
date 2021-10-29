#using deque
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=head
        from collections import deque
        queue=deque()
        while slow:
            queue.append(slow.val)
            slow=slow.next
        while len(queue)>1:
            if queue.popleft()==queue.pop():
                continue
            else:
                return False
        return True
            
        
# using stack
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack=[]
        slow=head
        while slow:
            stack.append(slow.val)
            slow=slow.next
        print(stack)   
        while head:
            if stack.pop()!=head.val:
                return False
            head=head.next
        if head is None:
            return True
        
# by reversing
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        curr=slow
        prev=nexxt=None
        while  curr:
            nexxt=curr.next
            curr.next=prev
            prev=curr
            curr=nexxt
        
        while prev:
            if prev.val!=head.val:
                return False 
            head=head.next
            prev=prev.next
        return True
            
            
        