class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        print("Enter the value of the root node: ")
        value = input()
        self.root = Node(value)
        self.populate(self.root)

    def populate(self, node):
        print("Do you want to enter left node of " + node.val + "? (y/s)" )
        left = input()
        if left != "n":    
            print("Enter the value of the left node: ")
            value = input()
            node.left = Node(value)
            self.populate(node.left)

        print("Do you want to enter right node of " + node.val + "? (y/s)")
        right = input()
        if right != "n":     
            print("Enter the value of the right node: ")
            value = input()
            node.right = Node(value)
            self.populate(node.right)

    def display(self):
        print("Displaying the tree...")
        self.display_helper(self.root, "")

    def display_helper(self, node, indent):
        if node == None:
            return
            
        print(indent + node.val)
        self.display_helper(node.left, "\t")
        self.display_helper(node.right, "")

    def pretty_print(self):
        print("Pretty printing the tree...")
        self.pretty_print_helper(self.root, 0)

    def pretty_print_helper(self, node, indent):
        if node == None:
            return

        self.pretty_print_helper(node.right, indent+1)
        print("\t"*indent + node.val)
        self.pretty_print_helper(node.left, indent+1) 

if __name__ == "__main__":
    tree = BinaryTree()
    tree.display()

        


