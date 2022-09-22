from collections import deque
from collections import defaultdict

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # 0 -> circular 
        # 1 -> square 
        queue1 = deque(students)
        queue2 = deque(sandwiches)
        dict1 = defaultdict(int)
        dict2 = defaultdict(int)
        
        createDict(dict1, students)
        createDict(dict2, sandwiches)
        
        while queue1:
            currentStudent = queue1[0]
            currentSandwich = queue2[0]
            # check if I have enough units  to remove 
            if dict1[currentSandwich] == 0:
                return len(queue1)
            
            if currentStudent != currentSandwich:
                queue1.append(queue1.popleft())
            else:
                dict1[currentSandwich] -= 1 
                queue1.popleft()
                queue2.popleft()
                
        return 0
    
def createDict(dictionary, array):
    for num in array:
        dictionary[num] += 1 