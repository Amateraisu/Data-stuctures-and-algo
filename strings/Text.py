class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        n = len(words)
        assign = collections.defaultdict(int)
        wordLengths = collections.defaultdict(int)
        totalLength = collections.defaultdict(lambda: -1)

        for i in range(n):
            wordLengths[i] += len(words[i]) + 1

        def dfs(index, currentSpace, line):
            if index == n:
                return
            assign[index] = line
            current = currentSpace + len(words[index])
            totalLength[line] += len(words[index]) + 1
            # make sure the next word is valid
            if index == n - 1:
                dfs(index + 1, currentSpace, line)  # just end it
            else:
                # for the next word, there must be at least one line of space,
                nextWord = words[index + 1]
                if current + len(nextWord) + 1 <= maxWidth:
                    dfs(index + 1, current + 1, line)
                else:
                    dfs(index + 1, 0, line + 1)

            return

        dfs(0, 0, 0)
        numberOfLines = max(assign.values()) + 1
        res = [[] for i in range(numberOfLines)]
        for w in assign:
            res[assign[w]].append(words[w])
        for i in range(len(res) - 1):
            row = res[i]
            res[i] = processRow(row, maxWidth, totalLength[i])
            print(res[i])
        ret = []
        res[-1] = processRow(res[-1], maxWidth, totalLength[len(res) - 1], True)
        for r in res:
            ret.append(r)
        return ret


def processRow(row, maxWidth, totalLength, isLast=False):
    extra = maxWidth - totalLength
    countOfWords = len(row) - 1
    eachSpace = extra
    leftMost = eachSpace
    if isLast or len(row) == 1:
        return " ".join(row) + extra * ' '

    eachSpace = extra // (countOfWords)
    leftMost = extra % (countOfWords)
    for j in range(leftMost):
        row[j] += ' '

    for i in range(len(row) - 1):
        row[i] += ' ' * eachSpace
    return " ".join(row)