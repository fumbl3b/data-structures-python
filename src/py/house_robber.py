class Solution:
  def rob(self, nums):

    rob1, rob2 = 0,0

    for n in nums:
      temp = max(n + rob1, rob2)
      rob1 = rob2
      rob2 = temp
    return rob2

    def dp(m, arr):
      pass

    return dp(arr)


test = Solution()
print(test.rob([1,2,3,1]))