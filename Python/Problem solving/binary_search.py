a=[1, 22, 3,77, 4, 5, 6,0, 7, 8, 9, 10]
c=10
low=0
high=len(a)-1
while low<=high:
  mid=(low+high)//2
  if c==a[mid]:
    d=a[mid]
    break
  elif c>a[mid]:      
    low=mid+1
  else:
    high=mid-1

print(f'{d} found in the location {mid}')