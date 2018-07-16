#!/usr/bin/env zsh
#
asd=(hlt-v1x hlt-v20 hlt-v21 2018A 2018B)

set -x
for q in $asd; do
./harvest_pd_local.zsh ${1}_$q
done
set +x

