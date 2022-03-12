class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = list1
        ptr2 = list2 
        mainptr = None
        mainhead = None
        
        
        if ptr1 == None and ptr2 != None:
            return ptr2
        elif ptr2== None and ptr1 != None:
            return ptr1
        else:
            
        
        
            while ptr1 != None and ptr2 != None:
                if ptr1.val < ptr2.val:
                    if mainptr == None:
                        mainptr = ptr1
                        mainhead = ptr1
                    else:
                        mainptr.next = ptr1
                        mainptr = mainptr.next
                    ptr1 = ptr1.next

                else: #ptr1 is >= ptr2 
                    if mainptr == None:
                        mainptr = ptr2
                        mainhead = ptr2
                    else:
                        mainptr.next = ptr2
                        mainptr = mainptr.next 
                    ptr2 = ptr2.next

            if ptr1 != None:
                mainptr.next = ptr1
                mainptr = mainptr.next
                ptr1 = ptr1.next
            elif ptr2 != None:
                mainptr.next = ptr2
                mainptr = mainptr.next
                ptr2 = ptr2.next
            
        return mainhead
     ```