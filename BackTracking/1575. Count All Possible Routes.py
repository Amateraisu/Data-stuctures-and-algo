class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:

        mod = 10 ** 9 + 7

        @cache
        def dfs(current, fuel):
            if fuel == 0:
                return 1 if current == finish else 0
            best = 0

            for i, location in enumerate(locations):
                if i != current and fuel >= abs(locations[current] - locations[i]):
                    best += dfs(i, fuel - abs(locations[current] - locations[i]))
            if current == finish:
                best += 1
            return best % mod

        return dfs(start, fuel)