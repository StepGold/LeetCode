class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i, j = 0, 0
        li = []
        n1, n2 = len(nums1), len(nums2)
        k = 0
        while k < (n1 + n2) // 2 + 2:
            k += 1
            if (i < n1) and (j < n2):
                if nums1[i] < nums2[j]:
                    li.append(nums1[i])
                    i += 1
                else:
                    li.append(nums2[j])
                    j += 1
            elif (i < n1):
                li.append(nums1[i])
                i += 1
            elif (j < n2):
                li.append(nums2[j])
                j += 1
        k = n1 + n2
        return (li[(k-1)//2] + li[k//2]) / 2
