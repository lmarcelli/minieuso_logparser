import os 
import os.path
import sys
import math 
import numpy as np 
import pylab as pl
from datetime import datetime
from datetime import timedelta
from array import *
from pytz import timezone
from sys import argv
import pytz
import time


dir=argv[1]

filenamelist=[]
for path, subdirs, files in os.walk(dir):
    for filename in files:
        if filename.endswith('self.dat') and ("CPU_RUN_MAIN"  in filename) and not ("2019_10" in filename) :
            #filenamelist.append(os.path.join(path, filename))
            filenamelist.append(filename)
            #print(filename)
#print(filenamelist)


unixtime_a = array('d', [])
for filename in sorted(filenamelist):
    print(filename)
    step=filename.split("__")
    #print(step[1])
    step_d=step[1].split("_")
    #print(step[2])	
    step_t=step[2].split("_")	
    tu=datetime(int(step_d[0]),int(step_d[1]),int(step_d[2]),int(step_t[0]),int(step_t[1]),int(step_t[2]),0, tzinfo=pytz.utc)		 
    print(tu.timestamp())	
    unixtime_a.append(tu.timestamp())
#print(unixtime_a)


filetxt=dir+"logparser/timeduration.txt"
print("output file: ", filetxt, "\n")
fileout = open(filetxt,"w")
for filename in sorted(filenamelist):
    fileout.write(("%s\t") % filename)
fileout.write("\n\n\n")	
fileout.write("#file\t\tdate/time\t\t\tfile duration")
fileout.write("\n")	
i = 0
tempo_int = 0
while i < (len(unixtime_a)-1):
    nf=i+1
    fileout.write(("%i\t\t") % nf)	
    riga = str(datetime.utcfromtimestamp(unixtime_a[i]))
    fileout.write(riga)
    fileout.write("\t\t")		
    riga2 = str(datetime.utcfromtimestamp(unixtime_a[i+1])-datetime.utcfromtimestamp(unixtime_a[i]))
    fileout.write(riga2)
    fileout.write("\n")
    if((datetime.utcfromtimestamp(unixtime_a[i+1])-datetime.utcfromtimestamp(unixtime_a[i])).seconds<600): 		
         tempo_int = tempo_int + (datetime.utcfromtimestamp(unixtime_a[i+1])-datetime.utcfromtimestamp(unixtime_a[i])).seconds
    else:
         tempo_int = tempo_int + (datetime.utcfromtimestamp(unixtime_a[i])-datetime.utcfromtimestamp(unixtime_a[i-1])).seconds
    print(i)
    print((datetime.utcfromtimestamp(unixtime_a[i+1])-datetime.utcfromtimestamp(unixtime_a[i])))
    print((datetime.utcfromtimestamp(unixtime_a[i+1])-datetime.utcfromtimestamp(unixtime_a[i])).seconds)
    print(i, tempo_int)	
    print("\n")			
    i = i+1
fileout.write(("%i\t\t") % len(unixtime_a))
fileout.write(str(datetime.utcfromtimestamp(unixtime_a[len(unixtime_a)-1])))

#add the last interval 
tempo_int = tempo_int + (datetime.utcfromtimestamp(unixtime_a[len(unixtime_a)-1])-datetime.utcfromtimestamp(unixtime_a[len(unixtime_a)-2])).seconds
print("Adding the last interval: ", tempo_int)
print("\n\nnumber of file processed: ", len(unixtime_a))
print("total time: ", str(timedelta(seconds=tempo_int)))
fileout.write("\n\n\n")
fileout.write("number of file processed: \t")
fileout.write(str(len(unixtime_a)))
fileout.write("\n")
fileout.write("total time: \t")
fileout.write(str(timedelta(seconds=tempo_int)))

fileout.write("\n\n\n")
fileout.write("NOTE: Time duration is calculated using file name strings.\n")
fileout.write("In the calculation of 'total time', for files that have time duration 'unknown' (the following file is missing because not downloaded or for the entering in day mode), the duration of the previous file is taken into account.\n")


fileout.close()
 

