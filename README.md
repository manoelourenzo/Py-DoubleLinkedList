Double Linked List Implementation in Python
Overview
This repository contains a Python implementation of a doubly linked list. A doubly linked list is a data structure that consists of a sequence of elements, where each element points to both the next and the previous elements in the sequence.

The implementation includes a Node class representing the individual nodes in the doubly linked list and a DoubleLinkedList class that provides various operations on the list.

Classes
1. Node Class
The Node class represents a node in the doubly linked list.

Methods:
__init__(self, item): Initializes a new node with the given value.
2. DoubleLinkedList Class
The DoubleLinkedList class represents the doubly linked list.

Methods:
__init__(self): Initializes an empty doubly linked list.

isEmpty(self): Checks if the doubly linked list is empty.

addFirst(self, item): Adds a new node with the given item at the beginning of the list.

addLast(self, item): Adds a new node with the given item at the end of the list.

removeNode(self, item): Removes the first occurrence of the node with the given item from the list.

showList(self): Displays the items in the doubly linked list.

search(self, item): Searches for the first occurrence of the given item in the list.

clear(self): Deletes all nodes from the list.

Usage
To use the doubly linked list, create an instance of the DoubleLinkedList class and perform operations like adding elements, removing nodes, and displaying the list.

Example:

python
Copy code
# Create a new doubly linked list
linked_list = DoubleLinkedList()

# Add elements
linked_list.addFirst(5)
linked_list.addLast(10)
linked_list.addFirst(2)

# Display the list
linked_list.showList()
Contributing
Contributions are welcome! If you have suggestions, improvements, or bug fixes, please feel free to open an issue or submit a pull request.

License
This project is licensed under the MIT License.

Feel free to customize the README based on your specific project details and preferences. Ensure that you have a LICENSE file in your repository, and replace [MIT License] with the actual license you choose for your project.
