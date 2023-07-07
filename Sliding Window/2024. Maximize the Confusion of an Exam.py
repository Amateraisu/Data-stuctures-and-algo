class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        # maximum number of consecutive after replacing K
        # for any window, take the minimum one and replace it with K
        a = 0
        b = 0
        l = 0
        res = 0
        n = len(answerKey)
        for r in range(n):
            if answerKey[r] == 'T':
                a+= 1
            else:
                b+= 1
            # print(r, a, b, "first")
            while min(a, b) > k and l <= r:
                if answerKey[l] == 'T':
                    a -= 1
                else:
                    b -= 1
                l += 1
            res = max(res, a + b)
            # print(r, a, b)
        return res
