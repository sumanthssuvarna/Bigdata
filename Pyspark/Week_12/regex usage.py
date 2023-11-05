#This code is used to convert unstructured datafile to structured data

from pyspark.sql import SparkSession
from pyspark.sql.functions import regexp_extract
from pyspark.sql.functions import desc
spark=SparkSession.builder.appName("Sumanth_dev").getOrCreate()



df1=spark.read.text("/for week 4.txt")
df1.show()
my_reg=r'^(\S+)\s(\S+)\t(\S+),(\S+),(\S+)$'
df2=df1.select(regexp_extract('Value',my_reg,1).alias("Name"),regexp_extract('Value',my_reg,2).alias("age"),regexp_extract('Value',my_reg,3).alias("loc"),regexp_extract('Value',my_reg,4).alias("distance"),regexp_extract('Value',my_reg,5).alias("location"))
df2.show()