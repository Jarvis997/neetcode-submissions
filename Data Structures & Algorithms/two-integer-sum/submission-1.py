class Solution:
    def twoSum(self, nums, target):
        # Dictionary to store: { number_value: index }
        seen = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            # Check if the number we need has already been processed
            if complement in seen:
                # Return the past index first, then the current index
                return [seen[complement], i]
            
            # If not found, remember this number and its index for later
            seen[num] = i