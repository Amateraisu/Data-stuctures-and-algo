class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:

        res = [0] * n
        stack = [] # contains [lastTimeExecuted, id, method]
        for log in logs:
            id, method, end = log.split(":")
            id = int(id)
            end = int(end)
            print(id, method, end, res, stack)
        
            if method == "start":
                # add the current time executed, and then add to the top of the stack for the current method 
                if stack:
                    res[stack[-1][1]] += end - stack[-1][0]
                stack.append([end, id, method])
            else:
                # if it is an end'
                res[id] += end - stack[-1][0] + 1
                stack.pop()
                if stack:
                    stack[-1][0] = end + 1

        return res