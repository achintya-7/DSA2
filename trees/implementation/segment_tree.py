class Node:
    def __init__(self, si, ei):
        self.data = None
        self.si = si
        self.ei = ei
        self.left = None
        self.right = None

class SegmentTree:
    def __init__(self, arr):
        self.root = self.construct(arr, 0, len(arr) - 1)

    def construct(self, arr, s, e) -> Node:
        if s == e:
            node = Node(s, e)
            node.data = arr[s]
            return node

        node = Node(s, e)
        m = (s + e) // 2

        node.left = self.construct(arr, s, m)
        node.right = self.construct(arr, m + 1, e)

        node.data = node.left.data + node.right.data

        return node

    def query(self, node, qs, qe):
        return self.query_helper(self.root, qs, qe)

    def query_helper(self, node, qs, qe) -> int:
        if node.si >= qs and node.ei <= qe:
            # node is completely inside the query range
            return node.data

        elif node.si > qe or node.ei < qs:
            # node is completely outside the query range
            return 0

        else:
            left = self.query_helper(node.left, qs, qe)
            right = self.query_helper(node.right, qs, qe)
            return left + right

    def update(self, idx, val):
        self.root.data = self.update_helper(self.root, idx, val)

    def update_helper(self, node, idx, val) -> int:
        if idx >= node.si and idx <= node.ei:
            if node.si == node.ei:
                # leaf node reached for the index
                node.data = val
                return val
            else:
                left = self.update_helper(node.left, idx, val)
                right = self.update_helper(node.right, idx, val)
                node.data = left + right
                return node.data

        # if idx is not in the range of the node
        # return the node's data as no change is requireed
        return node.data