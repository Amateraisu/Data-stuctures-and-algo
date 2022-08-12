class Solution(object):

    def assignBikes(self, workers, bikes):
	
        bikeStates = [0 for bike in bikes]
        workerStartIndex = 0 
        cache = {}
        
        def dfs(currentWorkerIndex, bikeStates):
            if currentWorkerIndex >= len(workers):
                return 0
            if (currentWorkerIndex, tuple(bikeStates)) in cache:
                return cache[(currentWorkerIndex, tuple(bikeStates))]
            
            temp = float("inf")
            
            currentWorker = workers[currentWorkerIndex]
            for index, bike in enumerate(bikes):
                if bikeStates[index] == 0:
                    bikeStates[index] = 1
                    manhattanDistance = findManhattanDistance(currentWorker, bike)

                    temp = min(temp, dfs(currentWorkerIndex + 1, bikeStates) + manhattanDistance)
                    
                    bikeStates[index] = 0
                    
            cache[(currentWorkerIndex, tuple(bikeStates))] =  temp
            
            return cache[(currentWorkerIndex, tuple(bikeStates))]
        
        return dfs(workerStartIndex, bikeStates)
        
def findManhattanDistance(worker, bike):
    return abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])