a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
acount = 0
bcount = 0
while bcount < len(b):
  aNumber = a[acount]
  if a[acount] == b[bcount]:
    print(a[acount], b[bcount])
    acount += 1
  else:
    bcount += 1
