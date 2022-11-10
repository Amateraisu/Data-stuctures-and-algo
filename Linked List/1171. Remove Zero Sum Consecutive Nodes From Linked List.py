class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # time complexity would be O(N)
        # space complexity would be O(N) also.
        myMap = {}
        cumSumTracker = {}
        dummy = ListNode(0, head)
        currentPtr = head 
        currentSum = 0 
        cumSumTracker[dummy] = 0 
        myMap[0] = dummy 
        # print(myMap)
        # print(cumSumTracker)
        while currentPtr:
            currentNumber = currentPtr.val 
            currentSum += currentNumber
            if currentSum in myMap:
                temp = myMap[currentSum].next 
                while temp != currentPtr:
                    
                    myMap.pop(cumSumTracker[temp])
                    temp = temp.next 
                myMap[currentSum].next = currentPtr.next 
            else:
                myMap[currentSum] = currentPtr 
                cumSumTracker[currentPtr] = currentSum 
            
            currentPtr = currentPtr.next 
            
            
            
            
        return dummy.next