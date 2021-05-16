# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        start = ListNode()
        result = start
        carry = 0
        while l1 or l2 or carry: 
            summed = carry
            if l1: summed += l1.val 
            if l2: summed += l2.val 
                
            carry = int(summed / 10)
            res = summed % 10
            result.next = ListNode(res)
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            result = result.next
            
        return start.next
