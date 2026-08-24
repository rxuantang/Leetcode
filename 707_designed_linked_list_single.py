class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.dummy_head = ListNode()
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size or index < 0:
            return -1
        else:
            current = self.dummy_head.next
            for i in range(index):
                current = current.next
            
            return current.val

    def addAtHead(self, val: int) -> None:
        self.dummy_head.next = ListNode(val,self.dummy_head.next)
        self.size += 1
        

    def addAtTail(self, val: int) -> None:
        current = self.dummy_head
        while current.next:
            current = current.next
        current.next = ListNode(val)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size or index < 0:
            return 
        else:
            current = self.dummy_head
            for i in range(index):
                current = current.next
            current.next = ListNode(val,current.next)
            self.size += 1
        
    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size or index < 0:
            return 
        else:
            current = self.dummy_head
            for i in range(index):
                current = current.next
            current.next = current.next.next
            self.size -= 1

if __name__ == "__main__":
    linked_list = MyLinkedList()
    linked_list.addAtHead(1)
    linked_list.addAtTail(3)
    linked_list.addAtIndex(1, 2)  # linked list becomes 1->2->3
    assert linked_list.get(1) == 2  # returns 2
    linked_list.deleteAtIndex(1)  # now the linked list is 1->3
    assert linked_list.get(1) == 3  # returns 3
    print("passed all test cases!")