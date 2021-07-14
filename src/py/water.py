class Solution:
    def maxArea(self, height: list[int]) -> int:
        '''
        [1,8,6,2,5,4,8,3,7] len 9
         i               j = 9
           i             j = 49
           i           j   = 21
         
        
        '''
        if len(height) < 2: return 0
        
        current_max = 0
        
        # pointers at the beginning and end of height
        i,j = 0, len(height) - 1
        
        while j > i:
            water = min(height[i],height[j]) * (j - i)
            current_max = max(water,current_max)
            if height[j] > height[i]: i += 1
            else: j -= 1
        
        return current_max
        
test = Solution()
result = test.maxArea([1,8,6,2,5,4,8,3,7])
print(result)
        