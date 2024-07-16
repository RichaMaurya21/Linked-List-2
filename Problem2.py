## Problem2 (https://leetcode.com/problems/reorder-list/)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next    

        second = slow.next
        prev = slow.next = None
        #reverse second half
        while second:
            nextNode = second.next
            second.next = prev
            prev = second
            second = nextNode

        first, second = head, prev
        #merge both
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2



           