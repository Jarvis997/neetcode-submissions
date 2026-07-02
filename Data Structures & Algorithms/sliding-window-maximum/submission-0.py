from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        res = []
        q = deque()  # Stores indices of elements
        
        for i in range(len(nums)):
            # 1. Remove indices that have slid out of the current window bound
            if q and q[0] < i - k + 1:
                q.popleft()
                
            # 2. Maintain monotonic decreasing property
            # Pop elements from the back if they are smaller than the incoming element
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
                
            # 3. Append the current element's index to the back
            q.append(i)
            
            # 4. Once the window reaches size k, the front element is our max
            if i >= k - 1:
                res.append(nums[q[0]])
                
        return res