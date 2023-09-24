from pyspark import SparkContext

sc=SparkContext("local[*]","Campaign_ads")

def boring(): #Opens up other file and strip the spaces of each low in a column
  aa=set(line.strip() for line in open("/content/drive/MyDrive/PySpark/Dummy datas/week10/boringwords.txt"))
  return aa

loc=sc.textFile("/content/drive/MyDrive/PySpark/Dummy datas/week10/bigdatacampaigndata-201014-183159.csv")#Open a text file
names=sc.broadcast(boring())#call file opening function
cols=loc.map(lambda x:(float(x.split(",")[10]),x.split(",")[0])) #map to the required column and convert datatype if required
devides=cols.flatMapValues(lambda x:x.split(" ")) #split each column based on delimiter
reverse=devides.map(lambda x: (x[1].lower(),x[0]))# interchange the values

filtered=reverse.filter(lambda  x:x[0] not in names.value) # Removes the boring words

final=filtered.reduceByKey(lambda x,y: x+y) #adds up same keys and sum of values


result=final.sortBy(lambda x:x[1],False).collect() #collect and sort the result

for i in result:
  print(i)