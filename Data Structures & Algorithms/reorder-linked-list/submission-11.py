# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        midpoint = slow

        cur = midpoint.next
        midpoint.next = None
        prev = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        head2 = prev
        print("hi")

        while head2:
            h1 = head.next
            h2 = head2.next
            head.next = head2
            head.next.next = h1
            head = h1
            head2 = h2

