import collections
from math import ceil, log2
import io, os, time, sys

sys.setrecursionlimit(10**7)
class segment_tree:
    # merge(left, right): function used to merge the two halves
    # basef(value): function applied on individual values
    # basev: identity for merge function, merger(value, basev) = value
    # update(node_value, old, new): function to update the nodes
    def __init__(self, array, merge=lambda x, y: x + y, basef=lambda x: x, basev=0):
        self.merge = merge
        self.basef = basef
        self.basev = basev
        self.n = len(array)
        self.array = array
        self.tree = [0] * (2 ** ceil(log2(len(array)) + 1) - 1)
        self.build(array)

    def __str__(self):
        return ' '.join([str(x) for x in self.tree])

    def _build_util(self, l, r, i, a):
        if (l == r):
            self.tree[i] = self.basef(a[l])
            return self.tree[i]
        mid = (l + r) // 2
        self.tree[i] = self.merge(self._build_util(l, mid, 2 * i + 1, a), self._build_util(mid + 1, r, 2 * i + 2, a))
        return self.tree[i]

    def build(self, a):
        self._build_util(0, len(a) - 1, 0, a)

    def _query_util(self, i, ln, rn, l, r):
        if ln >= l and rn <= r:
            return self.tree[i]
        if ln > r or rn < l:
            return self.basev
        return self.merge(self._query_util(2 * i + 1, ln, (ln + rn) // 2, l, r),
                          self._query_util(2 * i + 2, (ln + rn) // 2 + 1, rn, l, r))

    def query(self, l, r):
        return self._query_util(0, 0, self.n - 1, l, r)

    def _update_util(self, i, ln, rn, x, v):
        if x >= ln and x <= rn:
            if ln != rn:
                self._update_util(2 * i + 1, ln, (ln + rn) // 2, x, v)
                self._update_util(2 * i + 2, (ln + rn) // 2 + 1, rn, x, v)
                self.tree[i] = self.merge(self.tree[2 * i + 1], self.tree[2 * i + 2])
            else:
                self.tree[i] = self.basef(v)

    def update(self, x, v):
        self._update_util(0, 0, self.n - 1, x, v)
        self.array[x] = v

input = io.BytesIO(os.read(0, \
     os.fstat(0).st_size)).readline
n, q = input().split()
n = int(n)
q = int(q)
values = input().split()
values = [int(x) for x in values]
graph = collections.defaultdict(set)
for i in range(n - 1):
    a, b = input().split()
    a = int(a)
    b = int(b)
    graph[a].add(b)
    graph[b].add(a)
dp = [[], [0 for i in range(n)], []]
visited = set()
mapper = collections.defaultdict(int)

#O(N)
def dfs(currentNode):
    dp[0].append(currentNode)
    mapper[currentNode] = len(dp[0]) - 1
    dp[2].append(values[currentNode - 1])
    visited.add(currentNode)
    curCount = 1
    for nei in graph[currentNode]:
        if nei not in visited:
            curCount += dfs(nei)
    dp[1][mapper[currentNode]] = curCount
    return curCount


dfs(1)

#O(N)
tree = segment_tree(dp[2])

for i in range(q):
    v = input().split()
    v = [int(x) for x in v]

    if v[0] == 2:
        newIndex = mapper[v[1]]
        size = dp[1][newIndex]
        res = tree.query(newIndex, newIndex + size - 1)
        sys.stdout.write(str(res)+"\n")
    else:
        newIndex = mapper[v[1]]
        tree.update(newIndex, v[2])