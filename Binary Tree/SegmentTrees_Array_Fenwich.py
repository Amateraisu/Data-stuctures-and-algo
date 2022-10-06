#Segment tree node
class Node(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.total = 0
        self.left = None
        self.right = None
        

class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        #helper function to create the tree from input array
        def createTree(nums, l, r):
            
            #base case
            if l > r:
                return None
                
            #leaf node
            if l == r:
                n = Node(l, r)
                n.total = nums[l]
                return n
            
            mid = (l + r) // 2
            
            root = Node(l, r)
            
            #recursively build the Segment tree
            root.left = createTree(nums, l, mid)
            root.right = createTree(nums, mid+1, r)
            
            #Total stores the sum of all leaves under root
            #i.e. those elements lying between (start, end)
            root.total = root.left.total + root.right.total
                
            return root
        
        self.root = createTree(nums, 0, len(nums)-1)
            
    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        #Helper function to update a value
        def updateVal(root, i, val):
            
            #Base case. The actual value will be updated in a leaf.
            #The total is then propogated upwards
            if root.start == root.end:
                root.total = val
                return val
        
            mid = (root.start + root.end) // 2
            
            #If the index is less than the mid, that leaf must be in the left subtree
            if i <= mid:
                updateVal(root.left, i, val)
                
            #Otherwise, the right subtree
            else:
                updateVal(root.right, i, val)
            
            #Propogate the changes after recursive call returns
            root.total = root.left.total + root.right.total
            
            return root.total
        
        return updateVal(self.root, i, val)

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        #Helper function to calculate range sum
        def rangeSum(root, i, j):
            
            #If the range exactly matches the root, we already have the sum
            if root.start == i and root.end == j:
                return root.total
            
            mid = (root.start + root.end) // 2
            
            #If end of the range is less than the mid, the entire interval lies
            #in the left subtree
            if j <= mid:
                return rangeSum(root.left, i, j)
            
            #If start of the interval is greater than mid, the entire inteval lies
            #in the right subtree
            elif i >= mid + 1:
                return rangeSum(root.right, i, j)
            
            #Otherwise, the interval is split. So we calculate the sum recursively,
            #by splitting the interval
            else:
                return rangeSum(root.left, i, mid) + rangeSum(root.right, mid+1, j)
        
        return rangeSum(self.root, i, j)
                


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.update(1, 10)
# numArray.sumRange(1, 2)

# class NumArray:

#     def __init__(self, nums: List[int]):
#         # construct a segment Tree 
#         # total Nodes = 2 N - 1 WHERE N is the number of leaf nodes 
#         # since this is a binary Tree 
#         totalNodes = 2 * len(nums) - 1 
#         self.N = len(nums) - 1 
#         self.segmentTree = constructTree(totalNodes, nums)
#         self.nums = nums

        

#     def update(self, index: int, val: int) -> None:
        
#         # for update, if in range, add it to the sum 
#         difference = val - self.nums[index]
#         # then just traverse down the tree and add the difference 
        
#         updateTree(0, 0, self.N, index, self.segmentTree , difference)
        
        
        

#     def sumRange(self, left: int, right: int) -> int:
        
#         return querySum(left, right, 0, 0, self.N, self.segmentTree)
        
# def updateTree(currentTreeIndex, rangeLeft, rangeRight, indexToUpdate, tree, toAdd):
#     if indexToUpdate == rangeLeft == rangeRight:
#         tree[currentTreeIndex] + toAdd
        
#         return 
#     middle = rangeLeft + (rangeRight - rangeLeft) // 2 
#     updateTree(currentTreeIndex * 2 + 1 , rangeLeft, middle, indexToUpdate, tree, toAdd)
#     updateTree(currentTreeIndex * 2 + 2, middle + 1, rangeRight, indexToUpdate, tree, toAdd)
    
#     return
        
# def querySum(targetLeft, targetRight, currentTreeIndex, rangeLeft, rangeRight, tree):
#     if rangeLeft == targetLeft and rangeRight == targetRight:
#         return tree[currentTreeIndex]
    
#     if rangeLeft >  targetRight:
#         return 0 
#     if rangeRight < targetLeft:
#         return 0 
#     middle = rangeLeft + (rangeRight - rangeLeft)//2 
#     return querySum(targetLeft, targetRight, currentTreeIndex * 2 + 1, rangeLeft, middle , tree) + querySum(targetLeft, targetRight, currentTreeIndex * 2 + 2, middle, right , tree)
        


# # Your NumArray object will be instantiated and called as such:
# # obj = NumArray(nums)
# # obj.update(index,val)
# # param_2 = obj.sumRange(left,right)


# def constructTree(totalNodes, nums):
#     tree = [0] * totalNodes 
    
#     current = 0 

#     fillUpTree(0, len(nums) - 1 ,0,  tree, nums)

#     return tree

# def fillUpTree(left, right, currentIndex, tree, nums):

#     if (left == right):

#         tree[currentIndex] = nums[right]
        
#         return nums[right]
#     if left > right:
#         return 0
    
#     mid = left + (right - left)//2
#     leftSum = fillUpTree(left, mid, currentIndex * 2 + 1, tree, nums)
#     rightSum = fillUpTree(mid + 1, right, currentIndex * 2 + 2, tree, nums)
#     tree[currentIndex] = leftSum + rightSum 
    
#     return tree[currentIndex]