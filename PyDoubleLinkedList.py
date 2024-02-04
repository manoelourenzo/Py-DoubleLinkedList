class Node:
    def __init__(self, item):
        """
        Constructor for Node class.

        Args:
            item: The value to be stored in the node.
        """
        self.item = item
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        """
        Constructor for DoubleLinkedList class.
        Initializes an empty doubly linked list.
        """
        self.begin = None
        self.end = None
        self.size = 0

    def isEmpty(self):
        """
        Checks if the doubly linked list is empty.

        Returns:
            True if the doubly linked list is empty, False otherwise.
        """
        return self.size == 0

    def addFirst(self, item):
        """
        Adds a new node with the given item at the beginning of the doubly linked list.

        Args:
            item: The value to be added to the list.
        """
        newNode = Node(item)
        if self.isEmpty():
            self.begin = self.end = newNode
        else:
            self.begin.prev = newNode
            newNode.next = self.begin
            newNode.prev = None
            self.begin = newNode
        self.size += 1

    def addLast(self, item):
        """
        Adds a new node with the given item at the end of the doubly linked list.

        Args:
            item: The value to be added to the list.
        """
        newNode = Node(item)
        if self.isEmpty():
            self.begin = self.end = newNode
        else:
            self.end.next = newNode
            newNode.prev = self.end
            self.end = newNode
        self.size += 1

    def removeNode(self, item):
        """
        Removes the first occurrence of the node with the given item from the doubly linked list.

        Args:
            item: The value to be removed from the list.
        """
        currentNode = self.begin
        while currentNode:
            if currentNode.item == item:
                if currentNode.prev:
                    currentNode.prev.next = currentNode.next
                else:
                    self.begin = currentNode.next

                if currentNode.next:
                    currentNode.next.prev = currentNode.prev
                else:
                    self.end = currentNode.prev
                break
            currentNode = currentNode.next
        self.size -= 1
        return True

    def showList(self):
        """
        Displays the items in the doubly linked list.
        """
        print("DOUBLE LINKED LIST")
        print(f"SIZE: {self.size}")
        print("None", end=" <-> ")
        currentNode = self.begin
        while currentNode:
            print(f"[{currentNode.item}]", end=" <-> ")
            currentNode = currentNode.next
        print("None")

    def search(self, item):
        """
        Searches for the first occurrence of the given item in the doubly linked list.

        Args:
            item: The value to be searched in the list.
        """
        currentNode = self.begin
        position = 0
        while currentNode:
            if currentNode.item == item:
                return print(f"Item {item} is in position {position}")
            position += 1
            currentNode = currentNode.next

        return print(f"Item {item} isn't in the list")

    def clear(self):
        """
        Deletes all nodes from the doubly linked list.
        """
        currentNode = self.begin
        while currentNode:
            nextNode = currentNode.next
            self.removeNode(currentNode.item)  # Remove the node from memory
            currentNode = nextNode

        self.begin = None
        self.end = None
        self.size = 0
