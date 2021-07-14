class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        a, z = 0, len(nums) - 1
        
        while a <= z:
            if nums[z] == val:
                z -= 1
            elif nums[a] == val:
                nums[z],nums[a] = nums[a],nums[z]
                z -= 1
                a += 1
            else:
                a += 1
        while a > 0:
            nums.pop()
            a -= 1

test = Solution()
nums = [0,1,2,2,3,0,4,2]
print(nums,'removing element')
test.removeElement(nums,2)
print(nums)