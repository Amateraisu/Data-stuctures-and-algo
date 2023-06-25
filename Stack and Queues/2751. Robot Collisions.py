class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        stack = []
        n = len(positions)

        total = [(pos, x, y) for pos, x, y in sorted(zip(positions, healths, directions))]
        mapper = {}
        for i, pos in enumerate(positions):
            mapper[pos] = i
            # print(total)
        for i in range(n):
            health, direct = total[i][1], total[i][2]
            robo = mapper[total[i][0]]
            # if there is anything in the stack of the opposite direction,
            # if i == 3:
            #     print(stack, "here", health, direct)
            while stack and (stack[-1][1] == 'R' and direct == 'L') and health > 0:
                top = stack[-1][0]
                # remove the one with lower health
                if health < top:

                    stack[-1][0] -= 1
                    health = 0
                    # if i ==3 :
                    #     print('condition met', stack)

                elif health == top:
                    stack.pop()
                    health = 0
                else:
                    health -= 1
                    stack.pop()
            if health > 0:
                stack.append([health, direct, robo])
            # print(stack)
        stack.sort(key=lambda x: x[2])
        print(stack)
        return [x for x, y, z in stack]