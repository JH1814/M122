arr = [1,2,3,4,3,5]
n = len(arr)

#insertion Sort------------------------------------------
for i in range(n):
  key = arr[i]
  j = i-1
  while(j >= 0 and arr[j] > key):
    arr[j+1] = arr[j]
    j = j-1
  arr[j+1] = key

#print sorted array
for a in range(n):
  print(arr[a])

#target for Search
target = 4

#binary search-------------------------------------------
def binary_search(arr, target):
  mid = 0
  low = 0
  high = n-1
  while(low <= high):
    mid = (high+low)//2
    #must be present in left half
    if(arr[mid]<target):
      low = mid+1
    #must be present in right half
    elif(arr[mid]>target):
      high = mid-1
    #is present at in the middle
    elif(arr[mid] == target):
      return mid
  #not present in the array
  return -1

#result
result = binary_search(arr, target)

#print out the result
if result != -1:
    print(target, "is present at index", result+1)
else:
    print(target, "is not present in array")






    