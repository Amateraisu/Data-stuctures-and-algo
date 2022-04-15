class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        earn1 , earn2 = 0, 0
        earns = Counter(nums)

        numsSorted = sorted(list(set(nums)))

        for i in range(len(numsSorted)):
            currentEarns = earns[numsSorted[i]] * numsSorted[i]
            
            if i > 0 and numsSorted[i] == numsSorted[i-1] + 1:
                temp = earn2
                maximumEarn = max(currentEarns + earn1, earn2)
                earn1 = temp
                earn2 = maximumEarn
            else:
                maximumEarn = max(currentEarns+earn1, earn2 + currentEarns)
                temp = earn1
                earn1 = earn2
                earn2 = maximumEarn
        return earn2