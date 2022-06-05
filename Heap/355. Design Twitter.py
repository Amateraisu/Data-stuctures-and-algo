class Twitter:

    def __init__(self):
        self.followList = {} # follow list will be a set #O(1) 
        self.postList = {} # post list will be a list because to get latest post will be O(1)
        
        self.time = 0 
        
        
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.postList:
            self.postList[userId] = [[self.time, tweetId]]
        else:
            self.postList[userId].append([self.time, tweetId])
            
        self.time -= 1
        return 

    def getNewsFeed(self, userId: int) -> List[int]:
        maxHeap = [] # the posts with the highest time
        # retrieve all the posts and make them into a heap 
        # print("postList", self.postList)
        if userId in self.followList:
            self.followList[userId].add(userId)
            allPostIds = self.followList[userId]

        else:
            
            allPostIds = {userId}
        res = []
        # put all posts inside my max Heap 
        # print("test2", allPostIds, userId, self.followList)
        for id in allPostIds:
            # check if he made any tweets at all 
            if id in self.postList:
                for post in self.postList[id]:
                    # print("This is post", post)
                    maxHeap.append(post)
        heapq.heapify(maxHeap)
        # print("heap here", maxHeap)
        while len(res) < 10 and maxHeap:
            time, tweetId = heapq.heappop(maxHeap)
            res.append(tweetId)
            
        return res
            
        
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followList:
            self.followList[followerId] = set()
            self.followList[followerId].add(followeeId)
        else:
            self.followList[followerId].add(followeeId)
            
        return

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followList:
            return 
        else:
            self.followList[followerId].remove(followeeId)
            
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)