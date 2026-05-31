import heapq

class Twitter:
    # runtime of O(n) to O(logn)
    def __init__(self):
        self.users = {}
        self.timestamp = 0

    # space | O(n) 
    # time | O(1) | O(n) | (depending if we extend array)
    def postTweet(self, userId: int, tweetId: int) -> None:
        # if no users yet, init user 
        if userId not in self.users:
            self.users[userId] = [[], set()] # [tweets, followings]
        
        self.users[userId][0].append((self.timestamp, tweetId))
        self.timestamp += 1

    # space | O(n + m)
    # time | O(n) + O(k * m) + O(log(n + m)) + O(n + m)
    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []

        if userId not in self.users:
            return feed

        # O(n)
        for timestamp, tweet in self.users[userId][0]:
            feed.append((timestamp, tweet))

        # O(k * m)
        for follower in list(self.users[userId][1]):
            for timestamp, tweet in self.users[follower][0]:
                feed.append((timestamp, tweet))

        feed = heapq.nlargest(10, feed)

        return [feed[i][1] for i in range(len(feed))]

    # space | O(n)
    # time | O(n) | (depending of if you extend the list)
    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId == followerId:
            return

        if followerId not in self.users:
            self.users[followerId] = [[], set()]
            
        if followeeId not in self.users:
            self.users[followeeId] = [[], set()]

        self.users[followerId][1].add(followeeId)

    # space | O(n)
    # time | O(n)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId == followerId:
            return

        if followerId not in self.users:
            self.users[followerId] = [[], set()]
            
        if followeeId not in self.users:
            self.users[followeeId] = [[], set()]
        
        if followeeId in self.users[followerId][1]:
            self.users[followerId][1].remove(followeeId)
        
