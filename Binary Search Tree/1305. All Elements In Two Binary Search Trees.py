class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        arra1 = []
        size1 = 0
        arra2 = []
        size2 = 0     
        totalarra = []
        def inorder(root, array):
            if root is None:
                return
            inorder(root.left,array)
            array.append(root.val)
            inorder(root.right,array)
            
            return 
        
        def sizeCounter(root):
            if root is None:
                return 0
            return 1+sizeCounter(root.left) + sizeCounter(root.right)
        
        size1 = sizeCounter(root1)
        size2 = sizeCounter(root2)
        inorder(root1, arra1)
        inorder(root2, arra2)
        print(arra1, arra2)
        counter1 = 0
        counter2 = 0
        
        
        while counter1 < size1 and counter2 <size2:
            if arra1[counter1] < arra2[counter2]:
                totalarra.append(arra1[counter1])
                counter1+=1
            else:
                totalarra.append(arra2[counter2])
                counter2+=1
                
        while counter1<size1:
            totalarra.append(arra1[counter1])
            counter1+=1
        while counter2<size2:
            totalarra.append(arra2[counter2])
            counter2+=1
        return totalarra