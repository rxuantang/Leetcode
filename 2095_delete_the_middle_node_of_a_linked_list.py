# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head):
        dummy_head = ListNode(next=head)
        count1 = 0
        while head:
            count1 += 1
            head = head.next
        index = count1 // 2

        current = dummy_head
        count2 = 0
        while current.next:
            if count2 == index:
                current.next = current.next.next
            else:
                current = current.next
            count2 += 1

        return dummy_head.next

if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    head = ListNode(1, ListNode(3, ListNode(4, ListNode(7, ListNode(1, ListNode(2))))))
    new_head = solution.deleteMiddle(head)
    assert new_head.val == 1
    assert new_head.next.val == 3
    assert new_head.next.next.val == 4
    assert new_head.next.next.next.val == 1
    assert new_head.next.next.next.next.val == 2
    assert new_head.next.next.next.next.next is None

    # Test case 2
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    new_head = solution.deleteMiddle(head)
    assert new_head.val == 1
    assert new_head.next.val == 2
    assert new_head.next.next.val == 4
    assert new_head.next.next.next is None

    # Test case 3
    head = ListNode(2, ListNode(1))
    new_head = solution.deleteMiddle(head)
    assert new_head.val == 2
    assert new_head.next is None

    print("passed all test cases!")
        
        
        
