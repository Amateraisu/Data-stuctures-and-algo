class Solution:
    def minimizeResult(self, expression: str) -> str:
        # have a defualt test case first 
        n = len(expression)
        result = '(' + expression + ')'
        plusIndex = expression.index('+')
        currentMin = sum(map(int, expression.split("+")))
        
        #search all possible sub expressions 
        
        for i in range(plusIndex):
            for j in range(plusIndex+2, n+1):
                e1 = expression[0:i] #before the expression 
                e2 = expression[i:j] # the expression itself
                e3 = expression[j:n] # the expression after
                
                value = sum(map(int, e2.split('+')))
                
                #calculate current total 
                if e1 == "" and e3 !="":
                    current = value * int(e3)
                elif e1 != "" and e3 =="":
                    current = value * int(e1)
                elif e1 == "" and e3 == "":
                    current = value
                else:
                    current = value * int(e1) * int(e3)
                    
                if current < currentMin:
                    currentMin = current
                    result = e1 + "(" + e2 + ")" + e3
                    
        return result