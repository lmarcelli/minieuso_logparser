import os 
import os.path
import sys
import numpy as np 
import pylab as pl
from datetime import datetime
from array import *
from pytz import timezone
from sys import argv
import pytz

#f='/home/laura/Scrivania/Mini-EUSO_Analisi/dati_minieuso/iss/20191106/logparser/grep_photodiode.txt'
f=argv[1]
path=f.split("grep")
workingdir=path[0]

temp_a = array('I', [])
unixtime_a = array('d', [])

print("\n...Parsing photodiode sensor counts ....")
print("from file: ", f)
with open(f) as fp:    
  myline=fp.readline() 
  cnt = 1
  #print(cnt, myline)
  cntok = 0	
  step = myline.split(" ")
  if ( len(step) == 8 and len(step[0]) == 10 ):
    #date format year/month/day
    date = step[0].split("/")	
    year = date[0]	
    month = date[1]
    day = date[2]
    #hour format h:m:s.xxxxxx
    hour = step[1].split(":")
    h = hour[0]	
    m = hour[1]
    second =hour[2].split(".")
    s=second[0]	
    ss=second[1]	
    b = datetime(int(year), int(month), int(day), int(h), int(m), int(s), int(ss), tzinfo=pytz.utc)
    #print(b)	
    unixtime=b.timestamp()
    unixtime_a.append(unixtime)	
    #print(type(unixtime))		
    #print(unixtime)
    #print(datetime.utcfromtimestamp(unixtime)) 	
    temp = step[7]
    temp_a.append(int(temp))	
    cntok += 1	
    #print(year, month, day, h, m, s,temp)	
  for myline in fp:	
     cnt += 1
     #print(cnt, myline)
     step = myline.split(" ")
     if (len(step) == 8  and len(step[0]) == 10 ):	
        #date format year/month/day
        date = step[0].split("/")	
        year = date[0]	
        month = date[1]
        day = date[2]
        #hour format h:m:s.xxxxxx
        hour = step[1].split(":")
        h = hour[0]	
        m = hour[1]
        second =hour[2].split(".")
        s=second[0]	
        ss=second[1]	
        b = datetime(int(year), int(month), int(day), int(h), int(m), int(s), int(ss), tzinfo=pytz.utc)	
        unixtime=b.timestamp()
        unixtime_a.append(unixtime)	
        #print(unixtime)
        #print(datetime.fromtimestamp(unixtime)) 
        temp = step[7]	
        temp_a.append(int(temp))
        cntok += 1		
  #print("nrows", cnt, "      nrow_ok", cntok, "\n\n")   	
     

pl.plot(unixtime_a, temp_a, 'r')
pl.xlabel('timeunix')
pl.ylabel('UV sensor counts')
#pl.hist(temp_a, 1000)
#pl.show()
#pl.savefig('/home/laura/Scrivania/Mini-EUSO_Analisi/dati_minieuso/iss/20191106/logparser/UV_Sensor_counts.png')
filepng=workingdir+"UV_Sensor_counts.png"
print("output file: ", filepng, "\n")
pl.savefig(filepng)




