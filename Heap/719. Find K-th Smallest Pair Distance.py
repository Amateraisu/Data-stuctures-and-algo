class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        # TLE
        n = len(nums)
        cur = n * (n - 1) // 2
        nums.sort()
        minHeap = [[(nums[-1] - nums[0]) * -1, n - 1, 0]]
        visited = set()
        visited.add((0, n - 1))
        diff = minHeap[0][0]
        while cur != k:

            diff, last, initial = heapq.heappop(minHeap)
            if last - 1 > initial and (initial, last - 1) not in visited:
                visited.add((initial, last - 1))
                heapq.heappush(minHeap, [(nums[last - 1] - nums[initial]) * -1, last - 1, initial])
            if initial + 1 < last and (initial + 1, last) not in visited:
                visited.add((initial + 1, last))
                heapq.heappush(minHeap, [(nums[last] - nums[initial + 1]) * -1, last, initial + 1])

            cur -= 1

        return minHeap[0][0] * -1