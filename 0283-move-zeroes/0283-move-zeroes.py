class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # lastNonZeroIndex=0

        # for i in range(len(nums)):
        #     if nums[i]!=0:  
        #         nums[lastNonZeroIndex]=nums[i]
        #         lastNonZeroIndex+=1

        # for i in range(lastNonZeroIndex,len(nums)):
        #     nums[i]=0
        
        
        lastNonZeroIndex=0
        for i in range(len(nums)):

            if nums[i]==0:
                continue
            else:
                nums[i],nums[lastNonZeroIndex]=nums[lastNonZeroIndex],nums[i]
                lastNonZeroIndex+=1
            

# In other words, the code will maintain the following invariant:

# All elements before the slow pointer (lastNonZeroIndex) are non-zeroes.

# All elements between the current and slow pointer(lastNonZeroIndex) are zeroes.

# Therefore, when we encounter a non-zero element, we need to swap elements pointed by current and slow pointer, then advance both pointers. If it's zero element, we just advance current pointer.