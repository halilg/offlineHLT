#!/usr/bin/env zsh
# read configuration
. ./common.zsh
. ./config.zsh
echo PDs: $PDS

#PDS=(MET)


#checkGridProxy

hltvers=(hlt-v1x hlt-v20 hlt-v21)
eras=(2018A 2018B)

for pd in $PDS;do
	#echo $pd
	ofname=list_${pd}_local.txt
	rm -f $ofname
	find /afs/cern.ch/work/${USER:0:1}/$USER/data/topDQM/$pd -type f | grep .root | grep -v failed > $ofname
        sed -i -e 's/^/file:/' $ofname 
	wc -l $ofname

        for hlt in $hltvers; do
	   grep $hlt $ofname > list_${pd}_${hlt}_local.txt
	done

        for era in $eras; do
	   grep $era $ofname > list_${pd}_${era}_local.txt
	done

done
