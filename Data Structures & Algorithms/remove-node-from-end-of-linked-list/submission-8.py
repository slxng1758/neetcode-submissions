# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        retstart = head
        start = head
        while head:
            length +=1
            head = head.next
        idx = length - n
        cidx = 0
        if idx ==0:
            return retstart.next
        while cidx<idx-1:
            cidx+=1
            start = start.next
        if start and start.next and start.next.next:
            start.next = start.next.next
        elif start and start.next:
            start.next = None

        return retstart
        

        