from PyDoubleLinkedList import *

def test_add_first():
    value = int(input("Enter the value to add at the beginning: "))
    doubleLinkedList.addFirst(value)
    print("Added at the beginning.")

def test_add_last():
    value = int(input("Enter the value to add at the end: "))
    doubleLinkedList.addLast(value)
    print("Added at the end.")

def test_remove_node():
    value = int(input("Enter the value to remove: "))
    doubleLinkedList.removeNode(value)
    print(f"Removed the first occurrence of {value}.")

def test_show_list():
    print("Current linked list:")
    doubleLinkedList.showList()

def test_search():
    value = int(input("Enter the value to search: "))
    result = doubleLinkedList.search(value)
    print(result)

def test_clear():
    doubleLinkedList.clear()
    print("Linked list cleared.")

if __name__ == "__main__":
    doubleLinkedList = DoubleLinkedList()

    while True:
        doubleLinkedList.showList()
        print("\nChoose an option:")
        print("1. Add to the beginning")
        print("2. Add to the end")
        print("3. Remove node")
        print("4. Show list")
        print("5. Search")
        print("6. Clear list")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            test_add_first()
        elif choice == "2":
            test_add_last()
        elif choice == "3":
            test_remove_node()
        elif choice == "4":
            test_show_list()
        elif choice == "5":
            test_search()
        elif choice == "6":
            test_clear()
        elif choice == "7":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")
