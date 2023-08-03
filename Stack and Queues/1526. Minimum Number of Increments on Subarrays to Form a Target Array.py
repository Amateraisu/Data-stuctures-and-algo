class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        # at every increment, we will always increment some subarray
        # we always want to like go from the outer to the inner
        # as we go from left to right, if
        stack = []
        res = 0
        for t in target:
            if stack and stack[-1] > t:
                res += stack[-1] - t
            stack.append(t)
            # print(stack)

        if stack:
            res += stack[-1]
        return res