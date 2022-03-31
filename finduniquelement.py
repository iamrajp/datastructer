
"""

Find unique Element from sorted array

Time Complexity : O(log(n))
Space Complexity: O(log(n))

"""

array = [1, 1,1,1,1,1]

hs = []
def findunique(array, left, right):
  mid = left + (right-left)//2
  if array[mid] not in hs:
     hs.append(array[mid])

  if array[left]!= array[mid]:
    findunique(array, left, mid-1)

  if array[mid]!= array[right]:
    findunique(array, mid+1, right)
findunique(array, 0, len(array)-1)  
  
print(list(hs))
