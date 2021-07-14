def prefixHeavyPermutations(n, k):

  arr = []
  arrList = []
  for i in range(n):
    arr.append(n-i)

  def perm(arr, pointer = 0):
    if pointer == len(arr):
      permutation = list(arr)
      arrList.append(permutation)
    else:
      for i in range(pointer,len(arr)):
        arr[pointer], arr[i] = arr[i], arr[pointer]
        perm(arr, pointer + 1)
        arr[pointer], arr[i] = arr[i], arr[pointer]
  
  print(arr)
  perm(arr)
  print(arrList)


prefixHeavyPermutations(4, 2)