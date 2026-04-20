class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total / 2

        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1

        l1, r1 = 0, len(nums1) - 1

        while True:
            m1 = (l1+r1)//2
            m2 = math.floor(half) - m1 - 2

            m1left = nums1[m1] if m1 >= 0 else float("-infinity")
            m1right = nums1[m1+1] if (m1+1) < len(nums1) else float("infinity")
            m2left = nums2[m2] if m2 >= 0 else float("-infinity")
            m2right = nums2[m2+1] if (m2+1) < len(nums2) else float("infinity")

            if m1left <= m2right and m2left <= m1right:
                return (max(m1left,m2left) + min(m1right, m2right))/2 if half.is_integer() else min(m1right, m2right)

            elif m1left > m2right:
                r1 = m1 - 1
            else:
                l1 = m1 + 1
