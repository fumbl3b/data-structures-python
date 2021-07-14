def solution(nums, target):
    l , r = 0, len(nums) - 1
    res = [-1, -1]

    while r > l and r - l > 1:
        m = (l + r) // 2
        if nums[m] == target:
            # find beginning and end
            print('looping down from ', m, ' to ', l)
            for n in range(m,l - 1,-1):
                print('n is',n)
                if nums[n] != target:                
                    res[0] = n + 1
                    break
            print('looping from ', m, ' to ', r)
            for n in range(m,r + 1):
                print('n is',n)
                if nums[n] != target:
                    res[1] = n - 1
                    break
            return res
        elif target > nums[m]:
            l = m
        elif target < nums[m]:
            r = m
    return res


# print(solution([1,2,3,4,5,5,7,7,8,8,8,10],8))
# print(solution([5,7,7,8,8,10],8))
print(solution([5,7,7,8,8,10],6))


'''

5 7 7 8 8 10
l   m      r
l m r
l r
r

'''

