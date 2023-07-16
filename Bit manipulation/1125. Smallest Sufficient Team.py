class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        mp = {skill : i for i, skill in enumerate(req_skills)}

        cand = []
        for skills in people:
            val = 0
            for skill in skills:
                val |= 1 << mp[skill]
            cand.append(val)

        @cache
        def dfs(i, mask):
            if mask == 0:
                return []
            if i == len(people):
                return [0] * 100 # impossible
            if not (mask & cand[i]):
                return dfs(i + 1, mask)
            new = mask & ~cand[i]
            return min(dfs(i + 1, mask), [i] + dfs(i + 1, new), key = len)
        return dfs(0, (1 << len(req_skills)) - 1)