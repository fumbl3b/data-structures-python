class Solution(object):
   def findPeakElement(self, nums):
      low = 0
      high = len(nums)-1
      while low<high:
         mid = low + (high - low+1)//2
         if (mid-1>=0 and nums[mid-1]<=nums[mid]):
            low = mid
         else:
            high = mid-1
      return nums[low+1]


def getPeak(nums):
  l = 0
  r = len(nums) - 1
  while l < r:
    m = l + (r - l + 1) // 2
    if m - 1 >= 0 and nums[m - 1] <= nums[m]:
      l = m
    else:
      r = m - 1
  return l

print(getPeak([1,2,3,1]))