class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if start == end:
            return 0
        valids = set()
        for valid in bank:
            valids.add(tuple(valid))
            
        # store all the valid iterations 
        # do this recursively and check if its valid 
        possible_choices = ["A", "C", "G", "T"]
        
        endString = tuple(end)
        # do a dfs and edit all the possible choices and check if its valid or not 

        seen = set()

        # at every iteration always edit the string 
        
        def dfs(currentString):
            currentTuplifyed = tuple(currentString)
            if currentTuplifyed == endString:
                return 0
            if currentTuplifyed in seen:
                return float("inf")
            
            res = float("inf")
            # print("check", indexes_of_concern)
            seen.add(currentTuplifyed)
            for index in range(len(start)):
                # print(index, "index")
                for choice in possible_choices:
                    
                    # try and do a dfs 
                    temp = currentString[index]
                    
                    currentString[index] = choice
                    if tuple(currentString) in valids:
                        
                        res = min(res, dfs(currentString) + 1)
                    # restore it back 
                    currentString[index] = temp 
            return res 
        
        res = dfs(list(start))
        
        return res if res != float("inf") else -1