class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:

        n = len(arr1)
        arr2.sort()
        @cache
        def dfs(i, prev):
            if i == n:
                return 0
            best = float('inf') # now is the maximum
            if arr1[i] > prev: # if the currentNumber is greater than the prev
                # I can choose to find a number that is smaller than this number in arr2 and replace it
                best = min(best, dfs(i + 1, arr1[i]))
            # if the currentNumber is lesser than or equals to the previous number,
            c = bisect.bisect_right(arr2, prev)
            if c != len(arr2):
                best = min(best, 1 + dfs(i + 1, arr2[c]))
            return best

        res = dfs(0, -1)
        if res != float('inf'):
            return res

        return -1