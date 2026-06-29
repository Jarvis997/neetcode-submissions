class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        output = [1] * n
        
        # Pass 1: Calculate prefix products (Left to Right)
        # Each index will temporarily hold the product of all numbers before it
        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]
            
        # Pass 2: Calculate suffix products (Right to Left)
        # Multiply the existing prefix values by a running suffix product
        suffix = 1
        for i in range(n - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]
            
        return output