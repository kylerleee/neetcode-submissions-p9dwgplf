class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = []
        median = (1 + len(nums1) + len(nums2))/2
        
        for x in range(math.ceil(median)):
            if nums1 and nums2:
                if nums1[0] < nums2[0]:
                    res.append(nums1[0])
                    nums1.pop(0)
                else:
                    res.append(nums2[0])
                    nums2.pop(0)
            elif nums1 and not nums2:
                res.append(nums1[0])
                nums1.pop(0)
            else:
                res.append(nums2[0])
                nums2.pop(0)
             
        
        return res[-1] if median.is_integer() else (res[-1] + res[-2])/2