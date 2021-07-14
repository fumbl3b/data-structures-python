grid = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],   # [-3][5]
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


def maxTunnelDepth(grid):
    # Write your code here
    maxDepth = len(grid)
    r = len(grid[0]) - 1
    l = 0
    mid = r // 2
    
    def checkPoint(x,y):
        if grid[maxDepth - y - 1][x]: return True
        else: return False
    
    print(checkPoint(mid,maxDepth))
    print(checkPoint(0,0))
    
    
    # start from the bottom center
    # loop upwards checking for ones
    # find 1 then check left and right
    #if left and right, check left and right again
    #if hit, see if theres a lower level
    #otherwise repeat until 0

print(maxTunnelDepth(grid))

found = False
    maxDepth = len(grid) - 1
    currDepth = maxDepth
    r = len(grid[0]) - 1
    l = 0
    mid = r // 2
    
    def checkPoint(x, depth = maxDepth):
        if grid[depth][x]: return True
        else: return False
    
    def checkUp(x,depth):
        if grid[depth - 1][x]: return True
        else: return False
    
    def checkLeft(x,depth):
        if grid[depth][x-1]: return True
        else: return False
    
    def checkRight(x,depth):
        if grid[depth][x+1]: return True
        else: return False
    
    while not found:
        if checkPoint(mid,currDepth):
        
            
        
    print(checkPoint(0,0))