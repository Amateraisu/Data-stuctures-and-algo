class Solution:
    def calPoints(self, ops: List[str]) -> int:
        scores = []
        
        for operation in ops:
            print(operation)
            if operation[0] == "-" or operation.isdigit():
                scores.append(int(operation))
            else:
                if operation == "C":
                    scores.pop()
                elif operation == "D":
                    scores.append((int(scores[-1]) * 2))
                elif operation == "+":
                    scores.append((int(scores[-1]) + int(scores[-2])))
            print(scores)
                    
      
        return sum(scores)