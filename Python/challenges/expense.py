a=['12','-$45','23','-34','-$76']
# 'epenseCount:3 expenseSum:154'
expenseCount=0
expenseSum=0
for i in a:
  if i.startswith("-"):
    i=i.replace("$","")
    i=i.replace("-","")
    expenseCount+=1
    expenseSum+=int(i)
print(expenseCount,expenseSum)