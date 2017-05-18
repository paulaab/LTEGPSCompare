import json
import ast
from datetime import datetime
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






gpsFile.close()
lteFile.close()

