class Solution(object):
    def twoSum(self, nums, target):
        
        # Dictionary to store values ​​and their indices
        num_indices = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            # Check if the complement is in the dictionary
            if complement in num_indices:
                return [num_indices[complement], i]
            
            # Add the number and its index to the dictionary
            num_indices[num] = i

# Example of use
solution = Solution()

nums1 = [2, 7, 11, 15]
target1 = 9
print(solution.twoSum(nums1, target1)) 
