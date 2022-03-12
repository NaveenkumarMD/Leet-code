# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr=[head]
        while arr[-1].next:
            arr.append(arr[-1].next)
        return arr[len(arr)//2]
        