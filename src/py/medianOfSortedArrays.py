def findMedianSortedArrays(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        bigNums = nums1 + nums2
        bigNums.sort()
        idx = len(bigNums) // 2

        if len(bigNums) % 2 == 0:
            print(bigNums)
            print(idx)
            calcMedian = (bigNums[idx] + bigNums[idx - 1]) / 2
            print(calcMedian)
            return calcMedian
        else:
            return bigNums[idx]

findMedianSortedArrays([1,2],[3,4])
        