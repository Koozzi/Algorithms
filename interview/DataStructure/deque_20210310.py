class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class MyDeque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.cnt = 0

    def my_head(self):
        return self.head.data if self.cnt > 0 else None
    
    def my_tail(self):
        return self.tail.data if self.cnt > 0 else None

    def my_popleft(self):
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
    
    def my_pushleft(self, data):
        new_data = Node(data)
        if self.cnt == 0:
            self.head = new_data
            self.tail = new_data
        else:
            self.head.prev = new_data
            new_data.next = self.head
            self.head = new_data
        self.cnt += 1
            
    def my_pop(self):
        if self.cnt == 0:
            return None

        node = self.tail
        if self.cnt == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.cnt -= 1
        value = node.data ; del node
        return value
    
    def my_push(self, data):
        new_data = Node(data)
        if self.cnt == 0:
            self.head = new_data
            self.tail = new_data
        else:
            self.tail.next = new_data
            new_data.prev = self.tail
            self.tail = new_data
        self.cnt += 1
        return

if __name__=="__main__":
    my_deque = MyDeque()
    print("Head : ", my_deque.my_head())
    print("Tail : ", my_deque.my_tail())

    my_deque.my_push(0)
    print("Head : ", my_deque.my_head())
    print("Tail : ", my_deque.my_tail())

    my_deque.my_push(1)
    print("Head : ", my_deque.my_head())
    print("Tail : ", my_deque.my_tail())
    
    my_deque.my_push(2)
    print("Head : ", my_deque.my_head())
    print("Tail : ", my_deque.my_tail())

    my_deque.my_pushleft(100)
    print("Head : ", my_deque.my_head())
    print("Tail : ", my_deque.my_tail())

    my_deque.my_popleft()
    print("Head : ", my_deque.my_head())
    print("Tail : ", my_deque.my_tail())
