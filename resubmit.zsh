#!/usr/bin/env bash
#
D_BL=T1_UK_RAL
D_MJRT=1379

read -p "Blacklist [$D_BL]: " BL
BL=${BL:-$D_BL}
#echo $BL

read -p "Time [$D_MJRT]: " MJRT
MJRT=${MJRT:-$D_MJRT}
#echo $MJRT

read -p "Task: " TASK

set -x
crab resubmit --maxjobruntime $MJRT --siteblacklist=$BL crab_workspaces/$TASK
set +x
