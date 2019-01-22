# single linked list class
class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):

    def __init__(self):
        # initialize the root node which contains nothing
        self.head = None
        self.size = 0

    @property
    def size2(self):
        current_node = self.head
        size = 0
        while current_node is not None:
            size += 1
            current_node = current_node.next
        return size

    # O(1) constant complexity
    def insertStart(self, data):
        # insert element to the beginning
        self.size += 1
        # instantiate the Node class
        newnode = Node(data)

        if self.head is None:
            # set as new start node
            self.head = newnode
        else:
            # insert to the beginning (left side)
            newnode.next = self.head
            self.head = newnode

    # O(N) complexity
    def insertEnd(self, data):
        self.size += 1
        newnode = Node(data)
        search_node = self.head
        while search_node.next is not None:
            search_node = search_node.next
        search_node.next = newnode
        # return search_node

    def traverseList(self):
        current_node = self.head
        # print("head data after insertion: ", current_node.data)
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def remove(self, data):
        # remove a specific data from the linked list
        self.size -= 1
        currentNode = self.head
        previousNode = None
        while currentNode.data != data:
            # store previous node
            previousNode = currentNode
            currentNode = currentNode.next

        if previousNode is None:
            # remove the 1st Node
            self.head = currentNode.next
        else:
            previousNode.next = currentNode.next


if __name__ == '__main__':

    linkedlist = LinkedList()
    linkedlist.insertStart(12)
    linkedlist.insertStart(122)
    linkedlist.insertStart(3)
    linkedlist.insertEnd(31)
    linkedlist.insertEnd(311)
        # print(type(linkedlist.head))
    print("size2: ", linkedlist.size2)

    # newlinkedlist = linkedlist.insertEnd(i)

    linkedlist.traverseList()
    print("size1: ", linkedlist.size)

    linkedlist.remove(31)
    linkedlist.remove(12)
    linkedlist.remove(311)

    linkedlist.traverseList()
    print("size2: ", linkedlist.size2)