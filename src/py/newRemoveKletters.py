from typing import List


def removeKStrings(s,k):

  result = []
  characters = list(set(s))

  def removeLetter(s, target):
    return s.replace(target, '')


  def generateCombos(items,k):
      returnSet = []
      N = len(items)
      for i in range(2**N):
        combo = []
        for j in range(N):
          if(i>>j) % 2 == 1:
            combo.append(items[j])
        if len(combo) == k:
          returnSet.append(combo)
      return returnSet

  combinations = generateCombos(characters,k)
  print(combinations)

  for charSet in combinations:
    tempString = s
    for char in charSet:
      tempString = removeLetter(tempString,char)
    result.append(str(tempString))

  result.sort()
  return result
    
print(removeKStrings('abaca',2))
