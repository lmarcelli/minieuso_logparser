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

#f='/home/laura/Scrivania/Mini-EUSO_Analisi/dati_minieuso/iss/20191106/logparser/grep_hvpsstatus.txt'
f=argv[1]
path=f.split("grep")
workingdir=path[0]

mode_a = array('i', [])
mode_string = [] 
unixtime_a = array('d', [])

print("\n...Parsing hvps status....")
print("from file: ", f)
with open(f) as fp:    
  myline=fp.readline() 
  cnt = 1
  #print(cnt, myline)
  cntok = 0	
  step = myline.split(" ")
  if ( len(step) == 15 and len(step[0]) == 10 ):
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
    #print(unixtime)	
    unixtime_a.append(unixtime)	
    #print(type(unixtime))		
    #print(unixtime_a)	
    #print(datetime.fromtimestamp(unixtime)) 
    mode_string.append(step[6]+step[7]+step[8]+step[9]+step[10]+step[11]+step[12]+step[13]+step[14]) 	
    mode = int(step[6])*100000000+int(step[7])*10000000+int(step[8])*1000000+int(step[9])*100000+int(step[10])*10000+int(step[11])*1000+int(step[12])*100+int(step[13])*10+int(step[14])
    #print(mode)
    #print(type(mode))
    mode_a.append(mode)
    cntok += 1	
    #print(year, month, day, h, m, s,temp)	
  for myline in fp:	
     cnt += 1
     #print(cnt, myline)
     step = myline.split(" ")
     #print(type(step[6])) 	
     if ( len(step) == 15  and len(step[0]) == 10 and len(step[6]) == 1 ):	
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
        #print(datetime.utcfromtimestamp(unixtime)) 
        mode_string.append(step[6]+step[7]+step[8]+step[9]+step[10]+step[11]+step[12]+step[13]+step[14]) 
        #print(mode_string)
        mode = int(step[6])*100000000+int(step[7])*10000000+int(step[8])*1000000+int(step[9])*100000+int(step[10])*10000+int(step[11])*1000+int(step[12])*100+int(step[13])*10+int(step[14])
        mode_a.append(mode)	
        cntok += 1		
  #print(mode_a)
  #print("nrows", cnt, "      nrow_ok", cntok, "\n\n")  



pl.plot(unixtime_a, mode_a, 'r')
pl.xlabel('timeunix')
pl.ylabel('hvps status from zynq')
#pl.show()
filepng=workingdir+"hvps_status.png"
print("output file: ", filepng)
#pl.savefig('/home/laura/Scrivania/Mini-EUSO_Analisi/dati_minieuso/iss/20191106/logparser/hvps_status.png')
pl.savefig(filepng)


filetxt=workingdir+"hvps_status.txt"
print("output file: ", filetxt, "\n")
fileout = open(filetxt,"w") 	
#fileout = open("/home/laura/Scrivania/Mini-EUSO_Analisi/dati_minieuso/iss/20191106/logparser/hvps_status.txt","w") 

i = 0
#print(len(mode_a))
while i < len(mode_a): 
   fileout.write(("%f\t") % unixtime_a[i])	
   riga = str(datetime.utcfromtimestamp(unixtime_a[i]))
   fileout.write(riga)
   fileout.write("\thvps status")	 	
   fileout.write(("\t%s") % mode_string[i])	
   fileout.write("\n")    
   i = i+1  
fileout.close()




