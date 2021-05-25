num = input("Enter the biggest number the list can contain ") 
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] 
lst = []

size = len(a)
for i in range(0, size-1):
  if(a[i] <= int(num)):
    lst.append(a[i])
print(lst)