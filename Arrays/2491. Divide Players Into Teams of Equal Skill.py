from collections import Counter 
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:

        teams = len(skill) / 2 
        goal = sum(skill) / teams 
        # pick of size 2 
        if sum(skill) % teams != 0:
            return -1 
        goal = int(goal)
        countDict = Counter(skill)
        # try to form teams of skills equals to goal.
        res = 0 
        length = int(len(skill) / 2)
        skill.sort()

        skills = set()
        print(goal)
        for i in range(length):
            level = skill[i]
            otherGoal = goal - level 
            if otherGoal in countDict and countDict[otherGoal] > 0:
                print("current", level, otherGoal)
                final = otherGoal * level
                skills.add(otherGoal + level)
                res += final
                countDict[otherGoal] -= 1 
                
            else:
                return -1 

        return res if len(skills) == 1 else -1