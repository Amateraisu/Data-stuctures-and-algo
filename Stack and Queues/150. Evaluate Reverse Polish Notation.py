class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # RPN = postfix 
        # ["2","1","+","3","*"]
        # so my intuition tells me that everytime I see an operator, I apply it to the 2 numbers that came before 

        # ["10","6","9","3","+"|,"-11","*","/","*","17","+","5","+"]

        # 10, 6, 12,, -11, 
        stack = []

        for token in tokens:
            if token.isnumeric() or (token[1:].isnumeric() and token[0] == "-"): # if it is not a numerical number, so a 
                stack.append(token)
            else:
                # so I need to evaluate certain expressions here 
                # i'm guaranteed 2 numbers before this current one 
                if len(stack) < 2:
                    return -1
                op2 = stack.pop()
                op1 = stack.pop()
                # print("evaluating",op1 + token + op2 )
                finalResult = eval(op1 + token + op2)
                stack.append(str(int(finalResult)))
        #     print(stack, "looping")
        # print(stack)
        return int(stack[-1])