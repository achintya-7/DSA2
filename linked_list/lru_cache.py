class Node(self, key, val):
    self.key = key
    self.val = val
    self.next = None
    self.prev = None 

class LRU(self, key, val):
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        nxt, prv = node.next, node.prev
        
        nxt.prev = prv
        prv.next = nxt

    def add(self, node):
        nxt, prv = self.tail, self.tail.prev

        prv.next = node
        nxt.prev = node

        node.next = nxt 
        node.prev = prv

    def get(self, key: int) -> int: 
        if key in self.cache:
            self.remove(self.cache[key])
            self.add(self.cache[key])
            return self.cache[key].val 
        else: 
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, val)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key]

