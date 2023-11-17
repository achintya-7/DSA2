class Node:
    def __init__(self, val):
     self.val = val
     self.left = None
     self.right = None
     self.height = 0

class AVL:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node == None:
            return -1
        else:
            return node.height

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

        return self.rotate(node)

    def rotate(self, node) -> Node:
        if self.height(node.left) - self.height(node.right) > 1:
            # LEFT HEAVY

            if (self.height(node.left.left) - self.height(node.left.right) > 0):
                # LEFT LEFT
                return self.rotate_right(node)

            if (self.height(node.left.left) - self.height(node.left.right) < 0):
                # LEFT RIGHT
                node.left = self.rotate_left(node.left)
                return self.rotate_right(node)

        if self.height(node.left) - self.height(node.right) < -1:
            # RIGHT HEAVY

            if (self.height(node.right.left) - self.height(node.right.right) < 0):
                # RIGHT RIGHT
                return self.rotate_left(node)

            if (self.height(node.right.left) - self.height(node.right.right) > 0):
                # RIGHT LEFT
                node.right = self.rotate_right(node.right)
                return self.rotate_left(node)

        return node

    def rotate_right(self, p) -> Node:
        c = p.left 
        t = c.right 

        c.right = p
        p.left = t

        # P will always be lower than C in tree, so update P first
        p.height = max(self.height(p.left), self.height(p.right)) + 1
        c.height = max(self.height(c.left), self.height(c.right)) + 1

        return c

    def rotate_left(self, p) -> Node:
        c = p.right
        t = c.left

        c.left = p
        p.right = t

        # P will always be lower than C in tree, so update P first
        p.height = max(self.height(p.left), self.height(p.right)) + 1
        c.height = max(self.height(c.left), self.height(c.right)) + 1

        return c

if __name__ == "__main__":
    avl = AVL()

    for i in range(1, 1000):
        avl.insert(i)

    print(avl.height(avl.root))