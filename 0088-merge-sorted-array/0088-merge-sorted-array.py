class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        
        # And move k backward through the array, each time writing
        # the largest value pointed at by i or j.
        for k in range((m + n) - 1, -1, -1):

            if j < 0:
                break

            elif i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1

            # We know that upon initialization, k is n steps ahead of i (in other words, i + n = k). and this will ensure that k will not cross i before visiting i location.

            else:
                nums1[k] = nums2[j]
                j -= 1


# Time complexity: O(n+m).
# Space complexity: O(1).
