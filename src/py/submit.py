def sumKStrings(k):
    
    def buildString(k, str=''):
        if k == 0:
            return str
        if k - 1 == 0:
          str += '1'
          return str
        else: 
            str += '2' + buildString(k - 2)
            return str
    
    def expandStrings(str):
        numList = [str]
        while '2' in numList[-1]:
            numList.append(numList[-1].replace('2', '11', 1))
        return numList
    
    def addPerms(arr):
        for num in arr:
            l = 0
            r = len(num) - 1
            while r > l:
                if num[l] != num[r]:
                    newNum = list(num)
                    newNum[l], newNum[r] = newNum[r], newNum[l]
                    newString = ''.join(newNum)
                    if newString not in arr:
                        arr.append(newString)
                l += 1
        
    result = buildString(k)
    print('original string', result)
    result = expandStrings(result)
    addPerms(result)
    # result.sort()
                
    return result

print('sumKSTrings on 3', sumKStrings(3))
print('sumKSTrings on 4', sumKStrings(4))
print('sumKSTrings on 7', sumKStrings(7))