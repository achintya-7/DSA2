class Node:
    def __init__(self, val):
     self.val = val
     self.left = None
     self.right = None
     self.height = 0

class BST:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node == None:
            return -1
        else:
            return node.height

    def isEmpty(self):
        if self.root == None:
            return True
        else:
            return False

    def display(self):
        print("Displaying the tree...")
        self.display_helper(self.root, "Root Node:  ")

    def display_helper(self, node, details):
        if node == None:
            return
        
        print(details + str(node.val) + " Height: " + str(node.height))

        self.display_helper(node.left, f"Left of {node.val}: ")
        self.display_helper(node.right, f"Right of {node.val}: ")

    def insert(self, val):
        self.root = self.insert_helper(self.root, val)

    def insert_helper(self, node, val) -> Node:
        if node == None:
            return Node(val)

        if val < node.val:
            node.left = self.insert_helper(node.left, val)

        if val > node.val:
            node.right = self.insert_helper(node.right, val)

        node.height = max(self.height(node.left), self.height(node.right)) + 1

        return node

    def balanced(self):
        return self.balanced_helper(self.root)

    def balanced_helper(self, node):
        if node == None:
            return True

        if abs(self.height(node.left) - self.height(node.right)) > 1:
            return False

        return self.balanced_helper(node.left) and self.balanced_helper(node.right)

    def populate(self, a):
        for i in a:
            self.insert(i)

    def populate_sorted(self, a):
        self.populate_sorted_helper(a, 0, len(a)-1)

    def populate_sorted_helper(self, a, start, end):
        if start >= end:
            return 
        
        mid = (start + end) // 2

        self.insert(a[mid])
        self.populate_sorted_helper(a, start, mid)
        self.populate_sorted_helper(a, mid+1, end)

if __name__ == "__main__":
    bst = BST()
    a = [2, 1, 5, 4, 3, 6, 7]
    b = [1, 2, 3, 4, 5, 6, 7]
    bst.populate(a)
    bst.display()  
    bst.populate_sorted(b)
    bst.display()  
    





    