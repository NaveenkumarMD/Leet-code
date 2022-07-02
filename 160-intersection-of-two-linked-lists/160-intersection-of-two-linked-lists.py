# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        arr={}
        x=headA
        y=headB
        while x:
            arr[x]=True
            x=x.next
        while y:
            try:
                if arr[y]==True:
                    return y
            except:
                pass
            y=y.next
        return None
            