# O(n) time complexity
# First pointer is to the head, if next node exists/!=0 point it to the Node
# Last items next pointer is Null/None

class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

if __name__ == '__main__':
    linkedList = LinkedList()

    linkedList.head = Node(1)
    secondNode = Node(2)
    thirdNode = Node(3)

    linkedList.head.next = secondNode
    secondNode.next = thirdNode

    while linkedList.head != None:
        print(linkedList.head.item)
        linkedList.head = linkedList.head.next