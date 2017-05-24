import re
import json
import collections
with open('gpsTrace_runde1.txt', 'r') as gpsFile:
#with open('C:\\Users\\InnoGarage\\Desktop\\Paula\\Textfiles\\gpsTrace_runde1.txt', 'r') as gpsFile:
    i = 0
    myGPS = {}
    mySats = []
    data = {}
    ignore = [' GPS reading', '----------------------------------------', 'Killing', 'Done', 'Exiting','nan']

    for line in gpsFile:

        if line.strip():                                            #Ignore the blank lines
            if any(name in line for name in ignore):                #Ignore additional info
                continue
            else:
                if 'sats' in line:
                    start = line.find('[') + 1
                    end = line.find(']', start)
                    satsstring = line[start:end]
                    if satsstring == '':
                        empty = True
                    else:
                        empty = False
                        satsstring = satsstring.split(',')
                        for item in satsstring:
                            # Create dictionary for each one of the objects
                            item = re.findall('[A-Z][^A-Z]*', item)[2:]
                            item[0] = "PR" + item[0]
                            myDict = dict((k.strip(), v.strip()) for k, v in (item.split(':') for item in item))
                            mySats.append(myDict)
                    data['sats'] = mySats
                    # adding for each data object
                    if not empty:
                        #st = 'Pegel' + i
                        myGPS[i] = data
                        i = i + 1
                    data = {}
                    mySats = []
                elif 'time utc' in line:
                    times = list(map(str.strip, line[8:].split('+'))).pop(0)
                    data['time utc'] = times

                else:
                    field = ' '.join(re.findall("[a-zA-Z]+", line))
                    value = ''.join(re.findall(r'[-+]?\d+(?:\.\d+)?', line)).strip()

                    try:
                        value = float(value)
                    except ValueError as e:
                        continue
                    data[field] = value
    keylist = myGPS.keys()
    keylist.sort()

    #print (len(keylist))
    #for key in keylist:
     #   print "%s: %s" % (key, myGPS[key])
    #od = collections.OrderedDict(sorted(myGPS.items()))
    #print(myGPS)
    jsonData = json.dumps(myGPS)                                       #Save Python dictionary as JSON File
    with open('JSONGPSData.json', 'a') as f:
        #json.dump(jsonData, f)
        f.write(jsonData + '\n')




print ("Text file containing GPS Measurements parsed into JSON File.")
#DELETE A CHARACTER FROM A STRING
#newstr = oldstr.replace("M", "")
#EXTRACT SUBSTRING INSIDE STRING
#how to extract a substring from inside a string in Python?
#http://stackoverflow.com/questions/4666973/how-to-extract-a-substring-from-inside-a-string-in-python
