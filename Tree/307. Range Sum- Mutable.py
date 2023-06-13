
class NumArray:

    def __init__(self, nums: List[int]):
        self.tree = segTree(nums)

    def update(self, index: int, val: int) -> None:
        update(self.tree.tree, index, val)


    def sumRange(self, left: int, right: int) -> int:
        return query(self.tree.tree, left, right)

class segTree:

    def __init__(self, nums):
        self.tree = self.buildTree(0, len(nums) - 1, nums)
    def buildTree(self, start, end, nums):
        if start == end:
            return node(start, end, nums[start])
        mid = (start + end )/ /2

        left = self.buildTree(start, mid, nums)
        right = self.buildTree(mid + 1, end, nums)

        return node(start, end, left.sum + right.sum, left, right)


def update(root, index, val):
    if root.start == root.end == index:
        root.sum = val
        return
    mid = (root.start + root.end) / /2
    if index <= mid:
        update(root.left, index, val)
    else:
        update(root.right, index, val)
    root.sum = root.left.sum + root.right.sum

def query(root, i, j):
    if root.start == i and root.end == j:
        return root.sum
    mid = (root.start + root.end) // 2
    if j <= mid:
        return query(root.left, i, j)
    elif i > mid:
        return query(root.right, i, j)

    return query(root.left, i, mid) + query(root.right, mid + 1, j)


class node:
    def __init__(self, start, end, total, left = None, right = None):
        self.start = start
        self.end = end
        self.sum = total
        self.left = left
        self.right = right