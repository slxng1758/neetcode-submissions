# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        start = ListNode()
        head = start
        carry = 0
        ones = 0
        while l1 or l2 or carry!=0:
            l1v = 0
            l2v = 0
            if l1:
                l1v = l1.val
                l1 = l1.next
            if l2:
                l2v = l2.val
                l2 = l2.next
            summ = l1v + l2v + carry
            carry = summ//10
            ones = summ % 10
            start.next = ListNode(ones)
            start = start.next
        start.next = l1 or l2
        return head.next
        