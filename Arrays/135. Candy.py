class Solution:
    def candy(self, ratings: List[int]) -> int:
        if len(ratings) == 1:  # guarantees that the for loops later will have no out of bounds errors
            return 1
        n = len(ratings)
        res = [float("inf")] * n
        for i, rating in enumerate(ratings):
            if i == 0 and i + 1 < n:
                # check the index in front
                if ratings[i + 1] >= ratings[i]:
                    res[i] = 1
            elif i == n - 1 and i - 1 >= 0:
                # check the index at the back
                if ratings[i - 1] >= ratings[i]:
                    res[i] = 1
            else:
                # check both front and back
                if ratings[i - 1] >= ratings[i] and ratings[i + 1] >= ratings[i]:
                    res[i] = 1

        # I need to assign the ones who still dont have candy
        # the ones with infinity
        # I have to check the neighbors, and be greater than the ones
        for i in range(1, n):  # forward
            if ratings[i] > ratings[i - 1]:
                res[i] = res[i - 1] + 1

        for i in range(n - 2, -1, -1):  # backward
            # if it has not been assigned, that means I can just assign it freely
            if ratings[i] > ratings[i + 1] and res[i] == float("inf"):
                res[i] = res[i + 1] + 1
            # if it has BEEN assigned,that means the current number already satisfies the backwards neighbor
            # now I need to make sure it also satisfies its frontward neighbor
            elif ratings[i] > ratings[i + 1]:
                res[i] = max(res[i], res[i + 1] + 1)

        return sum(res)
