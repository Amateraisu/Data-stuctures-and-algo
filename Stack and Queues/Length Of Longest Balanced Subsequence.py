class Solution:
    def solve(self, s):
        stack = []
        res = 0
        for char in s:
            if char == "(":
                stack.append(char)
            else:
                if stack:
                    stack.pop()
                    res += 2 
        return res