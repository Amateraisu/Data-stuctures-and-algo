class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        # It is always better to change a number at the front
        # so find the first number that is bigger at the front
        res = list(num)
        n = len(num)
        start = -1
        for i in range(n):
            if int(num[i]) < change[int(num[i])]:
                start = i
                break
        while start < n and int(res[start]) <= change[int(num[start])]:
            res[start] = str(change[int(num[start])])
            start += 1

        return "".join(res)