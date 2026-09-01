class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head):
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
                return current.next
            else:
                current = current.next
            count2 += 1

if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    middle_node = solution.middleNode(head)
    assert middle_node.val == 3
    assert middle_node.next.val == 4
    assert middle_node.next.next.val == 5
    assert middle_node.next.next.next is None

    # Test case 2
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
    middle_node = solution.middleNode(head)
    assert middle_node.val == 4
    assert middle_node.next.val == 5
    assert middle_node.next.next.val == 6
    assert middle_node.next.next.next is None

    print("passed all test cases!")