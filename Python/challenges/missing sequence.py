a=[1,2,3,5,6,7]
for i in range(len(a)):
  if a[i]+1!=a[i+1]:
    a.insert(i+1,a[i]+1)

a 
#o/p : [1, 2, 3, 4, 5, 6, 7]