# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head, val):

        dummy_head = ListNode(next=head)

        current = dummy_head
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        
        return dummy_head.next


if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    head = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
    val = 6
    new_head = solution.removeElements(head, val)
    result = []
    while new_head:
        result.append(new_head.val)
        new_head = new_head.next
    assert result == [1, 2, 3, 4, 5]

    # Test case 2
    head = None
    val = 1
    new_head = solution.removeElements(head, val)
    assert new_head is None

    # Test case 3
    head = ListNode(7, ListNode(7, ListNode(7)))
    val = 7
    new_head = solution.removeElements(head, val)
    assert new_head is None
    
    print("passed all test cases!")
        
        