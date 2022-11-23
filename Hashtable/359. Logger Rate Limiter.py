class Logger:

    def __init__(self):
        self.hashmap = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:

        if message not in self.hashmap:

            self.hashmap[message] = timestamp + 10 
                
        else:
            if self.hashmap[message] > timestamp:

                return False 

            self.hashmap[message] = timestamp + 10
        return True 