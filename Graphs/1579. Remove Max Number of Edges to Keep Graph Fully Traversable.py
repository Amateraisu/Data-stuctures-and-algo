class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        a_par = [i for i in range(n)]
        b_par = [i for i in range(n)]
        a_ranks = [1 for i in range(n)]
        b_ranks = [1 for i in range(n)]
        edges.sort(key=lambda x: x[0] * -1)
        res = 0
        for t, a, b in edges:
            a -= 1
            b -= 1
            if t == 3:
                if not union(a, b, a_par, a_ranks) or not union(a, b, b_par,
                                                                b_ranks):  # if it is both, either one needs to be disconnected for me to perform this operation
                    res += 1
            elif t == 1:
                if not union(a, b, a_par, a_ranks):
                    res += 1

            elif t == 2:
                if not union(a, b, b_par, b_ranks):
                    res += 1

            else:
                continue

                # if either of them are not fully connected, return -1
        # print(a_par)
        # print(b_par)
        a_visited = set()
        b_visited = set()
        for n in a_par:
            p = find(n, a_par)
            a_visited.add(p)
        for n in b_par:
            p = find(n, b_par)
            b_visited.add(p)
        if len(set(a_visited)) != 1 or len(set(b_visited)) != 1:
            return -1

        return res


def find(n, parents):
    if parents[n] != n:
        parents[n] = find(parents[n], parents)

    return parents[n]


def union(a, b, parents, ranks):
    p1, p2 = find(a, parents), find(b, parents)

    if p1 == p2:
        return False  # returning false means it is already connected

    if ranks[p1] > ranks[p2]:
        ranks[p1] += ranks[p2]
        ranks[p2] = ranks[p1]
        parents[p2] = p1
    else:
        ranks[p2] += ranks[p1]
        ranks[p1] = ranks[p2]
        parents[p1] = p2
    return True