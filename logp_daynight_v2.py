import os 
import os.path
import sys
import math 
import numpy as np 
import pylab as pl
from datetime import datetime
from array import *
from pytz import timezone
from sys import argv
import pytz

#f='/home/laura/Scrivania/Mini-EUSO_Analisi/dati_minieuso/iss/20191106/logparser/grep_daynight.txt'
f=argv[1]
path=f.split("grep")
workingdir=path[0]


mode_a = array('i', [])
unixtime_a = array('d', [])

print("\n...Parsing day/night transitions....")
print("from file: ", f)
with open(f) as fp:    
  myline=fp.readline() 
  cnt = 1
  #print(cnt, myline)
  cntok = 0	
  step = myline.split(" ")
  if ( len(step) == 6  and len(step[0]) == 10 ):
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
    #print(unixtime)
    unixtime_a.append(unixtime)	
    #print(type(unixtime))		
    #print(unixtime_a)
    #print(datetime.utcfromtimestamp(unixtime)) 	
    mode = step[4]
    #print(mode)
    if mode=="NIGHT":		
      mode_a.append(0)
    else:		
      mode_a.append(1)	
    cntok += 1	
    #print(year, month, day, h, m, s,temp)	
  for myline in fp:	
     cnt += 1
     #print(cnt, myline)
     step = myline.split(" ")
     if ( len(step) == 6   and len(step[0]) == 10 ):	
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
        mode = step[4]
        if mode=="NIGHT":		
           mode_a.append(0)
        else:		
           mode_a.append(1)		
        cntok += 1		
  #print(mode_a)
  #print(unixtime_a)	
  #print("nrows", cnt, "      nrow_ok", cntok, "\n\n")  
  

#fileout = open("/home/laura/Scrivania/Mini-EUSO_Analisi/dati_minieuso/iss/20191106/logparser/Day-Night_transitions.txt","w") 
filetxt=workingdir+"Day-Night_transitions.txt"
print("output file: ", filetxt, "\n")
fileout = open(filetxt,"w")	
i = 0
while i < len(mode_a): 
  if mode_a[i]==0:
     fileout.write("NIGHT:\t") 
     fileout.write(("%f\t") % unixtime_a[i])	
     riga = str(datetime.utcfromtimestamp(unixtime_a[i]))
     fileout.write(riga)
     if i < (len(mode_a)-1):  
       riga2 = str(datetime.utcfromtimestamp(unixtime_a[i+1])-datetime.utcfromtimestamp(unixtime_a[i]))
       #print(riga2)
       fileout.write("\tnight duration:\t")	
       fileout.write(riga2)	
     fileout.write("\n")    
  else:
     fileout.write("DAY:\t")  
     fileout.write(("%f\t") % unixtime_a[i])	
     riga = str(datetime.utcfromtimestamp(unixtime_a[i]))
     fileout.write(riga)
     if i < (len(mode_a)-1):  
       riga2 = str(datetime.utcfromtimestamp(unixtime_a[i+1])-datetime.utcfromtimestamp(unixtime_a[i]))
       #print(riga2)	
       fileout.write("\tday duration:\t")	 
       fileout.write(riga2)
     fileout.write("\n") 
  i = i+1  
fileout.close()



