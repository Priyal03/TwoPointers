class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        uniqueIndex = 1

        for i in range(1,len(nums)):
            
            if nums[i-1] != nums[i]:
                
                nums[uniqueIndex] = nums[i]
                uniqueIndex += 1

        return uniqueIndex

# Time Complexity: O(N),

# Space Complexity: O(1),