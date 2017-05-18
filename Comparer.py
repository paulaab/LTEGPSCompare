import json
import ast
from datetime import datetime
gpsFile =  open('JSONGPSData.json','r')
lteFile = open('JSONLTEData.json','r')

gpsTime = []
lteTime=[]

gps = json.load(gpsFile)
lte = json.load(lteFile)

print (gps['71']['time utc'])
#print (lte)


for i in range(0, len(gps)):

    gpsTime.append(gps[str(i)]['time utc'])



for i in range(0,len(lte)):


  lteTime.append(lte[str(i)]['time utc'])




t1 = datetime.strptime(gpsTime[1], "%Y-%m-")

gpsFile.close()
lteFile.close()

print(gpsTime)
print(lteTime)
