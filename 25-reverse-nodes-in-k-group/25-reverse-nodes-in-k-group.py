class Solution:
    def reverseKGroup(self, head, k):
        ptr = ListNode(next=head)
        final = ptr
        end_ptr = ptr

        while True:
            for i in range(k):
                end_ptr = end_ptr.next
                if end_ptr ==  None: break
            if end_ptr == None: break

            resume_ptr = end_ptr.next
            end_ptr.next = None

            self.reverseList(ptr.next)
            ptr.next.next = resume_ptr
            temp = ptr
            ptr = ptr.next
            temp.next = end_ptr
            end_ptr = ptr

        return final.next

    def reverseList(self, head):
        if head == None: return head

        def reverseHelper(node):
            if node.next == None: return node
            new_head = reverseHelper(node.next)
            node.next.next = node
            return new_head

        new_head = reverseHelper(head)
        head.next = None
        return new_head