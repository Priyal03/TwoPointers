class Solution:
    def validPalindrome(self, s: str) -> bool:

        def check_palindrome(left, right, removed):

            while left < right:
                
                if s[left] != s[right]:
                    
                    if removed:
                        return False
                    
                    return check_palindrome(left + 1, right, True) or check_palindrome(left, right - 1, True)

                left += 1
                right -= 1

            return True

        return check_palindrome(0, len(s) - 1, False)

# Time complexity: O(N) at max two times N/2 comparisons. Space complexity: O(1)