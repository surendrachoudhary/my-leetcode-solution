class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count the frequency of each task
        count = Counter(tasks)
        # Initialize the current time
        time = 0
        # Initialize a queue to track tasks waiting for cooldown
        queue = deque()
        # Initialize a max heap to store the negative frequencies of tasks
        maxheap = []
        
        # Push the negative frequencies onto the max heap
        for freq in count.values():
            heapq.heappush(maxheap, -freq) 

        # While there are tasks in the max heap or the queue is not empty
        while maxheap or queue:
            # Increment the time
            time += 1
            # If there are tasks in the max heap
            if maxheap:
                # Pop the negative frequency of the most frequent task
                cnt = heapq.heappop(maxheap)
                # Decrease the frequency (negative value), 
                # add 1 to simulate cooldown (negative becomes less negative)
                update_cnt = cnt + 1
                # If the task still has remaining occurrences
                if update_cnt:
                    # Append the updated frequency and the time for cooldown to the queue
                    queue.append([update_cnt, time + n])
            
            # If there are tasks in the queue and it's time to execute a task
            if queue and time == queue[0][1]:
                # Push the task back into the max heap after cooldown
                heapq.heappush(maxheap, queue.popleft()[0])

        # Return the total time taken
        return time
