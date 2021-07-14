class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
            count = 0  # Count of non-zero elements
            n = len(nums)
            # Traverse the array. If element
            # encountered is non-zero, then
            # replace the element at index
            # 'count' with this element
            for i in range(n):
                if nums[i] != 0:

                    # here count is incremented
                    nums[count] = nums[i]
                    count += 1

            # Now all non-zero elements have been
            # shifted to front and 'count' is set
            # as index of first 0. Make all
            # elements 0 from count to end.
            while count < n:
                nums[count] = 0
                count += 1


test = Solution()
arr = [0, 1, 0, 3, 12]
print(arr)
print('moving Zeroes...')
test.moveZeroes(arr)
print(arr)
