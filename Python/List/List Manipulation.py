#9. **List Manipulation:** Write a function that takes a list of integers and returns a new list with each element squared.

a=[1,2,3,4,5,6,2,7,8,8,6,9,9]
b=[n*n for n in a]


#OR


a=[1,2,3,4,5,6,2,7,8,8,6,9,9]
b=[]
for i in range(len(a)):
  a[i]=a[i]*a[i]
  