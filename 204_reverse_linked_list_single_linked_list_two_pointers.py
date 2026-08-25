class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head):
        pre_pointer = None
        current_pointer = head
        while current_pointer:
            temp_pointer = current_pointer.next
            current_pointer.next = pre_pointer
            pre_pointer = current_pointer
            current_pointer = temp_pointer
        
        return pre_pointer