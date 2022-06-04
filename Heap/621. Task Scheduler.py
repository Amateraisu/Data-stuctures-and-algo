class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        
        # O(n * m)
        maxHeap = [-cnt for cnt in count.values()]
        
        heapq.heapify(maxHeap)
        
        time = 0 
        q = deque()
        
        while maxHeap or q:
            time += 1 
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt != 0 :
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
            
        return time