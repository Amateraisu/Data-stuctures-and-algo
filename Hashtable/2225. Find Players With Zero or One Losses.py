class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        res = [[], []]
        count = defaultdict(int)
        playerList = set()
        for match in matches:
            winner, loser = match 
            count[loser] += 1 
            playerList.add(loser)
            playerList.add(winner)

        for player in playerList:
            if player not in count:
                res[0].append(player)
            elif count[player] == 1:
                res[1].append(player)
                
                
        res[0].sort()
        res[1].sort()
        
        return res