class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1, len2 = len(nums1), len(nums2)
        i, j = 0, 0
        median1, median2 = 0, 0

        for _ in range(((len1 + len2) // 2) + 1):
            median2 = median1
            if i < len1 and j < len2:
                if nums1[i] < nums2[j]:
                    median1 = nums1[i]
                    i += 1
                else:
                    median1 = nums2[j]
                    j += 1
            elif i < len1:
                median1 = nums1[i]
                i += 1
            elif j < len2:
                median1 = nums2[j]
                j += 1

        if (len1 + len2) % 2 == 0:
            return (median1 + median2) / 2.0
        else:
            return float(median1)

#TIME-COMPLEXITY: O((n+m)log(n+m))
#SPACE-COMPLEXITY: O(n+m) 

