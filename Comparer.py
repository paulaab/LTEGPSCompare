
import json
import ast
from datetime import datetime
from datetime import timedelta
import numpy as np
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
    t2 = datetime.strptime(ls, "%Y-%m-%dT%H:%M:%S")
    lteTime.append(t2)

lteTimeUtc = []

#correcting lteTime to utc
for currentLTEtime in lteTime:
    lteTimeUtc.append(currentLTEtime- timedelta(hours=1))

#marking the position of every lteTime in original Data
lteTimeUtc = np.vstack((lteTimeUtc,range(len(lteTime)))).T






lteLowDelta = []


#compare lte and gps times.
for currentGPStime in gpsTime:
    lowestDelta = timedelta(days=365)
    lowestLTEtime = []
    for currentLTEtime in lteTimeUtc:
        currentDelta = abs(currentGPStime-currentLTEtime[0])
        #always save the lte time with the lowes difference towards the current gps time
        if(currentDelta < lowestDelta):
            lowestDelta = currentDelta
            lowestLTEtime = currentLTEtime
    lteLowDelta.append(lowestLTEtime)
print (len(lteLowDelta))
#creating new Json File from old file, so that all the data will be there
newLTEjson = {}
i=0
for a in lteLowDelta:
    newLTEjson[i]=(lte[str(a[1])])
    i = i + 1
jsonData = json.dumps(newLTEjson)                                       #Save Python dictionary as JSON File
with open('JSONNnewLTEData.json', 'a') as f:
    f.write(jsonData + '\n')










gpsFile.close()
lteFile.close()
