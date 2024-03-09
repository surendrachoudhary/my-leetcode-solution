class Node:
    def __init__(self, key, val):
        """
        Initialize a new node with key and value.

        Args:
            key: Key of the node.
            val: Value associated with the key.
        """
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        """
        Initialize the LRUCache with the specified capacity.

        Args:
            capacity: Maximum capacity of the cache.
        """
        self.cap = capacity
        self.cache = {}  # Map key to node

        # Initialize dummy head and tail nodes
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        """
        Remove the given node from the linked list.

        Args:
            node: Node to be removed.
        """
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        """
        Insert the given node at the right end of the linked list.

        Args:
            node: Node to be inserted.
        """
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        """
        Retrieve the value associated with the given key from the cache.

        Args:
            key: Key to search in the cache.

        Returns:
            Value associated with the key if found, otherwise -1.
        """
        if key in self.cache:
            # Move accessed node to the right end of the list (most recently used)
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        """
        Add or update the key-value pair in the cache.

        Args:
            key: Key of the entry.
            value: Value associated with the key.
        """
        if key in self.cache:
            # If key exists, remove it and update the value
            self.remove(self.cache[key])
        else:
            if len(self.cache) >= self.cap:
                # If capacity is reached, evict the least recently used node (from the left end)
                lru = self.left.next
                self.remove(lru)
                del self.cache[lru.key]

        # Insert the new node at the right end of the list
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
