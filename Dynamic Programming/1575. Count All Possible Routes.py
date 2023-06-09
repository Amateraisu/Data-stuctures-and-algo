class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = 10 ** 9 + 7
        n = len(locations)

        @cache
        def dfs(location, fuelRemaining):
            if fuelRemaining < 0:
                return 0
            best = 0
            if location == finish:
                best = 1
            for i in range(n):
                if i != location:
                    best += dfs(i, fuelRemaining - abs(locations[location] - locations[i]))

            return best % MOD

        return dfs(start, fuel)