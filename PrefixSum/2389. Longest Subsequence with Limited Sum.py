class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        # the maximum size of a subsequence I can take from nums such that the sum is <= query 
        # sort them -> have a prefix sum -> binary search each query 
        nums.sort()
        prefixSums = [0] * len(nums)
        current = 0 
        for i, num in enumerate(nums):
            current += num
            prefixSums[i] = current

        print(prefixSums)
        res = []
        for query in queries:
            result = binarySearch(prefixSums, query)
            res.append(result) if result != float("-inf") else res.append(0)

        return res 

def binarySearch(prefixSums, query):
    # try to maximize while being smaller than the query
    left = 0 
    right = len(prefixSums) - 1 
    res = float("-inf")
    # 0 3 1 
    # 
    while left <= right:
        mid = left + (right - left)//2
        if prefixSums[mid] <= query:
            res = mid 
            left = mid + 1 
        else:
            right = mid - 1 
    return res + 1