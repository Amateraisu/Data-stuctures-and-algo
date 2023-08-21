class Solution:
    def sortItems(self, n: int, m: int, group: List[int], pre: List[List[int]]) -> List[int]:
        groups = collections.defaultdict(set)
        group_id = collections.defaultdict(int)
        total = n
        for i in range(n):
            if group[i] == -1:  # they are in their own group
                groups[total].add(i)
                group_id[i] = total
                total += 1
            else:
                group_id[i] = group[i]
                groups[group[i]].add(i)
        # sort everyone amongst themselves first
        new_groups = collections.defaultdict(list)
        # this is only O(n) because this is inter group sorting
        visited = set()

        def dfs(currentNode, curGroup):
            if currentNode in visited:
                return True
            if currentNode in isVisiting:
                return False

                # check the currentNode's prereqs
            isVisiting.add(currentNode)

            for prereq in pre[currentNode]:
                if prereq in groups[curGroup]:
                    if not dfs(prereq, curGroup):
                        return False
            isVisiting.discard(currentNode)
            new_groups[curGroup].append(currentNode)
            visited.add(currentNode)
            return True

        for g in groups:
            visited = set()
            if len(groups[g]) == 1:
                new_groups[g].append(list(groups[g])[0])
            else:

                for node in groups[g]:
                    isVisiting = set()
                    if not dfs(node, g):  # we have detected an acyclic graph, invalid
                        return []
                        # print(new_groups)
        prereqs = collections.defaultdict(set)
        for g in new_groups:
            for node in new_groups[g]:
                for p in pre[node]:
                    if group_id[p] == g:
                        continue
                    prereqs[g].add(group_id[p])
        visited = set()
        res = []
        isVisiting = set()

        def dfs2(currentGroup):
            nonlocal res, isVisiting
            if currentGroup in visited:
                return True
            if currentGroup in isVisiting:
                return False
            isVisiting.add(currentGroup)
            for p in prereqs[currentGroup]:

                if not dfs2(p):
                    return False
            visited.add(currentGroup)
            isVisiting.discard(currentGroup)
            res += new_groups[currentGroup]
            # print('final', currentGroup)
            return True
            # print(new_groups)

        # print(prereqs)
        for node in range(n):
            isVisting = set()
            if group_id[node] in visited:
                continue
            # print("starting,", group_id[node])
            if not dfs2(group_id[node]):
                return []

        return res