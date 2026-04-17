class Twitter:

    def __init__(self):
        self.counter = 0
        self.arr = []
        self.following = {}
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.arr, (-self.counter, userId, tweetId))
        self.counter += 1 
        if not userId in self.following:
            self.following[userId] = set()

    def getNewsFeed(self, userId: int) -> List[int]:
        heapcopy = self.arr.copy()
        i = 0
        res = []
        while i < 10 and heapcopy:
            top = heapq.heappop(heapcopy)
            if top[1] == userId or top[1] in self.following[userId]:
                i += 1
                res.append(top[2])
        
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].add(followeeId)
        else:
            self.following[followerId] = {followeeId}
        print(self.following)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
