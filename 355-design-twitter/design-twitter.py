class Twitter:
    def __init__(self):
        """
        Initialize the Twitter object with necessary data structures.
        """
        # Counter to assign unique timestamps to tweets
        self.count = 0
        # Dictionary to store the users followed by each user
        self.followMap = defaultdict(set)
        # Dictionary to store the tweets posted by each user
        self.tweetMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Post a tweet by the given user.
        """
        # Append the tweet to the user's tweet list with a unique timestamp
        self.tweetMap[userId].append([self.count, tweetId])
        # Decrement the timestamp counter for uniqueness
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweets in the user's news feed.
        """
        # List to store the result of news feed
        res = []
        # Min heap to maintain the recent tweets from followed users
        minHeap = []

        # Add the user to its own followees to include its own tweets
        self.followMap[userId].add(userId)

        # Iterate over the followees of the user
        for followeeId in self.followMap[userId]:
            # Check if the followee has any tweets
            if followeeId in self.tweetMap:
                # Get the index of the latest tweet
                index = len(self.tweetMap[followeeId]) - 1
                # Get the timestamp and tweet ID of the latest tweet
                count, tweetId = self.tweetMap[followeeId][index]
                # Add the tweet to the min heap
                minHeap.append([count, tweetId, followeeId, index - 1])

        # Heapify the min heap
        heapq.heapify(minHeap)

        # Process the min heap until it is empty or 10 tweets are retrieved
        while minHeap and len(res) < 10:
            # Pop the tweet with the earliest timestamp
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            # Add the tweet ID to the result list
            res.append(tweetId)

            # If there are more tweets from the same followee, add them to the min heap
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Add a follow relationship between a follower and a followee.
        """
        # Add the followee to the follower's followees
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Remove a follow relationship between a follower and a followee.
        """
        # Check if the follower follows the followee
        if followeeId in self.followMap[followerId]:
            # Remove the followee from the follower's followees
            self.followMap[followerId].remove(followeeId)
