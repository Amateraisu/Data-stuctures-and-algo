class LRUCache:

    def __init__(self, capacity: int):
        self.count = 0
        self.map = {}  # maps key to nodes
        self.most = Node()
        self.least = Node()
        self.least.prev = self.most
        self.most.next = self.least
        self.cap = capacity

    def get(self, key: int) -> int:
        res = -1
        if key in self.map:
            res = self.map[key].val
            n = self.removeNode(self.map[key])
            self.makeRecent(n)
        ptr = self.least

        return res

    def put(self, key: int, value: int) -> None:

        if key in self.map:  # we dont need to worry about the count
            self.map[key].val = value
            # break off from both sides here
            node = self.removeNode(self.map[key])
            # print(key, value, node.val, "put function1")
            self.makeRecent(node)
        else:
            self.count += 1
            node = Node(value)
            # print(key, value, node.val, "put function2")
            node.key = key
            self.makeRecent(node)
            self.map[key] = node

        if self.count > self.cap:
            # evict the one the self.least is pointing to
            node = self.removeNode(self.least.prev)
            self.count -= 1
            self.map.pop(node.key)
        ptr = self.least
        # while ptr:
        #     print(ptr.val, ptr.key, "test")
        #     ptr = ptr.prev
        # print("========")
        return None

    def makeRecent(self, node):
        node.next = self.most.next
        node.prev = self.most
        self.most.next = node
        node.next.prev = node
        return

    def removeNode(self, node):
        # print(self.map)
        # print("to be removed", node.val)
        node.prev.next, node.next.prev = node.next, node.prev

        return node
