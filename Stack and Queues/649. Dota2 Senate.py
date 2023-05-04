class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # play the strategy for your own party
        # ending score should be equals to the length of the string
        net = 0
        stack = list(senate)

        while True:
            new = []
            should = False
            for s in stack:
                if s == 'D':
                    net += 1
                    if net > 0:
                        new.append(s)
                    else:
                        should = True

                elif s == 'R':
                    net -= 1
                    if net < 0:
                        new.append(s)
                    else:  # that means I deleted an element
                        should = True

            stack = new
            if not should:
                break

        if net > 0:
            return "Dire"

        return "Radiant"

