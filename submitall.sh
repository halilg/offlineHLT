#EGamma JetHT MET SingleMuon 
pd=$1
crab submit -c crab_${pd}_hlt-v1x_2018A-v1.py
crab submit -c crab_${pd}_hlt-v20_2018A-v1.py
crab submit -c crab_${pd}_hlt-v20_2018A-v2.py
crab submit -c crab_${pd}_hlt-v21_2018A-v2.py
crab submit -c crab_${pd}_hlt-v21_2018A-v3.py
crab submit -c crab_${pd}_hlt-v21_2018B-v1.py
crab submit -c crab_${pd}_hlt-v22_2018B-v1.py

