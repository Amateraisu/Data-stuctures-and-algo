class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        for n in range(0,num+1):
            strN = str(n)		### convert int to string
            strR = strN[::-1]	### reverse the digits
            ### make sure to convert the string back to int.
            if int(strN)+int(strR)==num:
                return True
        return False