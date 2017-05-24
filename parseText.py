#!/usr/bin/python
import os
myFiles = ['JSONGPSData.json','JSONLTEData.json','JSONNnewLTEData.json','DataJoined.json']
for item in myFiles:
    if os.path.isfile(item):
        os.remove(item)



print ("Starting...")

import LTE_converter
import GPS_converter
import Comparer
import Join
print ("Done!")

