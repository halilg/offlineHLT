#!/usr/bin/env zsh
#
asd=(hlt-v1x hlt-v20 hlt-v21 hlt-v22 hlt-v30 hlt-v31 hlt-v33 hlt-v34 2018A 2018B 2018C 2018D)

set -x
for q in $asd; do
./harvest_pd_local.zsh ${1}_$q
done
set +x

