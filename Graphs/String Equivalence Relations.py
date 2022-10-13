class Solution:
    def solve(self, a, b, target):

        
        parent = [char for char in ascii_lowercase]

        def find(node):
            # it will end when it is pointing towards itself 
            ptr = node 
            index = ord(ptr) - ord("a")
            while ptr != parent[index]:
                ptr = parent[index]
                index = ord(ptr) - ord("a") 
            
            return index

        for index in range(len(a)):
            node1 = a[index]
            node2 = b[index]
            # find their parent node 
            parent1 = find(node1)
            parent2 = find(node2) # remember we are using the index 
            if parent1 < parent2:
                parent[parent2] = chr(parent1 + ord("a"))
            else:
                parent[parent1] = chr(parent2 + ord("a")) 

        res = []
        for char in target:
            parentIndex = find(char)
            res.append(chr(parentIndex + ord("a")))

        return "".join(res)