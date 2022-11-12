from collections import deque 

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = deque()

        queue.append([["0", "0", "0", "0"], 0])
        turns = 0 
        deadends = set(deadends)
        visited = set()
        while queue:
            currentNode, cost = queue.popleft()
            # print(currentNode, cost)
            tuplified = tuple(currentNode)
            if tuplified in visited:
                continue 
            currentString = "".join(currentNode)
            if currentString == target:
                return cost 
            if currentString in deadends:
                continue 

                
            visited.add(tuple(currentNode))
            for index, char in enumerate(currentNode):
                newChar = getNextChar(char)
                newChar2 = getPrevChar(char)
                tempCopy = currentNode[:]
                tempCopy2 = currentNode[:]
                tempCopy[index] = newChar 
                tempCopy2[index] = newChar2
                queue.append([tempCopy, cost + 1])
                queue.append([tempCopy2, cost + 1])
                

            
        return -1
                
                
def getPrevChar(currentChar):
    current = int(currentChar)
    current -= 1 
    if current < 0:
        current = 9 
    return str(current)
        
def getNextChar(currentChar):
    current = int(currentChar)
    current += 1 
    if current == 10:
        current = 0 
    return str(current)