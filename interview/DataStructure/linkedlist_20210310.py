class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
    
    def __str__(self):
        return str(self.data)

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.cnt = 0
    
    def __str__(self):
        linkedlist = []
        for i in range(self.cnt):
            linkedlist.append(self.item(i))
        return str(linkedlist)

    def append(self, index, data):
        new_data = Node(data)
        if self.cnt <= index:
            return None
        if self.cnt == 0:
            self.head = new_data
            self.tail = new_data
        else:
            if index == 0:
                self.head.prev = new_data
                new_data.next = self.head
                self.head = new_data
            elif index == -1:
                self.tail.next = new_data
                new_data.prev = self.tail
                self.tail = new_data
            else:
                if index == self.cnt - 1:
                    self.append(-1, data)
                    return
                next_node = self.next_item(index, 1, self.head)
                prev_node = new_data.prev

                prev_node.next = new_data
                new_data.prev = prev_node

                next_node.prev = new_data
                new_data.next = new_data

        self.cnt += 1
    
    def delete(self, index):
        if self.cnt == 0 or index < 0 or index >= self.cnt:
            return None
        if index == 0:
            node = self.head
            if self.cnt == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
                del node
        elif index == self.cnt - 1:
            node = self.tail
            if self.cnt == 1:
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None
                del node
        else:
            node = self.next_item(index, 1, self.head)
            prev_node = node.prev
            next_node = node.next

            prev_node.next = next_node
            next_node.prev = prev_node

            del node

        self.cnt -= 1
    
    def item(self, index):
        if self.cnt == 0 or index < 0 or index >= self.cnt:
            return None
        if index == 0: return self.head.data
        node = self.next_item(index, 1, self.head)
        return node.data

    def next_item(self, index, cnt, prev_node):
        current_node = prev_node.next
        if index == cnt: return current_node
        return self.next_item(index, cnt+1, current_node)

if __name__=="__main__":
    my_linkedlist = MyLinkedList()
    my_linkedlist.append(-1, 0)
    print(my_linkedlist)

    my_linkedlist.append(-1, 1)
    print(my_linkedlist)

    my_linkedlist.append(-1, 2)
    print(my_linkedlist)

    my_linkedlist.delete(0)
    print(my_linkedlist)

    my_linkedlist.append(-1, 6)
    print(my_linkedlist)
    
    my_linkedlist.append(3, 99)
    print(my_linkedlist)

    my_linkedlist.delete(2)
    print(my_linkedlist)