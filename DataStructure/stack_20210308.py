class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None


class MyStack:
    def __init__(self):
        self.head = None
        self.top = 0
    
    def __str__(self):
        
        print_stack = '['
        node = self.head
        while True:
            try:
                print_stack += str(node)
                if node.prev == None:
                    break
                node = node.prev
                print_stack += ', '
            except:
                break
        print_stack += ']'
        return print_stack

    def push(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        new_node.prev = self.head
        self.head = new_node
        self.top += 1
    
    def pop(self):
        node = self.head
        try:
            value = node.data ; del node
            self.top -= 1
            self.head = self.head.prev
        except:
            value = None
        return value

if __name__=="__main__":
    my_stack = MyStack()
    print(my_stack)
    my_stack.push(4)
    print(my_stack)
    my_stack.push(2)
    print(my_stack)
    my_stack.push(1)
    print(my_stack)
    print(my_stack.pop())
    print(my_stack)
    print(my_stack.pop())
    print(my_stack)
    print(my_stack.pop())
    print(my_stack)