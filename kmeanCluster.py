from __future__ import print_function

from pyspark.ml.clustering import KMeans

from pyspark.sql import SparkSession

import json
import codecs
import re
import sys

if __name__ == "__main__":

    year = int(sys.argv[1])
    numCenter = int(sys.argv[2])
    filename = 'T'+str(year)+'.txt'
    spark = SparkSession\
        .builder\
        .appName("KMeansExample")\
        .getOrCreate()

    # $example on$
    # Loads data.
    dataset = spark.read.format("libsvm").load(filename)
    
    #print(dataset)
    # Trains a k-means model.
    kmeans = KMeans().setK(numCenter).setSeed(1)
    model = kmeans.fit(dataset)

    # Evaluate clustering by computing Within Set Sum of Squared Errors.
    wssse = model.computeCost(dataset)
    print("Within Set Sum of Squared Errors = " + str(wssse))

    # Shows the result.
    centers = model.clusterCenters()
    print("Cluster Centers: ")
    num = 0
    for center in centers:
        num = num + 1
        print(center)
    # $example off$

    spark.stop()
    
    fhand = codecs.open('where.js','w', "utf-8")
    fhand.write("year = "+str(year)+';\n')
    fhand.write("numCenters = "+str(numCenter)+';\n')
    fhand.write("myData = [\n")
    count = 0
    for row in centers :
        row = str(row)
        row = row.lstrip('[ ')
        row = row.rstrip(' ]')
        row = re.sub(' +',' ',row).split(' ')
        lang = float(row[0])
        lati = float(row[1])
        print(lang,lati)
        count = count + 1
        fhand.write('[' + str(lang) + ',' + str(lati) + ',' +"'Center" + str(count) + "']")
        if count<num :
            fhand.write(",\n")
        else:
            continue
    fhand.write("\n];\n")
    fhand.close()
    print(count, "records written to where.js")
    print("Open where.html to view the data in a browser")
