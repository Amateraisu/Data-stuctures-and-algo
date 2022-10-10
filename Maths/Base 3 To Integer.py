class Solution:
    def solve(self, s):
        res = 0
        power = -1
        for i in range(len(s) - 1, -1, -1):
            power += 1 
            currentChar = s[i]
            if currentChar != "0":
                res += 3**power * int(currentChar)

        return res