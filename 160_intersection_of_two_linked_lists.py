class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getLength(self,head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length
    
    def moveForward(self,head,length):
        while length > 0:
            head = head.next
            length -= 1
        return head

    def getIntersectionNode(self, headA, headB):
        lengthA = self.getLength(headA)
        lengthB = self.getLength(headB)

        if lengthA >= lengthB:
            headA = self.moveForward(headA,lengthA-lengthB)
        else: 
            headB = self.moveForward(headB,lengthB-lengthA)

        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        
        return None

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

        