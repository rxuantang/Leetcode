class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head):
        return self.reverse(head,None)
    
    def reverse(self, current_pointer, pre_pointer):
        if current_pointer == None:
            return pre_pointer
        
        temp_pointer = current_pointer.next
        current_pointer.next = pre_pointer
        
        return self.reverse(temp_pointer,current_pointer)

if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    new_head = solution.reverseList(head)
    result = []
    while new_head:
        result.append(new_head.val)
        new_head = new_head.next
    assert result == [5, 4, 3, 2, 1]

    # Test case 2
    head = None
    new_head = solution.reverseList(head)
    assert new_head is None

    # Test case 3
    head = ListNode(1)
    new_head = solution.reverseList(head)
    assert new_head.val == 1 and new_head.next is None

    print("passed all test cases!")