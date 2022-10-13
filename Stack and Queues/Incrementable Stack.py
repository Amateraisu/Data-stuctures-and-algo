from collections import defaultdict

class IncrementableStack:
    def __init__(self):
        self.hashmap = defaultdict(int)
        self.stack = []


    def append(self, val):
        self.stack.append(val)

        

    def pop(self):
        # am I currently sitting on any increments? 
        # print(self.stack, print(self.hashmap))
        currentIndex = len(self.stack) - 1 
        # check if im on current any increments or not 
        res = self.stack.pop() + self.hashmap[currentIndex]
        # add to the previous 
        self.hashmap[currentIndex - 1] += self.hashmap[currentIndex]
        self.hashmap[currentIndex] = 0 


 
        return res



        

    def increment(self, inc, count):
        # 
        index = count - 1 
        validIndex = min(index, len(self.stack) - 1)
        self.hashmap[validIndex] += inc 