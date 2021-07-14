def buildString(k, str=''):
  if k - 1 == 0:
    str += '1'
    return str
  else:
    str += '2' + buildString(k - 2)
    return str

test = buildString(5)

print(test)

def expandStrings(str):
  numList = [str]
  while '2' in numList[-1]:
    numList.append(numList[-1].replace('2', '11', 1))
  return numList

def addPerms(l): 
  for num in l:
    left = 0
    right = len(num) - 1
    while right > left:
      if num[left] != num[right]:
        newNum = list(num)
        newNum[left], newNum[right] = newNum[right], newNum[left]
        newString = ''.join(newNum)
        if newString not in l:
          l.append(newString)
      right -= 1
      left += 1
    


testList = expandStrings(test)
print(testList)
addPerms(testList)
print(testList)

