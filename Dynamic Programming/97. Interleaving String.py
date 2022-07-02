class Solution:
    
    
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False 
        
        
        ptr1 = 0 
        ptr2 = 0 
        ptr3 = 0 
        cache = {}
        
        return self.recursive(s1, s2, s3, ptr1, ptr2, ptr3, cache)
        
    def recursive(self, s1, s2, s3, ptr1, ptr2, ptr3, cache):
        
        
        if ptr3 == len(s3) and ptr1 + ptr2 != ptr3:
            return False 
        
        elif ptr3 == len(s3) and ptr1 + ptr2 == ptr3:
            return True 
        
        elif ptr3 == len(s3):
            return False 
        
        if (ptr1, ptr2, ptr3) in cache:
            return cache[(ptr1, ptr2, ptr3)]
        
        cache[(ptr1, ptr2, ptr3)] = False 
        
        
        if ptr1 == len(s1) and ptr2 == len(s2):
            return False 
        
        if ptr1 < len(s1) and s3[ptr3] == s1[ptr1]:
            if self.recursive(s1, s2, s3, ptr1 + 1, ptr2, ptr3 + 1, cache):
                cache[(ptr1, ptr2, ptr3)] = True 
                return cache[(ptr1, ptr2, ptr3)]
            
        if ptr2 < len(s2) and s3[ptr3] == s2[ptr2]:
            if self.recursive(s1, s2,s3, ptr1, ptr2 + 1, ptr3 + 1, cache):
                cache[(ptr1, ptr2, ptr3)] = True 
                return cache[(ptr1, ptr2, ptr3)]
            
        
        return cache[(ptr1, ptr2, ptr3)] 
        