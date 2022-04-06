class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        #time complexity is O(n) where n is the number of pixels in the image
        #space complexity is O(1) 
        for array in image:
            reverseArray(array)
            flipArray(array)
            
        return image
        
        
        
def reverseArray(array):
    ptr1 = 0
    ptr2 = len(array)-1
    
    
    while ptr1 < ptr2:
        array[ptr1], array[ptr2] = array[ptr2], array[ptr1]
        ptr1+=1
        ptr2 -=1
        
    return

def flipArray(array):
    for index in range(len(array)):
        binary = array[index]
        if binary:
            array[index] = 0
        else:
            array[index] = 1
    return