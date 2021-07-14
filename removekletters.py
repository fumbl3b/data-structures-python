
def removeKStrings(s, k):
  # Write your code here
  res = []
  options = []
  letters = list(set(s))

  def removeLetters(s,letters):
    newString = ''
    for char in s:
      if char not in letters:
        newString += char
    return newString

  for char in letters:
    holder = []
    holder.append(char)
    letters.remove(char)
    for l in letters:
      newL = str(l)
      holder.append(newL)
      options.append(list(holder))


  for option in options:
    res.append(removeLetters(s,option))
      
  return res
  
def powerSet(items, k):
    returnSet = []
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        if len(combo) == k:
          returnSet.append(combo)
    return returnSet

print(powerSet(['a','b','c'],2))



# print(removeKStrings('abab',1))
# print(removeKStrings('abaca', 2))