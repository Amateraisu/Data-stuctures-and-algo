class Solution:
    def fib(self, n: int) -> int:
        # memoiz = {}
        # memoiz[0] = 0
        # memoiz[1] = 1
        if n == 0:
            return 0
        if n == 1:
            return 1
        dp = [0 for num in range(n+1)]
        dp[0] = 0
        dp[1] = 1
        for index in range(2,n+1):
            dp[index] = dp[index-1] + dp[index-2]
            
        return dp[-1]
    
    
    
# memoization shaves down the time complexity to O(n)
# def fibonacci(n, memoiz):
#     if n in memoiz:
#         return memoiz[n]
#     number = fibonacci(n-1, memoiz) + fibonacci(n-2, memoiz)
#     memoiz[n] = number
#     return number


#time complexity of 2**n 
# def fibonacci(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fibonacci(n-1) + fibonacci(n-2)