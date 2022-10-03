class Solution:
    def solve(self, pushes, pops):
        # find the index of the element that is popped first in the push, then reverse iterate to see if it matches 
        # push always 
        if len(pops) > len(pushes):
            return False


        stack = []
        popPtr = 0 
        for index, num in enumerate(pushes):
            stack.append(num)


            while stack and stack[-1] == pops[popPtr]:
                stack.pop()
                popPtr += 1 

        
        while stack and popPtr < len(pops) and stack[-1] == pops[popPtr]:
            stack.pop()
            popPtr += 1 






        return True if popPtr == len(pops) else False