class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        res = 1
        left = 0
        right = maxSum
        while left <= right:
            mid = left + (right - left)//2
            if isValid(mid, index, maxSum, n):
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        return res

def isValid(num, index, maxSum, maxi):
    numbersLeft = index
    numbersRight = maxi - 1 - index
    # num
    num2 = num
    num -= 1
    sumLeft = 0
    sumLeft += num*(num + 1)//2
    if numbersLeft - num  > 0:
        sumLeft += (numbersLeft - num )
    elif numbersLeft - num  < 0:
        new =  num - numbersLeft
        sumLeft -= new*(new + 1)//2
    sumRight = 0
    sumRight += num*(num + 1)//2
    if numbersRight - num  > 0:
        sumRight += (numbersRight - num)
    elif numbersRight - num < 0:
        new = num - numbersRight
        sumRight -= new*(new + 1)//2
    total = sumLeft + sumRight + num2
    return total <= maxSum