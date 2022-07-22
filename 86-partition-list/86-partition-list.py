# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummyS, dummyG  = ListNode(), ListNode()
        prevS, prevG = dummyS, dummyG
        curr = head
        while curr:
            if curr.val < x:
                prevS.next, prevS = curr, curr
            else:
                prevG.next, prevG= curr, curr
            curr.next, curr = None, curr.next
        prevS.next = dummyG.next
        return dummyS.next