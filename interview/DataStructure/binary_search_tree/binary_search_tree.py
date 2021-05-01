class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

class BST:
    def __init__(self, data):
        self.root = Node(data)
    
    def insert(self, root, data):
        
        if not root:
            return Node(data)

        if data < root.data:
            child = self.insert(root.left, data)
            child.parent = root
            root.left = child
        
        elif data > root.data:
            child = self.insert(root.right, data)
            child.parent = root
            root.right = child
        
        return root 

    def search(self, data):
        """
        Return node equal to 'data'.
        Return None if 'data' is not in BST.
        """

        current_node = self.root

        while True:
            if not current_node:
                return None

            if data == current_node.data:
                return current_node

            if data < current_node.data:
                current_node = current_node.left
            
            elif data > current_node.data:
                current_node = current_node.right
            
    def remove(self, data):
        """
        Remove node except root node.
        """

        delete_node = self.search(data)

        if not delete_node:
            print("{} is not in binary search tree.".format(data))
            return

        my_parent = delete_node.parent

        # There are no children
        if not delete_node.left and not delete_node.right:
            if my_parent.data > delete_node.data:
                my_parent.left = None
            elif my_parent.data < delete_node.data:
                my_parent.right = None

        # There is only left child
        if delete_node.left and not delete_node.right:
            if my_parent.data > delete_node.data:
                my_parent.left = delete_node.left
                delete_node.left.parent = my_parent
            elif my_parent.data < delete_node.data:
                my_parent.right = delete_node.left
                delete_node.left.parent = my_parent

        # There is only right child
        if not delete_node.left and delete_node.right:
            if my_parent.data > delete_node.data:
                my_parent.left = delete_node.right
                delete_node.right.parent = my_parent
            elif my_parent.data < delete_node.data:
                my_parent.right = delete_node.right
                delete_node.right.parent = my_parent
            
        # There are two children
        if delete_node.left and delete_node.right:
            min_node = self.find_min_node(delete_node)
            self.remove(min_node.data)
            delete_node.data = min_node.data
    
    def find_min_node(self, node):
        current_node = node
        while current_node.left:
            current_node = current_node.left
        return current_node
    
    def find_max_node(self, node):
        current_node = node
        while current_node.right:
            current_node = current_node.right
        return current_node

    def inorder(self, node):
        if node.left: self.inorder(node.left)
        print(node.data, end="->")
        if node.right: self.inorder(node.right)
    
    def preorder(self, node):
        print(node.data, end="->")
        if node.left: self.preorder(node.left)
        if node.right: self.preorder(node.right)

    def postorder(self, node):
        if node.left: self.postorder(node.left)
        if node.right: self.postorder(node.right)
        print(node.data, end="->")

    def is_bst(self, node, _min, _max):
        if not node:
            return True
        
        if node.data < _min or node.data > _max:
            return False
        
        return self.is_bst(node.left, _min, node.data)\
            or self.is_bst(node.right, node.data, _max)

    def lca(self, root, x, y):

        # For invalid parameter.
        if not root:
            return None

        if root.data > max(x, y):
            return self.lca(root.left, x, y)
        
        elif root.data < min(x, y):
            return self.lca(root.right, x, y)
        
        return root 


if __name__ == "__main__":
    bst = BST(10)
    ROOT = bst.root
    bst.insert(ROOT, 5)
    bst.insert(ROOT, 13)
    bst.insert(ROOT, 15)
    bst.insert(ROOT, 3)
    bst.insert(ROOT, 7)
    bst.insert(ROOT, 12)
    # bst.remove(13)

    lca_node = bst.lca(bst.root, 5, 13)
    print(lca_node.data)

    # bst.inorder(bst.root)
    # print()
    # bst.preorder(bst.root)
    # print()
    # bst.postorder(bst.root)
    # print()