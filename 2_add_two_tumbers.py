class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy_head = ListNode()
        carry = 0
        current_pointer = dummy_head
        while l1 or l2 or carry:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            sum_val = l1_val + l2_val + carry

            current_pointer.next = ListNode(sum_val % 10)
            carry = sum_val // 10
            
            current_pointer = current_pointer.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy_head.next

if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    result = solution.addTwoNumbers(l1, l2)
    output = []
    while result:
        output.append(result.val)
        result = result.next
    assert output == [7, 0, 8]

    # Test case 2
    l1 = ListNode(0)
    l2 = ListNode(0)
    result = solution.addTwoNumbers(l1, l2)
    output = []
    while result:
        output.append(result.val)
        result = result.next
    assert output == [0]

    # Test case 3
    l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
    l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9)))) 
    result = solution.addTwoNumbers(l1, l2)
    output = []
    while result:
        output.append(result.val)
        result = result.next
    assert output == [8, 9, 9, 9, 0, 0, 0, 1]   

    print("passed all test cases!")