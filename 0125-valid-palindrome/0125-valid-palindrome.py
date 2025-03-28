class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Time & space complexity : O(n), in length n of the string.
        """
        filtered_chars = filter(lambda ch: ch.isalnum(), s)
        lower_chars = map(lambda ch:ch.lower(),filtered_chars)

        char_list = list(lower_chars)
        reversed_list = char_list[::-1]

        return char_list == reversed_list
        """
        i = 0
        j = len(s) - 1
        
        # Loop Invariant (Key Assertion) "All characters outside the current [i, j] range (i.e., already checked characters) form a valid palindrome."
        while i < j:

            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            
            i += 1
            j -= 1

        return True

        # Time complexity : O(n), Space : O(1), no extra space required.