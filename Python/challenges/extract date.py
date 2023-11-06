a= 'hgfgfhfgmonth01987uyghhgdate2jhgfhgfgyear2021987987'
# '2021-01-23'
a=a.lower()

b=a.index("month")+5
if a[b+1].isnumeric():
  month=a[b:b+2]
else:
  month=a[b]

c=a.index("year")+4
year=a[c:c+4]

d=a.index("date")+4
if a[d+1].isnumeric():
  date=a[d:d+2]
else:
  date=a[d]



print(f"{year}-{month}-{date}")