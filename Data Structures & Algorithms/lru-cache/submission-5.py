class Node:
    def __init__(self, key, val,cap):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keystore = {}

        self.left = Node(0,0)
        self.right = Node(0,0)

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        self.next = prev


    def insert(self , node):
        prev = self.right.prev
        nxt = self.right
        
        prev.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = prev

    def get(self, key: int) -> int:
        if key in self.keystore:
            self.remove(self.keystore[key])
            self.insert(self.keystore[key]) # updating as most recent key used
            return self.keystore[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.keystore:
            self.remove(self.keystore[key])
        self.keystore[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.keystore) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.keystore[lru.key]

