import json
import ast
from datetime import datetime
from datetime import timedelta
gpsFile =  open('JSONGPSData.json','r')
lteFile = open('JSONLTEData.json','r')

gpsTime = []
lteTime=[]

gps = json.load(gpsFile)
lte = json.load(lteFile)




for i in range(0, len(gps)):
    gs = gps[str(i)]['time utc'][:19]
    t1 = datetime.strptime(gs, "%Y-%m-%dT%H:%M:%S")
    gpsTime.append(t1)



for i in range(0,len(lte)):
    ls = lte[str(i)]['time utc']
    t2 = datetime.strptime(gs, "%Y-%m-%dT%H:%M:%S")
    lteTime.append(t2)

delta = gpsTime[1]-lteTime[1]
delta=delta.apply(lambda x: x + timedelta(days=1) if x < 0 else x)

#if delta.days<0:
   # delta = timedelta(days=0,seconds=delta.seconds)


print (gpsTime[1])
print (lteTime[1])
print (delta)







gpsFile.close()
lteFile.close()

