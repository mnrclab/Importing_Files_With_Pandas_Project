import pandas as pd
import pymongo
import datetime
dburl = 'mongodb://localhost:27017/'
mymongo = pymongo.MongoClient(dburl)

# MENGAKSES COLLECTION DALAM DATABASE 'pymongodb'
mydb = mymongo['pymongodb']
mycol = mydb['colmong']
alldata = list(mycol.find({},{"_id":0}))

#MEMBUAT DATAFRAME
df = pd.DataFrame(alldata)
print(df)