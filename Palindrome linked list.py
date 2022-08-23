# TC: O(n) 
# SC: O(n)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from copy import deepcopy
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        length = self.length(head)
        if length %2 == 0:
            mid = self.FindMid(head)
            temp = mid.next
            mid.next = None
        
        else:
            mid = self.FindMid(head)
            temp2 = mid.next
            temp = deepcopy(mid)
            mid.next = None
            temp.next = temp2
            
        LL2 = self.reverse(temp)
        
        while LL2 != None:
            if LL2.val != head.val:
                return False
            else:
                LL2 = LL2.next
                head = head.next
                
        return True
                
    
    def FindMid(self, head):
        
        slow = head
        fast = head
        
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
        
        return slow
    
    def length(self, head):
        
        count = 0
        p1 = head
        
        while p1 != None:
            p1 = p1.next
            count+= 1
            
        return count
    
    def reverse(self, head):
        prev = None
        curr = head
        
        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        return prev