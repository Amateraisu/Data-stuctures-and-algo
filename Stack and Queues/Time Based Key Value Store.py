from collections import defaultdict
from collections import deque


class TimeMap:

    def __init__(self):
        # for every key, initialize a maxHeap 
        # 
        self.dictionary = defaultdict(deque)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dictionary[key].append([timestamp, value])
        
        
        

    def get(self, key: str, timestamp: int) -> str:
        if len(self.dictionary[key]) == 0:
            return ""
        
        if timestamp < self.dictionary[key][0][0]:
            return ""
        
        if len(self.dictionary[key]) == 1:
            return self.dictionary[key][0][1]
        
        while len(self.dictionary[key]) > 1 and timestamp >= self.dictionary[key][1][0]:
            self.dictionary[key].popleft()
        return self.dictionary[key][0][1]
    

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)