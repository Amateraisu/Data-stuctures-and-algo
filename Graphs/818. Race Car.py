class Solution:
    def racecar(self, target: int) -> int:
        
        q = deque()
        start = [0, 0, 1] # instructions, pos, speed
        q.append(start)
        visited = set()

        while q:
            # print(q)
            currentNode = q.popleft()
            instruction, position, speed = currentNode 
            if position == target:

                return instruction
            # accelerate 
            if (position, speed) in visited:
                continue 
            else:
                visited.add((position, speed))

                q.append((instruction+ 1, position + speed, speed * 2))
                if (position + speed > target and speed > 0) or (position + speed < target and speed < 0):
                    speed = -1 if speed > 0 else 1 

                    q.append((instruction + 1, position, speed))

        return 0
