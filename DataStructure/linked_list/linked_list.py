class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

class LinkedList:
    def __init__(self, item):
        self.head = Node(item)

    def print_linked_list(self):
        """
        Print all elements of linked list.
        """
        cur = self.head

        if cur is None:
            print("Linked list is empty.")
            return

        print("[", end="")
        while cur is not None:
            if cur.next is not None:
                print(cur.data, end=", ")
            else:
                print(cur.data, end="]\n")
            cur = cur.next

    def insert_at_tail(self, item):
        print("Insert {} in linked list.".format(item))
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = Node(item)

        self.print_linked_list()
    
    def search_element(self, item):
        """
        Find the item in linked list.
        Print found message with index if item is in linked list.
        Pinrt not found message if item is not in linked list.
        """
        current_node = self.head
        index = 0
        if current_node.data == item:
            print("{} is in linked list at index {}.".format(item, index))
            return

        while current_node.data != item:
            index += 1
            current_node = current_node.next
            
            if current_node is None:
                print("{} is not in linked list.".format(item))
                return
            
            if current_node.data == item:
                print("{} is in linked list at index {}".format(item, index))
                return
    
    def remove_element(self, item):
        current_node = self.head
        
        if current_node.data == item:
            if current_node.next is None:
                self.head = None
                print("Delete {} in linked list.".format(item))
                self.print_linked_list()
                return
            
            self.head = current_node.next
            print("Delete {} in linked list.".format(item))
            self.print_linked_list()
            return
        
        while True:
            if current_node.next is None:
                print("{} is not in linked list.".format(item))
                return
            
            if current_node.next.data == item:

                delete_item = current_node.next

                if delete_item.next is None:
                    current_node.next = None
                    
                else:
                    current_node.next = delete_item.next

                print("Delete {} in linked list.".format(item))
                self.print_linked_list()
                return

            current_node = current_node.next

if __name__ == "__main__":
    my_linked_list = LinkedList(3)
    my_linked_list.print_linked_list()
    my_linked_list.insert_at_tail(4)
    my_linked_list.insert_at_tail(10)
    my_linked_list.insert_at_tail(6)
    my_linked_list.insert_at_tail(5)
    my_linked_list.insert_at_tail(2)
    my_linked_list.search_element(10)
    my_linked_list.search_element(1111)
    my_linked_list.remove_element(10)
    my_linked_list.remove_element(2)
    my_linked_list.remove_element(3)
