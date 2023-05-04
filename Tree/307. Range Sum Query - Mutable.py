class Tree:
    def __init__(self, length, array):
        self.tree = [0 for i in range(length)]
        self.n = length // 2
        for i in range(len(array)):
            self.tree[len(array) + i] = array[i]
        for i in range(length - 1 - len(array), 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def query(self, left: int, right: int) -> int:
        res = 0
        left += self.n
        right += self.n
        while left <= right:
            if left % 2 == 1:
                res += self.tree[left]
                left += 1
            if right % 2 == 0:
                res += self.tree[right]
                right -= 1
            left //= 2
            right //= 2

        return res

    def update(self, index, val):
        index += self.n
        self.tree[index] = val

        # Propagate the change up the tree
        while index > 0:
            left = right = index
            if index % 2 == 0:
                right = index + 1
            else:
                left = index - 1
            self.tree[index // 2] = self.tree[left] + self.tree[right]
            index //= 2


class NumArray:
    def __init__(self, nums: List[int]):
        n = len(nums)
        self.tree = Tree(2 * n, nums)

        return

    def update(self, index: int, val: int) -> None:
        self.tree.update(index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.tree.query(left, right)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)