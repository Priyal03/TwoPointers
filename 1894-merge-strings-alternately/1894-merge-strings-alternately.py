class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        length = max(len(word1), len(word2))
        ans = []

        for i in range(length):
            if i < len(word1):
                ans.append(word1[i])
            if i < len(word2):
                ans.append(word2[i])

        return "".join(ans)

# Time complexity: O(m+n) and Space complexity: O(1) no extra space except input and outputs.