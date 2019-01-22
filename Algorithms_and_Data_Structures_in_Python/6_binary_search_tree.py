class Node:
    """Define a node class in binary tree"""

    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


class BinarySearchTree:
    """Define a binary search tree"""

    def __init__(self):
        self.root = None

    # Olog(n) if the tree is balanced
    def insertNode(self, newdata, node):
        if newdata < node.data:
            if node.leftChild:
                # insert recursively until the leaf node
                self.insertNode(newdata, node.leftChild)
            else:
                # search until find the leaf node for insertion
                node.leftChild = Node(newdata)
        else:
            if node.rightChild:
                self.insertNode(newdata, node.rightChild)
            else:
                node.rightChild = Node(newdata)

    def insert(self, data):
        # insert a data to binary tree
        if self.root is None:
            self.root = Node(data)
        else:
            self.insertNode(data, self.root)

    def getMinValue(self):
        # the last node at left side
        currentNode = self.root
        while currentNode.leftChild:
            currentNode = currentNode.leftChild
        minValue = currentNode.data
        return minValue

    def getMaxValue(self):
        # the last node at right side
        currentNode = self.root
        while currentNode.rightChild:
            currentNode = currentNode.rightChild
        maxValue = currentNode.data
        return maxValue

    def traverse(self):
        if self.root:
            self.traverseInOrder(self.root)

    def traverseInOrder(self, node):
        if node.leftChild:
            self.traverseInOrder(node.leftChild)
        print(node.data)
        if node.rightChild:
            self.traverseInOrder(node.rightChild)

    def predecessor(self, node):
        # find the predecessor of a node -> a right leaf node of its subtree
        # -> max value of its subtree
        if node.leftChild:
            # traverse all the right nodes
            currentNode = node.leftChild
            while currentNode.rightChild:
                currentNode = currentNode.rightChild
            return currentNode
        else:
            return None

    def remove(self, data):
        if self.root:
            self.removeNode(data, self.root, None)

    # Olog(n)
    def removeNode(self, data, node, previousNode):
        # search the node and remove recursively
        while data != node.data:
            previousNode = node
            if data < node.data:
                node = node.leftChild
            else:
                node = node.rightChild
        targetNode = node
        # find the target value
        # 1) remove a leaf node
        if targetNode.leftChild is None and targetNode.rightChild is None:
            # (equal to not node.leftChild and not node.rightChild)
            if previousNode.leftChild == targetNode:
                print("removing a left leaf node...")
                previousNode.leftChild = None
            else:
                print("removing a right leaf node...")
                previousNode.rightChild = None
            del targetNode
        # 2) remove a node with only left/right child
        elif targetNode.leftChild and targetNode.rightChild is None:
            print("removing a node with only left child")
            previousNode.leftChild = targetNode.leftChild
            del targetNode

        elif targetNode.rightChild and targetNode.leftChild is None:
            print("removing a node with only right child")
            previousNode.rightChild = targetNode.rightChild
            del targetNode
        # 3) remove a node with both left and right
        else:
            print("removing a node with both left and right child!!!")
            # traverse all the right nodes
            predecessorNode = targetNode.leftChild
            print("predecessor of target node: ", predecessorNode.data)
            while predecessorNode.rightChild:
                predecessorNode = predecessorNode.rightChild
            # predecessorNode = self.predecessor(targetNode)
            # swap values
            targetNode.data = predecessorNode.data
            predecessorNode.data = data
            # remove the swapped node, either a left leaf node or node with
            # only 1 child
            previousNode = targetNode
            self.removeNode(data, targetNode.leftChild, previousNode)


if __name__ == '__main__':
    binarytree = BinarySearchTree()
    binarytree.insert(10)
    binarytree.insert(1)
    binarytree.insert(99)
    binarytree.insert(0)
    binarytree.insert(1.5)
    binarytree.insert(101)

    print("min: ", binarytree.getMinValue())
    print("max: ", binarytree.getMaxValue())

    binarytree.traverse()
    print("predecessor of root node: ",
          binarytree.predecessor(binarytree.root).data)

    binarytree.remove(1)
    binarytree.traverse()
    # binarytree.removeNode(10)
    print("min: ", binarytree.getMinValue())
    print("max: ", binarytree.getMaxValue())
