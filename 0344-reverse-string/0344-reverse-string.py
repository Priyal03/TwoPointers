class Solution:
    def reverseString(self, s: List[str]) -> None:
        # Approach 1: Recursion, In-Place, O(N) Space. Is it in place? Yes. Is it constant space? No, because of the recursion stack.
        # Time complexity : O(N) time to perform N/2 swaps.
        # Space complexity : O(N) to keep the recursion stack.
        """
        def helper(left,right):

            if left<right:
                s[left], s[right] = s[right], s[left]
                helper(left+1,right-1)

        helper(0,len(s)-1)
        """
        # Approach 2: Two Pointers, Iteration, O(1) Space
        # Time complexity : O(N) to swap N/2 element.
        # Space complexity : O(1), it's a constant space solution.

        left=0
        right=len(s)-1

        while left<right:
            s[left], s[right] = s[right], s[left]
            left+=1
            right-=1