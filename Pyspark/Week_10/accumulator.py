#Accumulator example


#!pip install pyspark py4j

from pyspark import SparkContext

def blankLineChecker (line):
  if(len(line) == 0): 
    myaccum.add(1)

sc = SparkContext("local[*]", "AccumulatorExample")

#Accumulator example

myrdd = sc.textFile("/content/drive/MyDrive/PySpark/Dummy datas/week10/abc.txt.txt")
myaccum =sc.accumulator (0.0)
myrdd.foreach (blankLineChecker)
print (myaccum.value)