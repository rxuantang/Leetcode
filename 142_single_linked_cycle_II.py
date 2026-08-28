class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def detectCycle(self, head):
        fast_pointer = head
        slow_pointer = head

        while fast_pointer and fast_pointer.next:
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next

            if slow_pointer == fast_pointer:
                slow_pointer = head
                while slow_pointer != fast_pointer:
                    slow_pointer = slow_pointer.next
                    fast_pointer = fast_pointer.next

                return slow_pointer
        
        return None

if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    common = ListNode(2, ListNode(0, ListNode(-4)))
    common.next.next.next = common  # Create a cycle
    head = ListNode(3, common)
    assert solution.detectCycle(head) == common

    # Test case 2
    common = ListNode(1)
    common.next = common  # Create a cycle
    head = ListNode(1, common)
    assert solution.detectCycle(head) == common

    # Test case 3
    head = ListNode(1)
    assert solution.detectCycle(head) == None

    print("passed all test cases!")

        