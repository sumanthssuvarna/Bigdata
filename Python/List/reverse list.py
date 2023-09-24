#3. **List Reversal:** Write a function to reverse a list without using any built-in list reversal methods.

a=[4,2,8,1]
b=[]
for i in a[::-1]:
    b.append(i)
print(b)


#with built in
a=[4,2,8,1]
a.reverse()
print(a)