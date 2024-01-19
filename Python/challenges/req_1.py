# python code to read an excel data model and print the output into json file.
# two files, columns -- filename,column_name,datatype 

import pandas as pd

df=pd.read_excel('/content/fffffffffffffff.xlsx')
df1=df['filename'].to_list()
df2=list(set(df1))
df3=df['column_name'].to_list()
df4=df['datatype'].to_list()

for i in df2:
  temp=""
  for j in range(len(df1)):
    if df1[j]==i:
      temp=temp + f"""
{{
  column  : {df3[j]} 
  datatype: {df4[j]}
}}
      """ 
  with open(f'/content/sample_data/{i}.json', 'w') as file:
    file.write(temp)
    print(f"Generated file for {i}")

