# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        dummy_head = ListNode(val = 0, next=head)
        slow_pointer = dummy_head
        fast_pointer = slow_pointer
        for i in range (n+1):
            fast_pointer = fast_pointer.next
        while fast_pointer:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next

        slow_pointer.next = slow_pointer.next.next

        return dummy_head.next

if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    n = 2
    new_head = solution.removeNthFromEnd(head, n)
    result = []
    while new_head:
        result.append(new_head.val)
        new_head = new_head.next
    assert result == [1, 2, 3, 5]

    # Test case 2
    head = ListNode(1)
    n = 1
    new_head = solution.removeNthFromEnd(head, n)
    assert new_head is None

    # Test case 3
    head = ListNode(1, ListNode(2))
    n = 1
    new_head = solution.removeNthFromEnd(head, n)
    result = []
    while new_head:
        result.append(new_head.val)
        new_head = new_head.next
    assert result == [1]

    print("passed all test cases!")