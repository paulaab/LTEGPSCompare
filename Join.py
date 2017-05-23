import json


gpsNewData = open('JSONGPSData.json','r')
lteNewData = open ('JSONNnewLTEData.json','r')

gp = json.load(gpsNewData)
lt = json.load(lteNewData)
x = 0
total = {}
for i in gp:
    z = gp[str(i)].copy()
    z.update(lt[str(i)])
    #total.append(z)
    total [x] = z
    x = x+1


jsonData = json.dumps(total)
with open('DataJoined.json', 'a') as f:
    f.write(jsonData + '\n')


print total
gpsNewData.close()
lteNewData.close()