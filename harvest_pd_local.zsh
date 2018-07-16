#!/usr/bin/env zsh
. ./common.zsh
checkCMSEnvironment

pd=$1
WDIR=$PWD
TDIR=$(mktemp -d)

lfname=list_${pd}_local.txt
ofname=DQM_step2_${pd}.root

cd $TDIR
echo Working in $PWD
cmsRun $WDIR/MULTIRUN_HARVESTING_listload.py $WDIR/$lfname || exit

cd $WDIR
rm -f $ofname
mv $TDIR/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root ./$ofname
echo "done: ./$ofname"
