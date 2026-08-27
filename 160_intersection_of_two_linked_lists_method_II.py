class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        pointerA = headA
        pointerB = headB

        while pointerA != pointerB:
            pointerA = pointerA.next if pointerA else headB 
            pointerB = pointerB.next if pointerB else headA

        return pointerA

if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    common = ListNode(8, ListNode(4, ListNode(5)))
    l1 = ListNode(4, ListNode(1, common))
    l2 = ListNode(5, ListNode(6, ListNode(1, common)))
    assert solution.getIntersectionNode(l1, l2) == common

    # Test case 2
    l1 = ListNode(2, ListNode(6, ListNode(4)))
    l2 = ListNode(1, ListNode(5))
    assert solution.getIntersectionNode(l1, l2) == None

    print("passed all test cases!")

        