def isValid(x, y, maze):
    return x >= 0 and x <= len(maze) - 1 and y >= 0 and y <= len(maze[0]) - 1 and maze[x][y] == 0


class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        minHeap = []
        # it should be keyed according to key: distance, instruction
        minHeap.append((0, "", ball[0], ball[1]))
        directions = [(-1, 0, "u"), (1, 0, "d"), (0, -1, "l"), (0, 1, "r")]
        visited = set()
        res = []
        while minHeap:
            # print(res)
            # print(minHeap)
            curCost, ins, x, y = heapq.heappop(minHeap)

            if (x, y) in visited:
                continue
            visited.add((x, y))
            for direction in directions:
                temp_x = x
                temp_y = y
                new_x = x + direction[0]
                new_y = y + direction[1]
                dist = 0

                while isValid(new_x, new_y, maze):
                    temp_x = new_x
                    temp_y = new_y
                    if [temp_x, temp_y] == hole:
                        res.append([curCost + dist, ins + direction[2]])

                    new_x = new_x + direction[0]
                    new_y = new_y + direction[1]
                    dist += 1

                    #     print("incrementing")
                # print("pushing", ins + direction[2], temp_x, temp_y)

                heapq.heappush(minHeap, [curCost + dist, ins + direction[2], temp_x, temp_y])
        # print(res)
        if not res:
            return "impossible"

        res.sort(key=lambda x: (x[0], x[1]))
        # print("HELLO WORLD")
        # print(res, "WHY")
        return res[0][1]