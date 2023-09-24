from pyspark import SparkContext

sc=SparkContext("local[*]","Campaign_ads")

loc=sc.textFile("/content/drive/MyDrive/PySpark/Dummy datas/week10/bigdatacampaigndata-201014-183159.csv")
cols=loc.map(lambda x:(float(x.split(",")[10]),x.split(",")[0]))
devides=cols.flatMapValues(lambda x:x.split(" "))
reverse=devides.map(lambda x: (x[1].lower(),x[0]))
final=reverse.reduceByKey(lambda x,y: x+y)


result=final.sortBy(lambda x:x[1],False).collect()

for i in result:
  print(i)