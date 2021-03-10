class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class MyQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.cnt = 0

    def my_push(self, data):
        new_data = Node(data)
        if self.cnt == 0:
            self.head = new_data
        elif self.cnt == 1:
            self.tail = new_data
            self.tail.prev = self.head
            self.head.next = self.tail
        else:
            self.tail.next = new_data
            new_data.prev = self.tail
            self.tail = new_data
        self.cnt += 1
        return
    
    def my_head(self):
        return None if self.cnt == 0 else str(self.head)
    
    def my_tail(self):
        return None if self.cnt == 0 else str(self.tail)

    def my_pop(self):
        if self.cnt == 0:
            return None

        node = self.head
        if self.cnt == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            
        self.cnt -= 1
        value = node.data ; del node
        return value


if __name__=="__main__":
    my_queue = MyQueue()
    my_queue.my_push(1)
    print(my_queue.my_head())
    print(my_queue.my_tail())
    print("============================")

    my_queue.my_push(2)
    print(my_queue.my_head())
    print(my_queue.my_tail())
    print("============================")

    my_queue.my_push(4)
    print(my_queue.my_head())
    print(my_queue.my_tail())
    print("============================")

    print(my_queue.my_pop())
    print(my_queue.my_head())
    print(my_queue.my_tail())
    print("============================")

    print(my_queue.my_pop())
    print(my_queue.my_head())
    print(my_queue.my_tail())
    print("============================")

    print(my_queue.my_pop())
    print(my_queue.my_head())
    print(my_queue.my_tail())
    print("============================")


    print(my_queue.my_pop())
