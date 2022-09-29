# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #1. Find Mid
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        
        #2. Reverse Second Half
        cur=slow
        prev= None
        
        while cur:
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp
        
        # 3. Traverse first hald and second half(Reversed)
        p1=head
        p2=prev
        while p1 and p2:
            # 4. Return False if node values does not match else if traversal completed return True
            if p1.val != p2.val:
                return False
            p1=p1.next
            p2=p2.next
        return True
        