def sumKStrings(k):
    # Write your code here
    
    
    def makeFirstNum(n):
        res = ''
        if n % 2 == 1:
            n -= 1
            res += '1'
        while n - 2 >= 0:
            n -= 2
            res += '2'
        return res

    def swapTwos(str):
      res = []
      for i, char in enumerate(str):
        if char == '2':
          newNum = str[:i] + '11' + str[i + 1:]
          res.append(newNum)
      return res
    
    def swapOnes(str):
        res = []
        for i, char in enumerate(str):
          if i + 1 < len(str):
            if char == '1' and str[i + 1] == '1':
                newNum = str[:i] + '2' + str[i + 2:]
                res.append(newNum)
        return res

    result = [makeFirstNum(k)]
    result += swapTwos(result[0])
    
    finalSet = set()

    for num in result:
      finalSet.update(swapTwos(num))
      finalSet.update(swapOnes(num))
    
    result = list(finalSet)                
    
    result.sort()
    
    return result

print(sumKStrings(4))