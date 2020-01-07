#! /bin/sh

WRKDIR=$1
OUTPUTDIR=$2


if [ "$1" = "-h" ] || [ "$1" = "--help" ]; then
  echo "Usage: two parameters are mandatory:" 
  echo "     1) LOG directory (with complete path) to be processed"
  echo "     2) working directory where to save output files"
  exit 0
fi


for file in $WRKDIR/*.log
do
 ls "$file"
 grep "average photodiode reading is" "$file" >> $OUTPUTDIR/grep_photodiode.txt 
 grep  "receiving via telnet" "$file" >> $OUTPUTDIR/grep_hvpsstatus.txt
 grep  "entering " "$file" >> $OUTPUTDIR/grep_daynight.txt
done

sleep 5s

python /home/laura/Scrivania/Mini-EUSO_Analisi/Software_analisi/LOG_parser/logp_photodiode_v2.py  $OUTPUTDIR/grep_photodiode.txt
python /home/laura/Scrivania/Mini-EUSO_Analisi/Software_analisi/LOG_parser/logp_daynight_v2.py  $OUTPUTDIR/grep_daynight.txt
python /home/laura/Scrivania/Mini-EUSO_Analisi/Software_analisi/LOG_parser/logp_hvpsstatus_v2.py  $OUTPUTDIR/grep_hvpsstatus.txt

python /home/laura/Scrivania/Mini-EUSO_Analisi/Software_analisi/LOG_parser/timeduration.py   $WRKDIR/
