## Problem4  (https://leetcode.com/problems/intersection-of-two-linked-lists/)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA, lenB = 0, 0
        currA, currB = headA, headB
        
        while currA:
            currA = currA.next
            lenA += 1
            
        while currB:
            currB = currB.next
            lenB += 1

        p1 = headA
        p2 = headB
        while lenA > lenB:
            p1 = p1.next
            lenA -= 1

        while lenB > lenA:
            p2 = p2.next
            lenB -= 1 

        while p1 and p2:
            if p1 == p2:
                return p1
            else:
                p1 = p1.next
                p2 = p2.next

        return None

    